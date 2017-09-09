from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])#get request from nodemcu
def disp():
    k = open("a.txt",'w')
    a = request.url
    a = a.split('%3F')
    for i in range(3):
        a[i] = a[i].split("=")[1]
    print(str(a[0])+' '+str(a[1])+' '+str(a[2])+'\n')
    if int(a[0])<=5:#if space in dustbin is less
        k.write("a")
    else:
        k.write("b")#if space is more
    k.close()
    return "Recieved"
        
app.run(host = '192.168.43.42', port = 5000, debug = True, use_reloader=True)

