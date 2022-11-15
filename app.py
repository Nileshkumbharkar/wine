from flask import Flask,request,render_template
from utils import Wine
# from utils import Wine
import pickle
import os


app =  Flask(__name__)

@app.route('/')
def new():
    print('hello')
    return render_template('user.html')

@app.route('/predict_wine',methods = ['POST'])
def submit():
    alcohol = float(request.form.get('alcohol'))
    malic_acid=float(request.form.get('malic_acid')) 
    ash=float(request.form.get('ash'))
    alcalinity_of_ash=float(request.form.get('alcalinity_of_ash'))
    magnesium=float(request.form.get('magnesium')) 
    total_phenols=float(request.form.get('total_phenols')) 
    flavanoids=float(request.form.get('flavanoids')) 
    nonflavanoid_phenols=float(request.form.get('nonflavanoid_phenols')) 
    proanthocyanins=float(request.form.get('proanthocyanins'))
    color_intensity=float(request.form.get('color_intensity')) 
    hue=float(request.form.get('hue')) 
    diluted_wines=float(request.form.get('diluted_wines')) 
    proline=float(request.form.get('proline')) 
  
    wine = Wine(alcohol,malic_acid,ash,alcalinity_of_ash,magnesium,total_phenols,flavanoids,nonflavanoid_phenols,proanthocyanins,color_intensity,hue,diluted_wines,proline)
    S = wine.get_predict()

    return '''<html>
    <head></head>
    <center>
    <body style="background-color:rgb(204, 128, 141);">
    <p style="font-size:50px ; ">
    
        <label>Wine_Prediction: %(S)s </label>
        <br>            
    </body>
    </center>
</html>
''' % locals()

if __name__ == '__main__':
    app.run(debug=True)
