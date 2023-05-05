from fastapi import FastAPI
import uvicorn
app=FastAPI()
@app.get('/hello')
def hello():
    str="hello world"
    return str
if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=1008)
