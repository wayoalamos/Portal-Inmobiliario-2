from search import Search

def count_words_at_url(url):
    s = Search() # create search element
    s.find_products(url) # find products of the urls
    return s.data
