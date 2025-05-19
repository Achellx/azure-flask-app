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
    app.run()