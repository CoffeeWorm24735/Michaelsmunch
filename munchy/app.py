import os
import mysql.connector
from flask import Flask, request, render_template, redirect, url_for, jsonify

project_root = os.path.dirname(os.path.realpath('__file__'))
app = Flask(__name__)


mydb = mysql.connector.connect(
  host="localhost",
  user="wqtpatjfrk88",
  password="Brady123!",
  database="Michaels_Munch"
)

mycursor = mydb.cursor()
print("Online")
# @app.route('/api', methods=['POST'])
# def api():
#     # content = request.json
#     # print(content['mytext'])
    
#     print(content['Name']) # should display 'bar'
    
#     if request.method == 'POST':
#       txtName = content['Name'] 
#       txtLocker = content['Locker'] 
#       txtYear = content['Year'] 
#       txtMangoLoco = content['MangoLoco'] 
#       txtUltraWhite = content['UltraWhite'] 
#       txtDairyMilk = content['DairyMilk'] 
#       txtPipelinePunch = content['PipelinePunch'] 
#       txtTotal = content['Total'] 
#       txtTime = content['Time'] 
#       txtStatus = content['Status'] 
#       txtUid = content['Uid']

#       sql = "INSERT INTO OrderBase (Year, Locker, Pipeline Punch, Ultra White, Mangog Loco, Dairy Milk, Username, Total, OrderTime, OrderStaus, UID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#       val = (txtYear, txtLocker, txtPipelinePunch, txtUltraWhite, txtMangoLoco, txtDairyMilk, txtName, txtTotal, txtTime, txtStatus, txtUid)

#       mycursor.execute(sql, val)

#     else:
        
#         return "Fail"

@app.route("/<string:name>/")
def say_hello(name):
    return f"Hello {name}!"

application = app
app.run()