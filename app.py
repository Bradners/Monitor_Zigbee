from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

datos = {
    "temperatura": 0,
    "humedad": 0,
    "gas": 0,
    "movimiento": 0
}

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/datos', methods=['POST'])
def recibir_datos():
    global datos
    nuevo_dato = request.get_json()

    if nuevo_dato:
        datos.update(nuevo_dato)
        print(datos)
        return jsonify({"estado": "ok"})

    return jsonify({"estado": "error"}), 400


@app.route('/api/datos')
def api_datos():
    return jsonify(datos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)