#!/usr/bin/env python
# coding: utf-8

# ## Flask itself will not run in Jupyternotebook file formats, this is only note taking purposes. 
# 
# ## All testing should be completed in applications that are in the traditional .py file format

# In[1]:


from flask import Flask


# ## Initial Setup
# 
# To setup begin by calling call an instance of the Flask Class: __"Flask(args)"__
# 
# The first argument in the flask class is the module or package which flask will use to look up resources (static files, templates, etc.)
# 
# __"\_\_name\_\_"__ is generally the most common arg for general built-in library flask setup<br> 
# __Note:__ If you wanted to generate one from scratch you can build one independently, then call it in place of the __"\_\_name\_\_"__ library

# In[1]:


app = Flask(__name__)
#double underscore "name" is just the name of the module


# ## Decorators
# * Decorators serve to allow flexibility and code readiability/clarity to the code (sort of like bootstrapping or creating shortcuts), 
# * Normally signified by the "@" symbol
# 
# route decorator: __@app.route__
# * Function: Route will trigger what webpage flask will bring up
# 

# In[3]:


#@app.route("/") # "/" represents the routepage/homepage of our website
#def hello_world():
    #return "<p>Hello, World!</p>"


# ## Running Application
# 
# To run the application, use the flask command or python -m flask inputted into command line: __flask --app "name" run__ 
# 
# __Command Input:__
# $ flask --app hello run
# 
# __Command Output:__
#  * Serving Flask app 'hello'
#  * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
# 
# 

# ## Debug mode
# Debugmode is critical for initial web development because it allows changes in the code to be applied in realtime to the webpage
# 
# __Command Input:__ <br>
# flask --app "name" run --debug
#  
# __Command Output:__ 
#  * Serving Flask app 'hello'
#  * Debug mode: on
#  * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: nnn-nnn-nnn

# # Creating a different page
# creation of a differnt page simly takes and defines the route decorator and the function to create a new page

# In[ ]:


#example

@app.route("/about") # "/" represents the routepage/homepage of our website
def about():
    return "<p>Nothing to see here!???</p>"


# # alternate routes into the same function
# Alternate routes are possible with the same function (webpage)
# To do this simply type in a secondary decorator with the appropriate name under the original decorator

# In[ ]:


#example

@app.route("/") # "/" represents the routepage/homepage of our website
@app.route("/home") #designated as a secondary route if url is /home is entered
def hello_world():
    return "<p>Hello, World!</p>"

