from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root' 
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_PORT'] = 3307  
app.config['MYSQL_DB'] = 'Nemo'

mysql = MySQL(app)

@app.route("/")
def home():
    return {"data":"homepage"}

@app.route("/<user>/<id>/")
def single_search(user,id):
    query = single_query(user,id)
    if query:
        return {"data": query}
    return {"data": 404}
    
def single_query(group,input):
    current = mysql.connection.cursor()
    if group == "instructors":
        if input == "all":
            query_string = "select * from instructors;"
        else:
            try:
                int(input)
                query_string = f"select * from instructors where instructorid = {input};"
            except ValueError:
                return False
    elif group == "users":
        if input == "all":
            query_string = "select * from users;"
        else:
            try:
                int(input)
                query_string = f"select * from users where userid = {input};"
            except ValueError:
                return False
    elif group == "courses":
        if input == "all":
            query_string = f"select * from courses;"
        else:
            try:
                int(input)
                query_string = f"select * from courses where courseid = {input};"
            except ValueError:
                return False
    elif group == "instructorcourses":
        if input == "all":
            query_string = "select courses.coursename, instructors.instructorname from courses join instructors using (instructorid);"
        else:
            try:
                int(input)
                query_string = f"select instructors.instructorname, courses.coursename from courses join instructors using (instructorid) where instructors.instructorid = {input};"
            except ValueError:
                return False
    elif group == "usercourses":
        if input == "all":
            query_string = "select users.username, courses.coursename from users join userstocourses on users.userid = userstocourses.userid join courses on userstocourses.courseid = courses.courseid;"
        else:
            try:
                int(input)
                query_string = f"select users.username, courses.coursename from users join userstocourses on users.userid = userstocourses.userid join courses on userstocourses.courseid = courses.courseid where users.userid = {input};"
            except ValueError:
                return False
    else:
        return False
    
    current.execute(query_string)
    fetch_data = current.fetchall()

    return fetch_data
    
    
if __name__ == "__main__":
    app.run()