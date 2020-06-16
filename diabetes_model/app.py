# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 22:14:52 2020

@author: sushant
"""

import flask
import pickle as pkl
import pandas as pd
import os

f=open(f'model/model2.pkl','rb')
models=pkl.load(f)
app=flask.Flask(__name__,template_folder='templates')
@app.route('/',methods=['GET','POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
        pregnant=flask.request.form['pregnant']
        glucose=flask.request.form['glucose']
        bp=flask.request.form['bp']
        skin=flask.request.form['skin']
        insulin=flask.request.form['insulin']
        bmi=flask.request.form['bmi']
        pedigree=flask.request.form['pedigree']
        age=flask.request.form['age']
        
        input_variable=pd.DataFrame([[pregnant,glucose,bp,skin,insulin,bmi,pedigree,age]])

        prediction =models.predict(input_variable)
        print(prediction)
        global results
        if(prediction == 1):
            results='Test Positive'
        else:
            results='Test Negative '
        return flask.render_template('main.html',result=results)


if __name__ == '__main__':
    
    app.run(port=8050)