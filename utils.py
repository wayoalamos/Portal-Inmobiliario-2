def count_words_at_url(url):
    s = Search() # create search element
    #s.workbook = Workbook() # create workbook element
    s.find_products(url) # find products of the urls

    # workbook = s.workbook
    return s.data
