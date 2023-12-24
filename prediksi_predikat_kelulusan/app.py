# import sklearn
# from process import preparation, generate_response
from flask import Flask, render_template, request
from model import load, prediksi
# import pickle
app = Flask(__name__)

# # load model dan scaler
load()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route("/get")
def get_bot_response():
    user_input = str(request.args.get('msg'))
    result = generate_response(user_input)
    return result

@app.route('/prediksi')
def prediksi():
    return render_template('prediksi.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/predict", methods=["POST"])
def predict():

    ips1 = int(request.form['ips1'])
    ips2 = int(request.form['ips2'])
    ips3 = int(request.form['ips3'])
    ips4 = int(request.form['ips4'])
    ips5 = int(request.form['ips5'])
    ips6 = int(request.form['ips6'])
    ips7 = int(request.form['ips7'])
    ips8 = int(request.form['ips8'])


        
    data_baru = [[ips1, ips2, ips3, ips4, ips5, ips6, ips7, ips8]]
    prediction_result= prediksi(data_baru)
    # prediction_result = int(prediction_result)
    return render_template('prediksi.html', hasil_prediksi=prediction_result)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)