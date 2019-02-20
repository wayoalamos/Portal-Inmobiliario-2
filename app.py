from flask import Flask, Response, request, render_template, make_response, redirect, url_for
import flask_excel as excel
from openpyxl import Workbook
import openpyxl
import pyexcel

from rq import Queue
from rq.job import Job

from worker import conn
from utils import count_words_at_url

import time

# fix dimensiones por la coma que hay se separan en dos valores distintos en el excel
app = Flask(__name__)

counter = 0

@app.route('/')
def homepage():
    return render_template('index.html', data=counter)

@app.route("/", methods=["POST"])
def getPlotCSV():
    text = request.form['text'] # url from webpage
    url = str(text)

    q = Queue(connection=conn) # create de queue
    task = q.enqueue(count_words_at_url, url)
    task_id = task.get_id()
    return redirect(url_for('waiting', task_id=task_id))

@app.route("/waiting/<task_id>")
def waiting(task_id):
    job = Job.fetch(task_id, connection=conn)
    start_time = time.time()
    while not job.is_finished:
        if time.time() - start_time > 25:
            print("la solicitud se ha demorado mas de 25 segundos, se redirege a la url waiting!!!!!!!!!!!!")
            return redirect(url_for('waiting', task_id=task_id))

    result = job.result
    my_workbook = Workbook()
    my_workbook_active = my_workbook.active

    # excel headers
    header=["Tipo", "Categoria", "Ubicacion", "Codigo", "Informacion",
    "Construido", "Terreno", "Valor(UF)", "UF/Construido", "UF/Terreno", "url"]
    my_workbook_active.append(header)

    for j in result:
        my_workbook_active.append(j)

    output = make_response(openpyxl.writer.excel.save_virtual_workbook(my_workbook))
    output.headers["Content-Disposition"] = "attachment; filename=Datos.xlsx"
    output.headers["Content-type"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    print("excel esta listo para ser retornado suerte")


    return output

if __name__ == '__main__':
    excel.init_excel(app)
    app.run(debug=True, use_reloader=True)
    # app.run()
