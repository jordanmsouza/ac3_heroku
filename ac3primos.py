import os
from flask import Flask, jsonify, request
from math import sqrt


app = Flask(__name__)

@app.route('/')
def cem_primos():
    a = 1000
    cont = 0
    lista = []
    for i in range(1, a):
        j = 0
        for j in range(1, a):
            if i % j == 0:
                cont += 1
        if cont == 2:
            lista.append(i)
        if len(lista) >= 100:
            break
        cont = 0
    return lista


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

