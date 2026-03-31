from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/next')
def next_page():
    return render_template('nextpage.html')

app.run(host = '0.0.0.0', port = 5000,debug=True)