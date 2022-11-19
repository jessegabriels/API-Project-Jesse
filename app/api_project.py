from fastapi import FastAPI
#import mysql.connector

app = FastAPI()
meetinglist = [[1,14.92], [2, 25.45], [3, 18.26], [4, 18.72], [5, 19.11], [6, 19.02], [7, 38.85], [8, 39.78]]
lengteList = len(meetinglist)

#mydb = mysql.connector.connect(
  #host="localhost",
  #user="root",
  #password="gabriels.klas4B",
  #database="api_iot",
  #auth_plugin='mysql_native_password'
#)

#mycursor = mydb.cursor()


@app.get("/meeting")
def root():
    #mycursor.execute("SELECT * FROM waterput WHERE meeting_id = '10'")
    #myresult = mycursor.fetchall()

    #for x in myresult:

    for x in meetinglist:
        return {"meeting": x[0], "diepte": x[1]}


@app.get("/meeting/day")
def root():
    #mycursor.execute("Select * FROM waterput ORDER BY meeting_id DESC LIMIT 4")
    #myresult = mycursor.fetchall()
    list = {}
    for x in meetinglist[-4:]:
      list[x[0]] = x[1]
      
    return list


@app.get("/meeting/week")
def root():
  #mycursor.execute("Select * FROM waterput ORDER BY meeting_id DESC LIMIT 28")
  #myresult = mycursor.fetchall()
  list = {}
  for x in meetinglist:
    list[x[0]] = x[1]
      
  return list 