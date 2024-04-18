from flask import Flask,render_template,url_for,request, redirect, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
import flasgger
from flasgger import Swagger
import pickle
from flaskext.mysql import MySQL
import os
import pandas as pd
from datetime import datetime
from werkzeug.utils import secure_filename
import numpy as np
import plotly.express as px
import csv
import string
import plotly.io as pio
import json
from pymysql.cursors import DictCursor
import emoji
from datetime import datetime

UPLOAD_FOLDER = 'static/file_upload/'
ALLOWED_EXTENSIONS = {'csv'}

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MYSQL_DATABASE_HOST	'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Jundixxx.000'
app.config['MYSQL_DATABASE_DB'] = 'db_kinerja_dpr'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.secret_key = 'check'

mysql = MySQL(cursorclass=DictCursor)
mysql.init_app(app)
Swagger(app)

model = pickle.load(open('model/nbtune.pkl','rb'))
model2 = pickle.load(open('model/knntune.pkl','rb'))
countVect = pickle.load(open('model/vectorizenbrnew.pkl','rb'))
countVect2 = pickle.load(open('model/vectorizerknntune.pkl','rb'))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

def unicode_escape(chars, data_dict):
    return chars.encode('unicode-escape').decode()

@app.route('/')
def home():
    con_hasil = mysql.get_db().cursor()
    con_positif = mysql.get_db().cursor()
    con_negatif = mysql.get_db().cursor()
    query = ("SELECT MONTH(date) as month, count(labelling) as count FROM tweet group by month order by month ASC");
    query_positif = ("SELECT case when helper.month = 1 then 'Januari' when helper.month = 2 then 'Februari' when helper.month = 3 then 'Maret' when helper.month = 4 then 'April' when helper.month = 5 then 'Mei' when helper.month = 6 then 'Juni' when helper.month = 7 then 'Juli' when helper.month = 8 then 'Agustus' when helper.month = 9 then 'September' when helper.month = 10 then 'Oktober' when helper.month = 11 then 'November' when helper.month = 12 then 'Desember' end as month, count(tweet.labelling) as count FROM tweet inner join (SELECT id,month(date) as month FROM tweet) as helper on helper.id = tweet.id where labelling='Positif' GROUP by helper.month order by helper.month");
    query_negatif = ("SELECT case when helper.month = 1 then 'Januari' when helper.month = 2 then 'Februari' when helper.month = 3 then 'Maret' when helper.month = 4 then 'April' when helper.month = 5 then 'Mei' when helper.month = 6 then 'Juni' when helper.month = 7 then 'Juli' when helper.month = 8 then 'Agustus' when helper.month = 9 then 'September' when helper.month = 10 then 'Oktober' when helper.month = 11 then 'November' when helper.month = 12 then 'Desember' end as month, count(tweet.labelling) as count FROM tweet inner join (SELECT id,month(date) as month FROM tweet) as helper on helper.id = tweet.id where labelling='negatif' GROUP by helper.month order by helper.month");
    con_hasil.execute(query)
    con_positif.execute(query_positif)
    con_negatif.execute(query_negatif)
    hasil = con_hasil.fetchall()
    positif = con_positif.fetchall()
    negatif = con_negatif.fetchall()    
    response = jsonify({'negatif':negatif}, {'positif':positif})
    if not hasil:   
        bulan = 'Data tidak ada'
        return render_template('index.html', bulan=bulan)       
    else:
        # path_all = r'static/chart_record/chart_all//'
        # img_all = listToString(os.listdir(path_all))
        # img_all = 'static/chart_record/chart_all/' + img_all
        bulan='2024'
        data_positif=[]
        data_negatif=[]
        for count in positif:
            data_positif.append(count)
        for count in negatif:
            data_negatif.append(count)
        return render_template('index.html',bulan=bulan, hasil=hasil, positif=positif, negatif=negatif, result=response)
    
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    path = r"static/file_upload//"
    for file_name in os.listdir(path):
        # construct full file path
        file = path + file_name
        if os.path.isfile(file):
            os.remove(file)

    path = r"static/chart_record/chart_all//"
    for file_name in os.listdir(path):
        # construct full file path
        file = path + file_name
        if os.path.isfile(file):
            os.remove(file)        

    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    path = r"static/file_upload//"
    sentimen = []
    for file_name in os.listdir(path):
        # construct full file path
        file = path + file_name
        if os.path.isfile(file):
            data_label = pd.read_csv(file, encoding='utf8')
            for index in range(len(data_label)):
                kalimat = data_label.iat[index, 2]
                data = [kalimat] 
                vect = countVect.transform(data).toarray()
                my_prediction = model.predict(vect)
                sentimen.append(my_prediction)
                
            data_label['Sentimen'] = np.array(sentimen)
            path_label = r"static/file_labelled//"
            data_label.to_csv(path_label + 'data with label.csv', encoding='utf-8', index=False)

            dframe = pd.read_csv(path_label + r"data with label.csv")
            row = pd.DataFrame(dframe)
            # row.append(dframe)
            count_row = dframe.shape[0]
            for x in range(0, count_row):
                col = row.iloc[x]
                tweet = emoji.replace_emoji(col[2], replace='')
                id = 0
                con = mysql.get_db().cursor()
                con.execute('''INSERT INTO tweet (id, date, tweet, labelling) VALUES (%s,%s,%s,%s)''',
                            (id, datetime.now(), tweet, col[3]))
                mysql.get_db().commit()
                con.close()
    
    return redirect(url_for('home'))

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        Reviews = request.form['Reviews']
        data = [Reviews]
        vect = countVect.transform(data).toarray()
        my_prediction = model.predict(vect)
        con = mysql.get_db().cursor()
        query = ("SELECT labelling FROM tweet");
        con.execute(query)
        hasil = con.fetchall()
        id=0
        con_2 = mysql.get_db().cursor()
        con_2.execute('''INSERT INTO prediksi (id, kalimat, labelling) VALUES (%s,%s,%s)''',
                            (id, Reviews, my_prediction[0]))
        mysql.get_db().commit()
        con_2.close()
        if not hasil:
            bulan = 'Data tidak ada'
            return render_template('nb.html', Reviews=Reviews, prediction=my_prediction[0], bulan=bulan) 
        else:
            # path_all = r'static/chart_record/chart_all//'
            # img_all = listToString(os.listdir(path_all))
            # img_all = 'static/chart_record/chart_all/' + img_all
            bulan='2024'
            return render_template('nb.html', Reviews=Reviews, prediction=my_prediction[0],bulan=bulan) 
    return redirect(url_for('predict')) 
       

