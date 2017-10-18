import os
from flask import Flask, render_template, request
import DGS

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
    file.save(f)
    image='./static/'+file.filename
    print image
    resolution = 1
    density = 10
    dofilter=1
    maxscale=8
    notes=8
    ans =  DGS.dgs(image, density, resolution, dofilter, maxscale, notes,1)
    print ans
    means=ans['mean grain size']
    kuto = ans['grain size kurtosis']
    stdev = ans['grain size skewness']
    return render_template('output.html',means=means,image=image,stdev=stdev,kuto=kuto)