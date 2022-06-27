import os, datetime
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from unidecode import unidecode

#Conecta ao banco de dados sqlite database.db
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask(__name__)
app.config["SECRET_KEY"] = 'your secret key'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

connection = sqlite3.connect('database.db',check_same_thread=False)
c = connection.cursor()

# é necessário retornar os valores em forma de dicionário e, em todas as rotas criadas, ao executar a query, dava erro.
# Então criei essa lista com o nome de todas as colunas do banco de dados, para então conseguir retornar no formato chave:valor

lista = ['id', 'created', 'nome', 'cpf', 'email', 'dataNascimento', 'titulo',
         'categoria', 'descricaoservico', 'rua', 'bairro', 'cidade', 'estado', 'cep',
         'tipoderedesocial1', 'link1', 'tipoderedesocial2', 'link2', 'tipoderedesocial3', 'link3',
         'numero1', 'numero2', 'numero3', 'numero4']

#Modelo do banco de dados de acordo com a tabela criada em esquema.sql
class Cadastro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    nome = db.Column(db.String(40), nullable=False)
    cpf = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    dataNascimento = db.Column(db.String(30), nullable=False)
    titulo = db.Column(db.String(30), nullable=True)
    categoria = db.Column(db.String(30), nullable=False)
    descricaoservico = db.Column(db.String(200), nullable=False)
    rua = db.Column(db.String(50), nullable=False)
    bairro = db.Column(db.String(30), nullable=False)
    cidade = db.Column(db.String(30), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    tiporedesocial1 = db.Column(db.String(30), nullable=True)
    link1 = db.Column(db.String(50), nullable=True)
    tiporedesocial2 = db.Column(db.String(30), nullable=True)
    link2 = db.Column(db.String(50), nullable=True)
    tiporedesocial3 = db.Column(db.String(30), nullable=True)
    link3 = db.Column(db.String(50), nullable=True)
    numero1 = db.Column(db.String(11), nullable=False)
    numero2 = db.Column(db.String(11), nullable=True)
    numero3 = db.Column(db.String(11), nullable=True)
    numero4 = db.Column(db.String(11), nullable=True)


#rotas
@app.route("/", methods=["GET", "POST"])
def home():
    cadastros = Cadastro.query.all()
    return render_template("index.html", cadastros=cadastros)

@app.route("/anunciar", methods=["GET"])
def anunciar():
    return render_template("new.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome'][:30]
        cpf = request.form['cpf'][:12]
        email = request.form['email'][:30]
        dataNascimento = request.form['dataNascimento'][:10]
        titulo = request.form['titulo'][:150]
        categoria = request.form['categoria'][:20]
        descricaoservico = request.form['descricaoservico'][:200]
        rua = request.form['rua'][:40]
        bairro = unidecode(request.form['bairro'].capitalize())[:30]
        cidade = unidecode(request.form['cidade'].capitalize())[:30]
        estado = request.form['estado']
        cep = request.form['cep'][:9]
        tiporedesocial1 = request.form['tiporedesocial1'][:15]
        link1 = request.form['link1'][:50]
        tiporedesocial2 = request.form['tiporedesocial2'][:15]
        link2 = request.form['link2'][:50]
        tiporedesocial3 = request.form['tiporedesocial3'][:15]
        link3 = request.form['link3'][:50]
        numero1 = request.form['numero1'][:12]
        numero2 = request.form['numero2'][:12]
        numero3 = request.form['numero3'][:12]
        numero4 = request.form['numero4'][:12]

        if not nome:
            flash("O Nome é obrigatório")
        elif not cpf:
            flash("O CPF é obrigatório")
        elif not dataNascimento:
            flash("A data de nascimento é obrigatória")
        elif not descricaoservico:
            flash("A descrição do serviço é obrigatória")
        elif not rua:
            flash("A rua é obrigatória")
        elif not bairro:
            flash("O bairro é obrigatório")
        elif not cidade:
            flash("A cidade é obrigatória")
        elif not estado:
            flash("O estado é obrigatório")
        elif not cep:
            flash("O CEP é obrigatório")
        elif not numero1:
            flash("Ao menos um número de telefone é obrigatório")

        else:
            cadastro= Cadastro(nome=nome, cpf=cpf, email=email, dataNascimento=dataNascimento, titulo=titulo,
                                categoria=categoria, descricaoservico=descricaoservico, rua=rua, bairro=bairro,
                                cidade=cidade, estado=estado, cep=cep, tiporedesocial1=tiporedesocial1, link1=link1,
                                tiporedesocial2=tiporedesocial2, link2=link2, tiporedesocial3=tiporedesocial3,
                                link3=link3, numero1=numero1, numero2=numero2, numero3=numero3, numero4=numero4)
            db.session.add(cadastro)
            db.session.commit()
            return redirect(url_for('ultimosanuncios'))

    return render_template("cadastro.html")

@app.route('/categoria/<categoria>')
def categoria(categoria):
    #as variáveis global connection, global c e global lista fazem referencia as variáveis definidas fora da função.
    global connection
    global c
    global lista
    query = "SELECT * FROM cadastro WHERE categoria= '" + categoria + "' "
    c.execute(query)
    resultados = c.fetchall()
    result_as_dict = []
    for i in range(len(resultados)):
        result_as_dict.append({k: resultados[i][lista.index(k)] for k in lista})
    return jsonify(result_as_dict)

@app.route('/cidade/<cidade>')
def cidade(cidade):
    global connection
    global c
    global lista
    query = "SELECT * FROM cadastro WHERE cidade= '" + cidade + "' "
    c.execute(query)
    resultados = c.fetchall()
    result_as_dict = []
    for i in range(len(resultados)):
        result_as_dict.append({k: resultados[i][lista.index(k)] for k in lista})
    return jsonify(result_as_dict)

@app.route('/ultimosanuncios')
def ultimosanuncios():
    global connection
    global c
    global lista
    query = "SELECT * FROM cadastro ORDER BY id DESC LIMIT 20"
    c.execute(query)
    resultados = c.fetchall()
    result_as_dict = []
    for i in range(len(resultados)):
        result_as_dict.append({k: resultados[i][lista.index(k)] for k in lista})
    return jsonify(result_as_dict)

@app.route('/sobre')
def sobre():
    return render_template("about.html")