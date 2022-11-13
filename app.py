from flask import *
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
plotly.offline.init_notebook_mode (connected = True)
import matplotlib.pyplot as plt
import warnings
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.decomposition import PCA
import os
import json
app = Flask(__name__)

def create_pca_label(X, y, n_components=None):
    if (n_components != None):
        pca = PCA(n_components)
    else:
        pca = PCA()
    trans = pca.fit_transform(X)
    trans = pd.DataFrame(trans)
    trans['species'] = y
    return pca, trans

def create_pca(X, n_components=None):
    if (n_components != None):
        pca = PCA(n_components)
    else:
        pca = PCA()
    trans = pca.fit_transform(X)
    trans = pd.DataFrame(trans)
    return pca, trans

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict",methods=['POST','GET'])
def predict():
    try:
        if request.method == 'POST':
            header = int(request.form.get('q1'))  # 0 for No, 1 for Yes
            label = int(request.form.get('q2')) # 0 for No, 1 for Yes
            visualization=int(request.form.get('q3')) # 0 for No, 1 for Yes
            apply = int(request.form.get('q4')) # 0 for none, 1 for standardization, 2 for normalization
            components = request.form.get('q5') # get number input from use
            if components.isdigit():
                components=int(components)
            else:
                components=0
            file = request.files['file']
            file.save(file.filename)
            if header==1:
                df = pd.read_csv(file.filename)
            else:
                df = pd.read_csv(file.filename,header=None)
            
            if label==1:
                labeled=df[df.columns[-1]]
                df=df.drop([df.columns[-1]],axis=1)

            warnings.filterwarnings("ignore")
            feats = df.columns[:] # getting the header names
            if apply==1:
                scaler = StandardScaler().fit_transform(df[feats])
            elif apply==2:
                scaler = preprocessing.normalize(df[feats])
            else:
                scaler = df[feats]     

            scaled = pd.DataFrame(scaler, columns=feats)
            if label==1:
                scaled['Label'] = labeled 

            #before applying PCA Visualization #Shivesh add this as title
            if label==1 and visualization==1 and len(feats)>=components:
                features = feats
                fig = px.scatter_matrix(
                    scaled,
                    dimensions=features,
                    color="Label"
                )
                fig.update_traces(diagonal_visible=True)
                graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
                print("graph working")
                

            if label==1:
                X, y = scaled.drop(['Label'], axis=1), scaled['Label']

                if len(feats)>=components:
                    if components == 0:
                        components=None
                    pca1, trans1 = create_pca_label(X=X, y=y, n_components=components)
                    print(pca1.explained_variance_ratio_)#mention what it is : Shivesh
                    print(pca1.components_)# mention this to!
                else:
                    print("No of Components entered is greater than number of input features.")
            else:
                X = scaled

                if len(feats)>=components:
                    if components == 0:
                        components=None
                    pca1, trans1 = create_pca(X=X, n_components=components)
                    print(pca1.explained_variance_ratio_)#mention what it is : Shivesh
                    print(pca1.components_)# mention this to!

            #After PCA
            if label==1 and visualization==1 and len(feats)>=components:

                pca = PCA()
                components = pca.fit_transform(df[features])
                labels = {
                    str(i): f"PC {i+1} ({var:.1f}%)"
                    for i, var in enumerate(pca.explained_variance_ratio_ * 100)
                }
                fig = px.scatter_matrix(
                components,
                labels=labels,
                dimensions=range(len(features)),
                color=scaled["Label"]
                )
                fig.update_traces(diagonal_visible=True)
                graphJSON2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

            os.remove(file.filename)

            return render_template('index.html',graphJSON1=graphJSON1,graphJSON2=graphJSON2,output1=str(pca1.explained_variance_ratio_),output2=str(pca1.components_))

    except:
        return render_template('index.html',output1="Something went wrong! Plz choose the following carefully according to your dataset!")

                                                                                                                            

if __name__ == '__main__':
    app.run(debug=True)