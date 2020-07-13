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




if __name__ == "__main__":
    app.run(debug=True)