# List Operations

# <list>.append(<element>)
#   adds a new element to the end of the List

# <list>+<list>
#   [0,1] + [2,3] = [0,1,2,3]

# loops on Lists
# while<test>:
#   Block

#<list>.index(<value>)
# returns the index of the first place the value is found in the list
# if value is not found in the list it returns an error

# <value> in <list>
# returns true/false if the value is in or not in the list

# <list>.pop()
# mutates the list by removing and returning its last element

# <string>.split()
# returns [<word1>, <word2>, ...s]


def better_crawl_web(seed,max_depth):
    tocrawl = [seed]
    crawled = [] #len(crawled) is length of crawled
    next_depth = []
    depth = 0
    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()
        if page not in crawled:
            union(next_depth, get_all_links(get_page(page)))
            crawled.append(page)
        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth = depth + 1
    return crawled

stooges = ['Moe','Larry','Curly']

def print_all_elements(p):
    for items in p:
        print(items)

print_all_elements(stooges)
