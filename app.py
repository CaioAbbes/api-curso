from flask import Flask, jsonify, request
from config import Config
from models import db, Curso
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/get_cursos', methods=['GET'])
def get_cursos():
    try:
       
        cursos = Curso.query.all()
        cursos_json = []

        for curso in cursos:
            curso_data = {
                'id_curso': curso.id_curso,
                'titulo': curso.titulo,
                'sub_titulo': curso.sub_titulo,
                'descricao': curso.descricao,
                'preco': curso.preco,
                'imagem': curso.imagem,
                'id_professor': curso.id_professor
            }
            cursos_json.append(curso_data)

        if len(cursos_json) > 0:
            return jsonify({'Curso': True, 'Mensagem': cursos_json})
    
        return jsonify({'Curso': False, 'Mensagem': 'Nenhum curso encontrado!'}), 404

    except Exception as e:
        logging.error(f"Erro no get_cursos: {e}")
        db.session.rollback()
        return jsonify({'Curso': False, 'Mensagem': str(e)}), 500
    
@app.route('/get_curso_id', methods=['GET'])
def get_curso_id():
    try:
       
        id_curso_entry = request.args.get('id_curso')

        curso = Curso.query.filter_by(id_curso=id_curso_entry).first()

        return jsonify({'Curso': True, 'Mensagem': {
            'id_curso': curso.id_curso,
            'titulo': curso.titulo,
            'sub_titulo': curso.sub_titulo,
            'descricao': curso.descricao,
            'preco': curso.preco,
            'imagem': curso.imagem,
            'id_professor': curso.id_professor
        }})
    
    except Exception as e:
        logging.error(f"Erro no get_curso_id: {e}")
        db.session.rollback()
        return jsonify({'Curso': False, 'Mensagem': str(e)}), 500
    
  
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5002)
