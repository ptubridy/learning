def get_next_target(page):
    start_link = page.find("_src")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 2)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


import urllib.request
import re
pat = re.compile('<DT><a href="[^"]+">(.+?)</a>')
url = 'https://www.instagram.com/ptubridy/followers/'
sock = urllib.request.urlopen(url).read().decode("utf-8")

li = pat.findall(sock)


links = get_all_links(sock)
with open("/Users/212329582/Documents/Udacity/InroToCS/outputfiles/linksfile.txt", mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(links))

with open("/Users/212329582/Documents/Udacity/InroToCS/outputfiles/sourcecodefile.txt", mode='wt', encoding='utf-8') as myfile:
    myfile.write(sock)
#desturl = "https://www.udacity.com/cs101x/index.html"
#page = get_page(desturl)
#links = get_all_links(page)
#for i in links:
#    print(i)
