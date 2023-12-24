import pickle

# global variable
global model,scaler

def load():
    global model, scaler
    model = pickle.load(open('model/model.pkl', 'rb'))
    scaler = pickle.load(open('model/scaler.pkl', 'rb'))

def prediksi(data_baru):
    data_baru = scaler.transform(data_baru)
    prediksi = int(model.predict(data_baru))
    if prediksi == 'A':
        hasil_prediksi = 'Sangat Baik'
    elif prediksi == 'B':
        hasil_prediksi = 'Baik'
    elif prediksi == 'C':
        hasil_prediksi = 'Cukup'
    elif prediksi == 'D':
        hasil_prediksi = 'Buruk'
    return hasil_prediksi
   
    