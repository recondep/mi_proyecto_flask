from flask import Flask

# Crear una instancia de la aplicación Flask
mi_app = Flask(__name__)

# Ruta principal
@mi_app.route('/')
def pagina_principal():
    return '¡Saludos! Estás en mi aplicación Flask.'

# Ruta para mostrar un mensaje personalizado
@mi_app.route('/usuario/<nombre>')
def mostrar_usuario(nombre):
    return f'Hola, {nombre}! ¡Bienvenido a la aplicación!'

# Ejecutar la aplicación
if __name__ == '__main__':
    mi_app.run(debug=True)
