from search import Search
from openpyxl import Workbook
from flask import make_response
import openpyxl
import pyexcel

from search import Search
from openpyxl import Workbook

import time


def count_words_at_url(url):
    print("dddentro de la funcion count words return largo del url")
    a = len(url)

    """
    s = Search() # create search element
    s.workbook = Workbook() # create workbook element
    s.workbook_active = s.workbook.active

    # excel headers
    header=["Tipo", "Categoria", "Ubicacion", "Codigo", "Informacion",
    "Construido", "Terreno", "Valor(UF)", "UF/Construido", "UF/Terreno", "url"]
    s.workbook_active.append(header)

    # aca esta el problema
    s.find_products(url) # find products of the urls
    print("ttterminando la funcion")
    return s.workbook
    """
    count = 0
    for i in range(7):
        print("workerk working xD", i)
        time.sleep(1)

    print("time done con exito ")
    return str(a)