@app.route('/labelling')
def labelling():
    return render_template('upload_labelling.html')

@app.route('/report', methods=['POST'])
def report():
    path = r"static/file_upload//"
    for file_name in os.listdir(path):
        # construct full file path
        file = path + file_name
        if os.path.isfile(file):
            os.remove(file)

    path = r"static/chart_record//"
    for file_name in os.listdir(path):
        # construct full file path
        file = path + file_name
        if os.path.isfile(file):
            os.remove(file)               

    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    path = r"static/file_upload//"
    sentimen = []
    for file_name in os.listdir(path):
        # construct full file path
        file = path + file_name
        if os.path.isfile(file):
            data_label = pd.read_csv(file, encoding='utf8')
            data_label.drop('Unnamed: 0', inplace=True, axis=1)
            data_label.drop('Date', inplace=True, axis=1)
            for index in range(len(data_label)):
                kalimat = data_label.iat[index, 0]
                data = [kalimat]
            
                vect = countVect.transform(data).toarray()
                my_prediction = model.predict(vect)
                sentimen.append(my_prediction)

            data_label['Sentimen'] = np.array(sentimen)
            # print(data_label['Sentimen'])
            positif = np.count_nonzero(data_label['Sentimen'] == 'Positif')
            negatif = np.count_nonzero(data_label['Sentimen'] == 'negatif')
            
            path_label = r"static/file_labelled//"
            data_label.to_csv(path_label + 'data with label.csv', encoding='utf-8', index=False)
            dframe = pd.read_csv(path_label + r"data with label.csv")
            
            
    path = r'static/chart_record//'
    img = listToString(os.listdir(path))
    img = 'static/chart_record/' + img
    with open("static/file_labelled/data with label.csv", encoding='UTF-8') as file:
        table = csv.reader(file)
        header = next(table)
        return render_template('hasil_labelling.html',csv=table, header=header,img=img, negatif=negatif, positif=positif)
    
