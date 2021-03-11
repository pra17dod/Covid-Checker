import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route("/")
def home():
    return render_template("medical-form.html")

@app.route('/predict', methods=['POST'])
def predict():

    features = [int(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = prediction

    return render_template('result.html', prediction = "You are Corona {}".format(output))

if __name__ == "__main__":
    app.run(debug=True)