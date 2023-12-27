from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    assistant_reply = eva.generate_answer(user_input)
    return render_template('index.html', user_input=user_input, assistant_reply=assistant_reply)
