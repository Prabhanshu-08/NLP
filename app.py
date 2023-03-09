import numpy as np
from flask import Flask, request, render_template
import tensorflow as tf

model = tf.keras.models.load_model('Disaster_tweet')


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():

    features = [x for x in request.form.values()]

    pred = round(model.predict([features],verbose=0)[0][0])

    if pred==0:
        return render_template('index.html',prediction_text = 'It is a just a random tweet')

    else:
        return render_template('index.html',prediction_text_1 = 'It is a tweet of disaster in happening....Please call the authorities.')


if __name__ == "__main__":
    app.run()