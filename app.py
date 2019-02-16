from flask import Flask, Response, request, render_template, make_response, redirect, url_for
import flask_excel as excel
from search import Search
from openpyxl import Workbook
import openpyxl
import pyexcel

from rq import Queue
from rq.job import Job

from worker import conn
from search import Search
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
    print("post method")
    text = request.form['text'] # url from webpage
    url = str(text)

    q = Queue(connection=conn)
    task = q.enqueue(count_words_at_url, url)

    #result = task.result
    task_id = task.get_id()

    return redirect(url_for('waiting', task_id=task_id))
    """
    return str(result)
    output = make_response(openpyxl.writer.excel.save_virtual_workbook(result))
    output.headers["Content-Disposition"] = "attachment; filename=Datos.xlsx"
    output.headers["Content-type"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    return result
    """

@app.route("/waiting/<task_id>")
def waiting(task_id):
    job = Job.fetch(task_id, connection=conn)
    start_time = time.time()
    while not job.is_finished:
        if time.time() - start_time > 25:
            print("la solicitud se ha demorado mas de 25 segundos, se redirege a la url waiting!!!!!!!!!!!!")
            return redirect(url_for('waiting', task_id=task_id))
        time.sleep(1)
    return job.result

if __name__ == '__main__':
    excel.init_excel(app)
    app.run(debug=True, use_reloader=True)
    # app.run()
