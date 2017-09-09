from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def disp():
    a = request.url
    a = a.split('%3F')
    for i in range(3):
        a[i] = a[i].split("=")[1]
    print(str(a[0])+' '+str(a[1])+' '+str(a[2])+'\n')
    return "Recieved"
        
app.run(host = '192.168.43.42', port = '8000', debug = False)
