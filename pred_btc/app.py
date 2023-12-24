import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pred')
def pred():
  return render_template('prediksi.html')


@app.route('/about')
def about():
  return render_template('about.html')
  


@app.route('/predict',methods=['POST'])
def predict():
  output = ""
    
  b = request.form['bulan']  

  # if b == 1:
  #   hasil = "Januari"
  # elif b == 2:
  #   hasil == "Februari"
  # else:
  #     hasil == "maret"

  int_features= request.form['price_open'],request.form['price_high'], request.form['price_low']
  
  if request.form['price_high'] < request.form['price_open'] :
    output = "Price High Tidak Boleh Lebih Kecil dari Price Open"
  elif request.form['price_low'] > request.form['price_high'] :
    output = "Price Low Tidak Boleh Lebih Besar dari Price High"
  else : 
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output ='Prediksi Harga Bitcoin Adalah : $ {} '.format(round(prediction[0],2))
    bul ='Bulan :  {b} '
  
  
  return render_template('prediksi.html', prediction_text=output, bu=b)

if __name__ == "__main__":  
    app.run(debug=True)