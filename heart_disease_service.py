import pickle
import pandas as pd
from flask import Flask, request

#load model
with open('knn_heart_disease.pkl', 'rb') as file:
    classifier = pickle.load(file)

# #coś przewisuję - dane to ROW, pamietać żeby dać 13 wartosci, bo 14 to target usunieta z trenowania modelu
# data = [[61, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]]
# df = pd.DataFrame(data)
# prediction = classifier.predict(data)
# print(prediction)

app = Flask(__name__)

@app.route('/KNN-heart-disease', methods=["POST"])
def knn_heart_disease():
    data = request.get_json(force=True)
    df = pd.DataFrame(data, index=[0]) #bo dane to słownik a nie 2D tablica, dlatego trzeba podać index
    prediction = classifier.predict(df) #numpy array
    if prediction[0] == 0:
        return "No presenece of heart disease detected."
    else:
        return "Presece of heart disease detected."

if __name__ == "__main__":
    app.run(port=9000)