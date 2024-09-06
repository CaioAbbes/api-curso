from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Curso(db.Model):
    __tablename__ = 'curso'

    id_curso = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(300), nullable=False)
    sub_titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.String(300), nullable=False)
    preco = db.Column(db.Numeric(19, 2), nullable=False)
    imagem = db.Column(db.String(300), nullable=False)
    id_professor = db.Column(db.Integer, nullable=False)