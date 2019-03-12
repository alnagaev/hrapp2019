from flask import Flask, render_template, url_for, request
import json

from science import find_worker

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('index.html')


@app.route('/worker', methods=['GET', 'POST'])
def worker():
	return render_template('worker.html')


@app.route('/data', methods=['GET', 'POST'])
def data():
	_, jsons = find_worker(request.form)
	# jsons = [{'first': 'hr', 'second': 25000, 'third': '3 years', 'fourth': 'Full', 'fifth': 'Senior cladovshik', 'sixth':'<p>Стрессоустойчивость.</p><p>Коммуникабельность.</p><p>Общительность.</p><p>Легко нахожу общий язык с людьми.</p><p>Желание развиваться.</p><p>Вредных привычек не имею.</p>',
	# 'seventh': '<p>Уверенный пользователь ПК.</p><p>Компьютерные навыки и знания:&nbsp;&nbsp;&nbsp;&nbsp; Работа с ОС WindowsXp, 2007, 8, 10,Vista.</p><p>Офисныеприложения: Microsoft Office (Excel, Word, PowerPoint, Access).</p><p>Графические редакторы: AdobePhotoshop, Rhinoceros.</p><p>Браузеры: Opera, Internet Explorer, Mozzilla Firefox, Safari.</p><p>Антивирусы: Eset Nod, Dr.Web, Kaspersky.</p><p>Знание программы 1С, СБИС.</p><p>Текстовые и видео системы ведения переговоров: Skype, ICQ, GoogleTalk.</p>',
	# 'score': 228}]
	return render_template('data.html', results=jsons)


@app.route('/employer', methods=['GET', 'POST'])
def employer():
	return render_template('employer.html')


if __name__ == '__main__':
	app.run(debug=True)
