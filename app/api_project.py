from fastapi import FastAPI
#import mysql.connector
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
meetinglist = [[1,14.92], [2, 25.45], [3, 18.26], [4, 18.72], [5, 19.11], [6, 19.02], [7, 38.85], [8, 39.78]]
lengteList = len(meetinglist)

#mydb = mysql.connector.connect(
  #host="localhost",
  #user="root",
  #password="password",
  #database="api_iot",
  #auth_plugin='mysql_native_password'
#)

#mycursor = mydb.cursor()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost.tiangolo.com",
    "http://127.0.0.1:5500",
    "http://localhost:63342",
    "https://jessegabriels.github.io"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/meeting")
def root():
    #mycursor.execute("SELECT * FROM waterput WHERE")
    #myresult = mycursor.fetchall()

    #for x in myresult:
    list = {}

    for x in meetinglist:
      list[x[0]] = x[1]
    return list


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