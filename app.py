from flask import Flask, request
from modules.exception.mode_exception import ModeException
from modules.embeddings_generator import EmbeddingsGenerator

app = Flask(__name__)
eg = EmbeddingsGenerator()

@app.route('/')
def index():
    return "<p>Listening</p>"

@app.route('/embedding', methods=['GET', 'POST'])
def embedding():
    data = request.json
    mode = data.get('mode', '')
    text = data.get('text', '')

    try:
        embedding = eg.generate_embedding(input=text, mode=mode)
    except ModeException:
        return {'success': False, 'message': 'Invalid mode'}

    return {'success': True, 'embedding': embedding.tolist()}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
