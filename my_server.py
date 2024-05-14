from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request

#Khởi tạo  Falsk Sever Backend
app = Flask(__name__)

#Apply Flask CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/add',methods=['POST','GET'])
@cross_origin(origins='*')
def add_process():
    a = int(request.args.get('sothunhat'))
    b = int(request.args.get('sothuhai'))
    sum = a+b
    return 'Kết quả là:'+str(sum)
@app.route('/minus',methods=['POST','GET'])
@cross_origin(origins='*')
def minus_process():
    return "Hàm trừ"
@app.route('/multi',methods=['POST','GET'])
@cross_origin(origins='*')
def multi_process():
    return "Hàm nhân"
@app.route('/div',methods=['POST','GET'])
@cross_origin(origins='*')
def div_process():
    return "Hàm chia"
#Start Backend
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='9999')