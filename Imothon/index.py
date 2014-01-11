#coding: utf-8

from flask import Flask
from flask import render_template
from flask import request
import MySQLdb

app = Flask(__name__)

con = MySQLdb.connect('54.207.12.211','root','root','imothon')


@app.route("/imothon")
def hello():
	return render_template('form.html')

@app.route('/add', methods=['POST'])
def add_entry():
	nome = request.form['nome']
	idade = request.form['idade']
	sexo = request.form['sexo']

	cursor = con.cursor()
	cursor.execute('insert into pessoas (nome,tel_comercial,sexo) values (%s, %s, %s)', [nome, idade, sexo])
	con.commit()
	return "Dados contratados com sucesso no sistema!!!!"

@app.route('/pessoas/')
def listar_pessoas():
	cursor = con.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('select * from pessoas')
	pessoas = cursor.fetchall()

	return render_template('pessoas.html',pessoas=pessoas)


app.debug = True
app.run()
