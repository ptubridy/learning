# Latency
# time it takes message to from source to destination
# measured in mili seconds

# Bandwidth
# amount of information that can be transmitted per unit time
# measured in mega bits per second

# bit
# 1 bit = smallest unit of information
# the answer to on question
def get_page(url):
    try:
        import urllib

        return urllib.urlopen(url).read()
    except:
        return ""

file = open("newfile.txt", "w")
test = "http://www.udacity.com/cs101x/index.html"
web = get_page(test)
