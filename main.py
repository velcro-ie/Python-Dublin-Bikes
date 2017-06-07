from flask import Flask
from flask import Flask, render_template
from flask import request, redirect
import sqlite3
from accessDB import GetData

app = Flask(__name__)

def create_db():
    ''' creates the .db file from the sql file. 
    
    Reads each line of the sql file and executes the commands to create a .db'''
    con = sqlite3.connect('bikes.db')
    c = con.cursor()

#change the path according to where the sql file is located
    fd = open('C:/Users/veldi_000/git/dublinbikes/static/dump.sql', 'r')
    sql = fd.readlines()
    fd.close()
    
    sql = [(n.strip()) for n in sql]
    
    for x in sql:
        try:
            c.execute(x)
        except OperationalError as e:
            print (e)
            print ("Command skipped: ", x) 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    con.commit()
    con.close()
    return

@app.route('/')
def homepage():
    return render_template("home.html")
    
@app.route('/time', methods = ['POST'])
def query():
    day = request.form.get('day')
    time = request.form.get('time')
    arr = GetData(day, time)
    return render_template("markers.html", arr=arr)

create_db()

if __name__ == "__main__":
    app.run(debug=True)

    
    
    