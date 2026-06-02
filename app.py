from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Datos globales recibidos del ESP32
datos = {
    "temperatura": 0,
    "humedad": 0,
    "gas": 0,
    "movimiento": 0
}

# Página principal
@app.route('/')
def inicio():
    return render_template(
        "index.html",
        datos=datos
    )

# Recibir datos desde ESP32
@app.route('/datos', methods=['POST'])
def recibir_datos():
    global datos

    try:
        nuevo_dato = request.get_json()

        if nuevo_dato:
            datos["temperatura"] = nuevo_dato.get(
                "temperatura",
                datos["temperatura"]
            )

            datos["humedad"] = nuevo_dato.get(
                "humedad",
                datos["humedad"]
            )

            datos["gas"] = nuevo_dato.get(
                "gas",
                datos["gas"]
            )

            datos["movimiento"] = nuevo_dato.get(
                "movimiento",
                datos["movimiento"]
            )

            print("\n===== DATOS RECIBIDOS =====")
            print(datos)
            print("===========================\n")

            return jsonify({
                "estado": "ok",
                "mensaje": "Datos recibidos correctamente"
            }), 200

        return jsonify({
            "estado": "error",
            "mensaje": "JSON vacío"
        }), 400

    except Exception as e:
        return jsonify({
            "estado": "error",
            "mensaje": str(e)
        }), 500

# API para consultar datos actuales
@app.route('/api/datos')
def api_datos():
    return jsonify(datos)

# Estado del servidor
@app.route('/estado')
def estado():
    return jsonify({
        "servidor": "activo",
        "datos_actuales": datos
    })

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )