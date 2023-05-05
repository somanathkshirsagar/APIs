from fastapi import FastAPI
from flask import request,Flask,render_template
import uvicorn

app = Flask(__name__)
#app = FastAPI()

@app.route("/",methods=['GET'])
def Home():
    return render_template("Home.html")
@app.route("/predict",methods=['POST'])
def predict():
    name = str(request.form['name'])
    age = int(request.form['age'])

    if(age>18):
        return "You Are Eligible...!!"
    else:
        return "You Are Not Eligible"

if __name__ == '__main__':
    #uvicorn.run(app,host='127.0.0.1',port=1000)
    app.run(host='127.0.0.1',port=1000)