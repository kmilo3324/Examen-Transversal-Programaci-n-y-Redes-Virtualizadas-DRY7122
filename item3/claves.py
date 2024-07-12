import hashlib
import sqlite3
from flask import Flask, request, jsonify

# Configuración básica de la aplicación Flask
app = Flask(__name__)

# Ruta para la autenticación de usuarios
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Verificar las credenciales
    if username and password:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Conectar a la base de datos y verificar usuario
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE username=? AND password=?', (username, hashed_password))
        user = cursor.fetchone()
        conn.close()

        if user:
            return jsonify({'message': 'Login exitoso'})
        else:
            return jsonify({'message': 'Credenciales inválidas'}), 401
    else:
        return jsonify({'message': 'Faltan datos de autenticación'}), 400

# Ruta para crear nuevos usuarios
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    username = request.json.get('username')
    password = request.json.get('password')

    # Verificar que se hayan proporcionado ambos campos
    if username and password:
        # Hashear la contraseña antes de almacenarla
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Conectar a la base de datos y almacenar el usuario
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        
        try:
            cursor.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
            conn.close()
            return jsonify({'message': 'Usuario creado exitosamente'})
        except sqlite3.IntegrityError:
            conn.close()
            return jsonify({'message': 'El usuario ya existe'}), 400
    else:
        return jsonify({'message': 'Faltan datos para crear el usuario'}), 400

if __name__ == '__main__':
    # Crear la base de datos y la tabla si no existen
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Ejemplo de inserción de usuarios (con contraseñas hasheadas)
    usuarios = [
        ('usuario1', hashlib.sha256('password1'.encode()).hexdigest()),
        ('usuario2', hashlib.sha256('password2'.encode()).hexdigest())
    ]

    cursor.executemany('INSERT OR IGNORE INTO usuarios (username, password) VALUES (?, ?)', usuarios)
    conn.commit()
    conn.close()

    # Ejecutar la aplicación Flask en el puerto 5800
    app.run(port=5800)
