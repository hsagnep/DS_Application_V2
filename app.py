from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/operations_management')
def operations_management():
    return render_template('operations_management.html')

@app.route('/linear_programming')
def linear_programming():
    return render_template('linear_programming.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz_template.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)