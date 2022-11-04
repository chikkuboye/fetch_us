import requests
import sys
import mysql.connector
import json

try:
    mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'userdb')
except mysql.connector.Error as e:
    sys.exit(e)

mycursor = mydb.cursor()

data = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population").text

data_info = json.loads(data)

for i in data_info["data"]:
    year = str(i["ID Year"])
    population = str(i['Population'])
    sql = "INSERT INTO `us_public`(`ID Nation`, `Nation`, `ID Year`, `Population`, `Slug Nation`) VALUES ('"+i['ID Nation']+"','"+i['Nation']+"','"+year+"','"+population+"','"+i['Slug Nation']+"')"
    mycursor.execute(sql)
    mydb.commit()
    print('Inserted the value succesfully')