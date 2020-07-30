from flask import Flask, render_template,Markup
app = Flask(__name__)
app._static_folder = '/Users/hervinsagnep/Desktop/DS_Application/static'
import test_db

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/operations_management')
def operations_management():
    return render_template('operations_management.html')

@app.route('/linear_programming')
def linear_programming():
    return render_template('linear_programming.html')

@app.route('/capacity_planning_decision')
def capacity_planning():
    return render_template('capacity_planning_decision.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz_template.html')

@app.route('/test_grounds')
def test_grounds():
    return render_template('lesson_base.html', all_content=test_db.content, terms = test_db.key_terms)

@app.route('/forecasting')
def forecasting():
    return render_template('forecasting.html', all_content=test_db.FC_Content, terms = test_db.FC_Key_Terms)

@app.route('/inventory_management')
def inventory_management():
    return render_template('inventory_management.html', all_content=test_db.IM_Content, terms = test_db.IM_Key_Terms)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)