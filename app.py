import os
from flask import Flask, render_template, request
import DGS
import random
import StringIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
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
    resolution =request.form['resolution']
    density = request.form['density']
    dofilter=request.form['dofilter']
    maxscale=request.form['maxscale']
    notes=request.form['notes']
    ans =  DGS.dgs(image, density, resolution, dofilter, maxscale, notes,1)
    print ans
    means=ans['mean grain size']
    kuto = ans['grain size kurtosis']
    stdev = ans['grain size skewness']
    
    
    y=ans['grain size frequencies']
    x=ans['grain size bins']
    for num in range(len(y)):
        y[num] *= 100
    

    

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(x,y,align='center',width=20)
    fig.savefig('./static/test.png')
    bar_chart= './static/test.png'
    
    return render_template('output.html',means=means,image=image,stdev=stdev,kuto=kuto,bar_chart=bar_chart)
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))