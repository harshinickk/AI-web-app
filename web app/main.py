import flask
import sys
import os
import numpy as np
import pickle
import glob
import re
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from flask import redirect, url_for
from werkzeug.utils import secure_filename

from tensorflow.keras.preprocessing import image
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.2
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)


# app = Flask(__name__) # to make the app run without any
app = Flask(__name__)
app.config["DEBUG"] = True
pumpmodel = pickle.load(open('pumppredict.pkl', 'rb'))
drynessmodel = pickle.load(open('drynesspredict.pkl', 'rb'))
cyclemodel = pickle.load(open('cyclepredict.pkl', 'rb'))
potatomodel=load_model('potatoinception.h5')
cornmodel=load_model('corninception.h5')
cottonmodel=load_model('cottoninception.h5')
cucumbermodel=load_model('cucumberinception.h5')
ricemodel=load_model('riceinception.h5')
weedmodel=load_model('weedinception.h5')
cmodel = pickle.load(open('Cpredict.pkl', 'rb'))
nmodel = pickle.load(open('Npredict.pkl', 'rb'))
pmodel = pickle.load(open('Ppredict.pkl', 'rb'))
kmodel = pickle.load(open('Kpredict.pkl', 'rb'))

def model_predict(img_path, model):
    print(img_path)
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    ## Scaling
    x=x/255
    x = np.expand_dims(x, axis=0)
   

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
   # x = preprocess_input(x)

    preds = model.predict(x)
    preds=np.argmax(preds, axis=1)
    
    return preds

# main index page route
@app.route('/')
def home():
    return render_template('front.html')

@app.route('/opt',methods=['POST'])
def opt():
    return render_template('home.html')

@app.route('/soilq',methods=['POST'])
def soilq():
    return render_template('soil.html')

@app.route('/waterq',methods=['POST'])
def waterq():
    return render_template('index.html')

@app.route('/irrig',methods=['POST'])
def irrig():
    return render_template('index.html')

@app.route('/cropw',methods=['POST'])
def cropw():
    return render_template('base.html')

@app.route('/croph',methods=['POST'])
def croph():
    return render_template('croplist.html')

@app.route('/corn',methods=['GET','POST'])
def cornupload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        
        # Make prediction
        preds = model_predict(file_path, cornmodel)
        
        if preds==0:
            preds="Blight"
        elif preds==1:
            preds="Common rust"
        elif preds==2:
            preds="Gray leaf spot"
        else:
            preds="Healthy"
        result=preds
        return result
    return None
    
@app.route('/cotton',methods=['GET','POST'])
def cottonupload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        
        # Make prediction
        preds = model_predict(file_path, cottonmodel)
        

        if preds==0:
            preds="The leaf is diseased cotton leaf"
        elif preds==1:
            preds="The leaf is diseased cotton plant"
        elif preds==2:
            preds="The leaf is fresh cotton leaf"
        else:
            preds="The leaf is fresh cotton plant"
        result=preds
        return result
    return None           
 
@app.route('/cucumber',methods=['GET','POST'])
def cucumberupload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        
        # Make prediction
        preds = model_predict(file_path, cucumbermodel)
        

        if preds==0:
                preds="Good"
        else:
                preds="Ill"
        result=preds
        return result
    return None

@app.route('/potato',methods=['GET','POST'])
def potatoupload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        
        # Make prediction
        preds = model_predict(file_path, potatomodel)
        

        if preds==0:
            preds="Early blight"
        elif preds==1:
            preds="Healthy"
        else:
            preds="Late blight"
        result=preds
        return result
    return None

@app.route('/rice',methods=['GET','POST'])
def riceupload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        
        # Make prediction
        preds = model_predict(file_path, ricemodel)
        

        if preds==0:
            preds="Brown spot"
        elif preds==1:
            preds="Healthy"
        elif preds==2:
            preds="Hispa"
        else:
            preds="Leaf blast"
        result=preds
        return result
    return None
            
@app.route('/crophw',methods=['GET','POST'])
def crophw():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        
        # Make prediction
        preds = model_predict(file_path, ricemodel)
        

        if preds==0:
            preds="weed"
        else:
            preds="No Weed"
        result=preds
        return result
    return None

@app.route('/ppredict',methods=['POST'])
def ppredict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    pred = pumpmodel.predict(final_features)
    out = (pred[0])
    if (out==1):
        a="Turn on pump"
        s1="static/pumpon.jpg"
    else:
        a="Turn off pump"
        s1="static/pumpoff.jpg"
    predi='{}'.format(a)
    return render_template('index.html', pprediction=predi,s=s1)


@app.route('/dpredict',methods=['POST'])
def dpredict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    pred = drynessmodel.predict(final_features)
    out = (pred[0])
    if(out=='d'):
        b="The soil is dry"
    elif(out=='m'):
        b="The soil is medium"
    elif(out=='w'):
        b="The soil is wet"
    predi='{}'.format(b)
    return render_template('index.html', dprediction=predi)
         
         
@app.route('/cpredict',methods=['POST'])
def cpredict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    pred = cyclemodel.predict(final_features)
    out = (pred[0])
    c=int((out-9))
    predi='Water needed after {} days'.format(c)
    return render_template('index.html', cprediction=predi)

@app.route('/cp',methods=['POST'])
def cp():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    pred = cmodel.predict(final_features)
    out = (pred[0])
    if (out=='L'):
        a="Low"
    elif(out=='M'):
        a="Medium"
    else:
        a="High"
    predi='{}'.format(a)
    return render_template('soil.html', cprediction=predi)

@app.route('/npr',methods=['POST'])
def npr():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    pred = nmodel.predict(final_features)
    out = (pred[0])
    if (out=='L'):
        a="Low"
    elif(out=='M'):
        a="Medium"
    else:
        a="High"
    predi='{}'.format(a)
    return render_template('soil.html', nprediction=predi)

@app.route('/pp',methods=['POST'])
def pp():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    pred = pmodel.predict(final_features)
    out = (pred[0])
    if (out=='VL'):
        a="Very Low"
    elif(out=='L'):
        a="Low"
    elif(out=='M'):
        a="Medium"
    elif(out=='MH'):
        a="Moderately high"
    elif(out=='H'):
        a="High"
    else:
        a="Very high"
    predi='{}'.format(a)
    return render_template('soil.html', pprediction=predi)

@app.route('/kp',methods=['POST'])
def kp():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    pred = kmodel.predict(final_features)
    out = (pred[0])
    if (out=='VL'):
        a="Very Low"
    elif(out=='L'):
        a="Low"
    elif(out=='M'):
        a="Medium"
    elif(out=='MH'):
        a="Moderately high"
    elif(out=='H'):
        a="High"
    else:
        a="Very high"
    predi='{}'.format(a)
    return render_template('soil.html', kprediction=predi)

if __name__ == '__main__':
    app.run(port=5001,debug=True)