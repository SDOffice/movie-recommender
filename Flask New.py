#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template
from flask import Flask, jsonify, request
from flask_cors import CORS
from App import Recommender
import pickle


# In[2]:


with open('movie.pkl', 'rb') as handle:
    model = pickle.load(handle)


# In[5]:


app = Flask(__name__)
CORS(app)
@app.route("/recommend/", methods=['GET'])
def recommend():
    title = request.args.get('title')
    result = model.get_recommendation(title)
    return render_template('data.html', result=result)

@app.route("/",methods=['GET'])
def default():
    return render_template('index.html')


if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=False)


# In[ ]:





# In[ ]:




