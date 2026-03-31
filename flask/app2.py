from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/contact', methods = ['POST'])
def contact():
    Name = request.form.get('Name')
    Email = request.form.get('Email')
    Message = request.form.get('Message')

    print(Name,Email,Message)
    with open('data.txt', 'a') as f:
        f.write(f'{Name},{Email},{Message}\n')
    return 'Thank you for contacting us'



app.run(host = '0.0.0.0', port = 5000,debug=True)