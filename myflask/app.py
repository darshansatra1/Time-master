from flask import Flask,render_template,request
from flask_mysqldb import MySQL
from werkzeug.serving import run_simple
from flask import Flask, jsonify
import simplejson as json
import requests
app =Flask(__name__)


app.config['MYSQL_HOST'] ='127.0.0.1'

app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Vibhav031998@'
app.config['MYSQL_DB']='adt'


mysql=MySQL(app)


@app.route('/',methods=["GET","POST"])
def total_leaves():

    #user='vivek'

    cur =mysql.connection.cursor()
    #total_leaves=cur.execute("SELECT (user,sum(leaves) as leave,year) as total_leaves FROM timesheet_timecardpython GROUP BY year HAVING user=(%s) ",(user))

    leave=cur.execute('SELECT sum(timesheet_timecard.leaves),timesheet_employee.name FROM timesheet_timecard INNER JOIN timesheet_employee ON timesheet_timecard.user_id=timesheet_employee.user_id GROUP BY (timesheet_timecard.user_id)')
    print(leave)
    row_headers = [x[0] for x in cur.description]
    leaves = []

    leaves=cur.fetchall()
    print(leaves)
    mysql.connection.commit()
    row_headers = [x[0] for x in cur.description]  # this will extract row headers

    json_data = []
    for result in leaves:
        json_data.append(dict(zip(row_headers, result)))

    return json.dumps(json_data)





    #cur.close()
if __name__=="__main__":
    app.run(debug=True)




