from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def disp():
    a = open("a.txt")#reading dustbin status
    a = a.read()
    a = a.strip()
    if(a == 'a'):#2 filled 
        b = open('2reds.html')
    else:#2 empty
        b = open('2greens.html')
    b = b.read()
    return b
app.run(host = '192.168.43.42', port = 8000, debug = True, use_reloader=True)


