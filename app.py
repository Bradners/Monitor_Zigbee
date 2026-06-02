from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Datos globales
datos = {
    "temperatura": 0,
    "humedad": 0,
    "gas": 0,
    "movimiento": 0
}

# Página principal
@app.route('/')
def inicio():
    return render_template("index.html")

# Recibir datos del ESP32
@app.route('/datos', methods=['POST'])
def recibir_datos():
    global datos

    nuevo_dato = request.get_json()

    if nuevo_dato:
        datos["temperatura"] = nuevo_dato.get("temperatura", datos["temperatura"])
        datos["humedad"] = nuevo_dato.get("humedad", datos["humedad"])
        datos["gas"] = nuevo_dato.get("gas", datos["gas"])
        datos["movimiento"] = nuevo_dato.get("movimiento", datos["movimiento"])

        print("Datos:", datos)

        return jsonify({"estado": "ok"})

    return jsonify({"estado": "error"}), 400

# API para frontend
@app.route('/api/datos')
def api_datos():
    return jsonify(datos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)