from flask import Flask, jsonify, render_template, request
import os
import predictions

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        #dados = request.form
        #y_pred = predictions.predict()

        return jsonify(request.form['comp_petala'])
    else:
        return jsonify({"mensagem" : "utilize o formulario"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
