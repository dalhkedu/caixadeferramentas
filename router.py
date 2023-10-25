import json

from flask import Flask, request, redirect, jsonify
from flask_cors import CORS
from projetos.encurtador_link import EncurtadorURL

app = Flask(__name__)
CORS(app)
encurtador = EncurtadorURL()


@app.route("/")
def index():
    return "Bem-vindo ao encurtador de links!"


@app.route("/encurtar", methods=["POST"])
def encurtar():
    if request.method == "POST":
        data = json.loads(request.data)
        url_longa = data.get("url_longa")
        url_curta = encurtador.encurtar_url(url_longa)
        return {'url_curta': url_curta}


@app.route("/<url_curta>")
def redirecionar(url_curta):
    url_longa = encurtador.redirecionar_url(url_curta)
    if url_longa:
        return redirect(url_longa)
    else:
        return "URL curta não encontrada."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