@app.route('/get-data', methods=['POST', 'GET'])
def getData():
    bulan=request.form.get('bulan')
    tahun=request.form.get('tahun')
    con_hasil = mysql.get_db().cursor()
    con_positif = mysql.get_db().cursor()
    con_negatif = mysql.get_db().cursor()
    print(tahun)
    if(bulan=='all'):
        query = ("SELECT case when helper.month = 1 then 'Januari' when helper.month = 2 then 'Februari' when helper.month = 3 then 'Maret' when helper.month = 4 then 'April' when helper.month = 5 then 'Mei' when helper.month = 6 then 'Juni' when helper.month = 7 then 'Juli' when helper.month = 8 then 'Agustus' when helper.month = 9 then 'September' when helper.month = 10 then 'Oktober' when helper.month = 11 then 'November' when helper.month = 12 then 'Desember' end as month, count(tweet.labelling) as count FROM tweet inner join (SELECT id,month(date) as month,year(date) as year FROM tweet) as helper on helper.id = tweet.id where helper.year ='" +tahun+ "'GROUP by helper.month order by helper.month")
        query_positif = ("SELECT case when helper.month = 1 then 'Januari' when helper.month = 2 then 'Februari' when helper.month = 3 then 'Maret' when helper.month = 4 then 'April' when helper.month = 5 then 'Mei' when helper.month = 6 then 'Juni' when helper.month = 7 then 'Juli' when helper.month = 8 then 'Agustus' when helper.month = 9 then 'September' when helper.month = 10 then 'Oktober' when helper.month = 11 then 'November' when helper.month = 12 then 'Desember' end as month, count(tweet.labelling) as count FROM tweet inner join (SELECT id,month(date) as month,year(date) as year FROM tweet) as helper on helper.id = tweet.id where labelling='Positif' and helper.year ='" +tahun+ "'GROUP by helper.month order by helper.month")
        query_negatif = ("SELECT case when helper.month = 1 then 'Januari' when helper.month = 2 then 'Februari' when helper.month = 3 then 'Maret' when helper.month = 4 then 'April' when helper.month = 5 then 'Mei' when helper.month = 6 then 'Juni' when helper.month = 7 then 'Juli' when helper.month = 8 then 'Agustus' when helper.month = 9 then 'September' when helper.month = 10 then 'Oktober' when helper.month = 11 then 'November' when helper.month = 12 then 'Desember' end as month, count(tweet.labelling) as count FROM tweet inner join (SELECT id,month(date) as month,year(date) as year FROM tweet) as helper on helper.id = tweet.id where labelling='negatif' and helper.year ='" +tahun+ "'GROUP by helper.month order by helper.month")
        con_hasil.execute(query)
        con_positif.execute(query_positif)
        con_negatif.execute(query_negatif)
        month = con_hasil.fetchall()
        positif = con_positif.fetchall()
        negatif = con_negatif.fetchall()
        response = {'negatif':negatif}, {'positif':positif}, {'month':month}
        return jsonify(response)

    else:
        query = ("SELECT count(labelling) as count FROM tweet where month(date) =" + bulan + " and year(date) = " + tahun + " group by labelling")
        con_hasil.execute(query)
        hasil = con_hasil.fetchall()
        return (hasil)
    
@app.route('/data-table')
def dataTable():
    bulan=request.args.get('bulan')
    tahun=request.args.get('tahun')
    con = mysql.get_db().cursor()
           
    if(bulan=='all'):
        query = ("SELECT * FROM tweet where year(date) = " + tahun)
        con.execute(query)
        hasil = con.fetchall()
        response = {'data':hasil}
        return (response)

    else:
        query = ("SELECT * FROM tweet where month(date) =" + bulan + " and year(date) = " + tahun)
        con.execute(query)
        hasil = con.fetchall()
        response = {'data':hasil}
        return (response)

@app.route('/data-prediksi')
def dataPrediksi():
    con = mysql.get_db().cursor()
    query = ("SELECT * FROM prediksi")       
    con.execute(query)
    hasil = con.fetchall()
    response = {'data':hasil}
    return (response)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)

