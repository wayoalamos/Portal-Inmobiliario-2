from search import Search

def count_words_at_url(url):
    s = Search() # create search element
    s.find_products(url) # find products of the urls
    t = ""
    for i in s.data:
        l = ""
        for j in i:
            l += j + "°x^"
        l.rstrip("°x[^")
        t += l + "~w{"
    t.rstrip("~w{")
    return t
