from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    """Entry point; the view for the main page"""
    return render_template('main.html')

@app.route('/productview')
def productview():
    """The view for the Product Views page"""
    return render_template('productview.html')

@app.route('/contenttype')
def contenttype():
    """The view for the Content Type page"""
    return render_template('contenttype.html')

@app.route('/pageview')
def pageview():
    """The view for the Page Views page"""
    return render_template('pageview.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
