from flask import Flask, jsonify, request # del paquete importa la clase flask
#from markupsafe import escape #No importa que recibo, lo interpreto com cadena de caractres (esto sirve para evitar que nos peguen un script en la url)
#modulo request permite...(?)---> request en una variable local a cada consulta. Es un contexto local en cada consulta y NO una variable global


app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/ping')
def ping():
    return 'Pong' # Nombre la funcion que se ejecuta al pasar por la ruta establecida en 

@app.route('/usuarios/<string:nombre>')
def usuario_by_name(nombre):
    return jsonify({"name": nombre})


@app.route('/usuarios/<int:id>')
def usuario_by_id(id):
    return jsonify({"id": id})


# sin importar el markupsafe aca se podria insertar codigo malicioso
@app.route('/<path:nombre>')
def danger(nombre):
    return nombre

@app.route('/recurso', methods = ['GET'])
def get_recursos():
    return jsonify({"data" : "lista de todos los item de este recurso"})


@app.route('/recurso', methods=['POST'])
def post_recurso():
    print(request.get_json())
    body = request.get_json()
    name = body["name"]
    modelo = body["modelo"]
    #Insertar en la BD
    return jsonify({"recurso": {
        "name": name,
        "modelo": modelo
    }})

#GET de un 'recurso' particular a traves de id
@app.route('/recurso/<int:id>', methods = ['GET'])
def get_recurso_by_id(id):
    #buscar en la BD un registro con ese id
    return jsonify({"recurso": {
        "name":"nombre correspondiente a ese id",
        "modelo": "modelo correspondiente a ese id"
    }})



 



















if __name__ == '__main__':
    app.run(debug = True, port = 5000)

