<<<<<<< HEAD
from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello():
    return """Hola desde Azure!
             Alejandro Soto Aguirre,
             Ing. Sistemas Computacionales,
             8vo semestre,
             21550303,
             Nuevo deploy"""

if __name__ == "__main__":
=======
from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello():
    return """Hola desde Azure!
             Alejandro Soto Aguirre,
             Ing. Sistemas Computacionales,
             8vo semestre,
             21550303"""

if __name__ == "__main__":
>>>>>>> 56187000028ed28eb4f63a834c5630f7c771e161
    app.run()