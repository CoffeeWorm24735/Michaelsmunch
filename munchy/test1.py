import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="wqtpatjfrk88",
  password="Brady123!",
  database="Michaels_Munch"
)

mycursor = mydb.cursor()

txtName = "Charlie"
txtLocker = 10
txtYear = "1st Year" 
txtMangoLoco = 2
txtUltraWhite = 5
txtDairyMilk = 6 
txtPipelinePunch = 7
txtTotal = 1.98
txtTime = "11:11"
txtStatus = "Ordered" 
txtUid = 9876545627389

sql = "INSERT INTO OrderBase (Year, Locker, PipelinePunch, UltraWhite, MangoLoco, DairyMilk, UserName, Total, OrderTime, Status, UID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (txtYear, txtLocker, txtPipelinePunch, txtUltraWhite, txtMangoLoco, txtDairyMilk, txtName, txtTotal, txtTime, txtStatus, txtUid)

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
