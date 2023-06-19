from flask import Flask, render_template,request, flash, redirect, url_for
from predict_pipeline import load_object, preprocess, predict_single_image, INPUT_SHAPE
from werkzeug.utils import secure_filename
import urllib.request
import os

app = Flask(__name__)

app.secret_key = "lungcancer"
CATEGORIES = ["adenocarcinoma", "largecellcarcinoma", "squamouscellcarcinoma", "normal"]#categories of carcinoma
INPUT_SHAPE = (250, 250, 3) #input shape that we used for training a model
ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','gif'])

def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])

def hello_world():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def predict():
        
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    
    if file.filename == '':
        flash('No image select for uploading')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join("static/uploads/",filename))
        image_path = "static/uploads/" + file.filename
        
        image = image_path
        model = load_object("Artifacts", "effnetb4_50epochs.h5")
        predicted_class = predict_single_image(image, model)
        
        flash('Image sucessfuly uploaded and displayed below')
        return render_template('home.html',filename=filename, prediction=predicted_class)
    
    else:
        flash('Allowed image types are - png, jpg, jped, gif')
        return redirect(request.url)    
    
@app.route('/display/<filename>')
def display_image(filename):
        #print("display_image filename: " + filename) 
    return redirect(url_for('static',filename='uploads/' + filename), code=301) 
        
if __name__=='__main__':
    app.run(port=3000, debug=True)