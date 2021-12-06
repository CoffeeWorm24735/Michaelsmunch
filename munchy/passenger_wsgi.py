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

@app.route("/<string:name>/")
def say_hello(name):
    return f"Hello {name}!"
  
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        
        mycursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = mycursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect("www.michaelsmunch.com/charlie")
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)


if __name__ == "__main__":
    app.run(debug=True)