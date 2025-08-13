from flask import render_template, url_for, request, redirect
from app import app
from app.service.autor_service import AutorService
from app.service.livro_service import LivroService
from app.models.livro_model import LivroModel
from app.models.autor_model import AutorModel

autores_service = AutorService()
livros_service = LivroService()

@app.route("/")
def index():
    return redirect(url_for("list_autores"))

@app.route("/autores")
def list_autores():
    autores = autores_service.get_all_autores()
    return render_template('autores/list.html', autores=autores)

@app.route("/autores/criar", methods=["GET", "POST"])
def create_autor():
    if request.method == "POST":
        nome = request.form["nome"]
        nacionalidade = request.form["nacionalidade"]
        data_nascimento = request.form["data_nascimento"]
        autor = AutorModel(id=None, nome=nome, nacionalidade=nacionalidade, data_nascimento=data_nascimento)
        autores_service.create_autor(autor)
        return redirect(url_for("list_autores"))
    return render_template("autores/form.html")

@app.route("/autores/editar/<int:id>", methods=["GET", "POST"])
def edit_autor(id):
    autor = autores_service.get_autor_by_id(id)
    if request.method == "POST":
        autor.set_nome(request.form["nome"])
        autor.set_nacionalidade(request.form["nacionalidade"])
        autor.set_data_nascimento(request.form["data_nascimento"])
        autores_service.update_autor(autor)
        return redirect(url_for("list_autores"))
    return render_template("autores/form.html", autor=autor)

@app.route("/autores/deletar/<int:id>")
def delete_autor(id):
    autores_service.delete_autor(id)
    return redirect(url_for("list_autores"))

@app.route("/livros")
def list_livros():
    livros = livros_service.get_all_livros()
    return render_template("livros/list.html", livros=livros)

@app.route("/livros/criar", methods=["GET", "POST"])
def create_livro():
    autores = autores_service.get_all_autores()
    if request.method == "POST":
        titulo = request.form["titulo"]
        genero = request.form["genero"]
        ano_publicacao = int(request.form["ano_publicacao"])
        autor_id = int(request.form["autor_id"])
        livro = LivroModel(id=None, titulo=titulo, genero=genero, ano_publicacao=ano_publicacao, autor_id=autor_id)
        livros_service.create_livro(livro)
        return redirect(url_for("list_livros"))
    return render_template("livros/form.html", autores=autores)

@app.route("/livros/editar/<int:id>", methods=["GET", "POST"])
def edit_livro(id):
    livro = livros_service.get_livro_by_id(id)
    autores = autores_service.get_all_autores()
    if request.method == "POST":
        livro.set_titulo(request.form["titulo"])
        livro.set_genero(request.form["genero"])
        livro.set_ano_publicacao(int(request.form["ano_publicacao"]))
        livro.set_autor_id(int(request.form["autor_id"]))
        livros_service.update_livro(livro)
        return redirect(url_for("list_livros"))
    return render_template("livros/form.html", livro=livro, autores=autores)

@app.route("/livros/deletar/<int:id>")
def delete_livro(id):
    livros_service.delete_livro(id)
    return redirect(url_for("list_livros"))
