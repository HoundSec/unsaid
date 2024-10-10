from flask import Flask, render_template, request, redirect, url_for
from dbm import DB  

app = Flask(__name__)

# Initialize the database manager
db = DB()

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/messages', methods=['POST'])
def messages():
    name = request.form['name']
    try:
        messages = db.collection.find({'name': name})
        return render_template('messages.html', messages=messages)
    except Exception as e:
        return str(e)

@app.route('/submit', methods=['GET', 'POST'])
def submit_message():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        try:
            result = db.submit_message(name, message)
            return redirect(url_for('home'))
        except Exception as e:
            return str(e)
    return render_template('submit.html')

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
