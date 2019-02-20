from search import Search
from openpyxl import Workbook
from flask import make_response
import openpyxl
import pyexcel

from search import Search
from openpyxl import Workbook

import time


def count_words_at_url(url):
    s = Search() # create search element
    #s.workbook = Workbook() # create workbook element
    my_workbook = workbook()

    #s.workbook_active = s.workbook.active
    my_workbook_active = my_workbook.active

    # excel headers
    header=["Tipo", "Categoria", "Ubicacion", "Codigo", "Informacion",
    "Construido", "Terreno", "Valor(UF)", "UF/Construido", "UF/Terreno", "url"]
    #s.workbook_active.append(header)
    my_workbook_active.append(header)

    # aca esta el problema
    s.find_products(url) # find products of the urls

    print("se termino la busqueda por url")
    for j in s.data:
        print (j)
        my_workbook_active.append(j)

    # workbook = s.workbook
    return "my_workbook"
