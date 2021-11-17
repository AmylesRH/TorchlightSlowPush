from flask import Flask, render_template
import mysql.connector
app = Flask(__name__)


def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host="127.0.0.1",
                                       user="userBO1",
                                       password="hmsgWMNPMxggQLh4",
                                       database="ccsdataplatformdb",
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()

select_product = """
 SELECT *
 FROM WebBehavior
 ORDER BY findability DESC
 """
with connection.cursor() as cursor:
     cursor.execute(select_all)
     for row in cursor.fetchall():
         print(row)

@app.route('/')
def main():
    """Entry point; the view for the main page"""
    return render_template('main.html')


@app.route("/productview/")
def productview():
    """The view for the Product Views page"""
    return render_template('productview.html')


@app.route("/contenttype/")
def contenttype():
    """The view for the Content Type page"""
    return render_template('contenttype.html')


@app.route("/pageview/")
def pageview():
    """The view for the Page Views page"""
    return render_template('pageview.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
