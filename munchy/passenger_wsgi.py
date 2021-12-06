from flask import Flask, request, jsonify
import mysql.connector
app = Flask(__name__)
application = app # our hosting requires application in passenger_wsgi



mydb = mysql.connector.connect(
  host="localhost",
  user="wqtpatjfrk88",
  password="Brady123!",
  database="Michaels_Munch"
)

@app.route("/hello")
def hello():
    return "This Hello Wold!"

mycursor = mydb.cursor()
print("Online")
@app.route('/api', methods=['GET','POST'])
def api():
    request_json = request.json
    print(request_json.get("UserName")) # should display 'bar'
    print("data is "+format(request_json))
    print(request.content_type)
    print(request.json)
    if request.method == 'POST':
      txtName = request_json.get("UserName")
      txtLocker = request_json.get("Locker") 
      txtYear = request_json.get("Year") 
      txtMangoLoco = request_json.get("MangoLoco") 
      txtUltraWhite = request_json.get("UltraWhite") 
      txtDairyMilk = request_json.get("DairyMilk") 
      txtPipelinePunch = request_json.get("PipelinePunch") 
      txtTotal = request_json.get("TotalDue") 
      txtTime = request_json.get("OrderTime") 
      txtStatus = request_json.get("Status") 
      txtUid = request_json.get("UID")
      print(f"hey {txtYear} {txtLocker} {txtPipelinePunch} {txtUltraWhite} {txtMangoLoco} {txtDairyMilk} {txtName} {txtTotal} {txtTime} {txtStatus} {txtUid}")
      sql = "INSERT INTO OrderBase (Year, Locker, PipelinePunch, UltraWhite, MangoLoco, DairyMilk, UserName, Total, OrderTime, Status, UID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
      val = (txtYear, txtLocker, txtPipelinePunch, txtUltraWhite, txtMangoLoco, txtDairyMilk, txtName, txtTotal, txtTime, txtStatus, txtUid)

      mycursor.execute(sql, val)

      mydb.commit()
      return f"hey {txtYear} {txtLocker} {txtPipelinePunch} {txtUltraWhite} {txtMangoLoco} {txtDairyMilk} {txtName} {txtTotal} {txtTime} {txtStatus} {txtUid}"
     

    else:
        
        return "Fail"


if __name__ == "__main__":
    app.run(debug=True)