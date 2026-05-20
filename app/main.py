# API de usuarios - IAS

import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# "Base de datos" en memoria
usuarios = []
next_id = 1

# Endpoint 1: Healthcheck
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

# Endpoint 2: Listar y crear usuarios
@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    return jsonify(usuarios)

@app.route("/usuarios", methods=["POST"])
def crear_usuario():
    global next_id
    data = request.get_json()
    if not data or "nombre" not in data:
        return jsonify({"error": "Falta el campo 'nombre'"}), 400
    usuario = {"id": next_id, "nombre": data["nombre"]}
    usuarios.append(usuario)
    next_id += 1
    return jsonify(usuario), 201

# Endpoint 3: Obtener y eliminar un usuario por ID
@app.route("/usuarios/<int:user_id>", methods=["GET"])
def get_usuario(user_id):
    usuario = next((u for u in usuarios if u["id"] == user_id), None)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(usuario)

@app.route("/usuarios/<int:user_id>", methods=["DELETE"])
def eliminar_usuario(user_id):
    global usuarios
    usuario = next((u for u in usuarios if u["id"] == user_id), None)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    usuarios = [u for u in usuarios if u["id"] != user_id]
    return jsonify({"mensaje": "Usuario eliminado"})

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"mensaje": "pong"})

if __name__ == "__main__":
    debug = os.getenv("DEBUG", "false").lower() == "true"
    app.run(debug=debug)

