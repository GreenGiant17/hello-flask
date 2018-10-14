from flask import Flask, request  #request allows you to grab the info @ /hello

app = Flask(__name__)
app.config['DEBUG'] = True  #as you make changes this reloads the app based on those changes so you dont have to stop and restart flask operation

#<form action="/hello"> contains the request type. request type is unspecified so it will be a GET request. GET and POST can be get or post. it doesn't matter
#action="/hello" submits the request to this specific appended URL
#POST requests submit as part of the body so the data is not exposed as part of the URL
form = """
<!doctype html>
<html>
   <body>
       <form action="/hello" method="post">
           <label form="first-name">First Name:</label>           
           <input id="first-name" type="text" name="first_name"/>
           <input type="submit"/> 
       </form>
   </body>
</html>
"""

@app.route("/")  #this function receives requests at that path. in this case is the root path
def index():     #it will send the request to this function
   return form

@app.route ("/hello", methods=['POST'])  # can also be ['GET', 'POST']
def hello ():
   first_name = request.form["first_name"]  #request.args.get is used to grab info from a GET request at the /hello path and assign to variable first_name 
   return '<h1>Hello, ' + first_name + '</h1>'  #request.form is used to grab info from a POST request at the /hello path.
app.run()