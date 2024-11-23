import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = '../models/mushroom_model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('class')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    class_pred = y_pred >= 0.5

    result = {
        'class_probability': float(y_pred),
        'class': bool(class_pred)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)