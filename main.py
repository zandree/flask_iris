from flask import Flask, jsonify, render_template, request
import os
import predictions
import torch

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        #larg_sepala, comp_sepala, larg_petala, comp_petala
        #['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
        dados = [
            float(request.form['comp_sepala']),
            float(request.form['larg_sepala']),
            float(request.form['comp_petala']),
            float(request.form['larg_petala'])
        ]
        y_pred = predictions.predict(dados)
        # print(y_pred)
        # return jsonify({"result": y_pred})
        #y_pred = (torch.round(y_pred, decimals=2))
        return jsonify({
            "versicolor" : f'{y_pred[0]}',
            "setosa" : f'{y_pred[1]}',
            "virginica" : f'{y_pred[2]}'
            })
    else:
        return jsonify({"mensagem" : "utilize o formulario"})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))