from flask import Flask, render_template
app = Flask(__name__)

content = [
    {
        'Header' : 'Test 1',
        'Paragraph' : ['Test Paragraph'],
        'List_Items' : []
    },
{
        'Header' : 'Header',
        'Paragraph' : ['Paragraph'],
        'List_Items' : [{'Title' : 'List Title',
                        'li' : ['List Item','List Item']},]
    },
]

key_terms = [{
    'Term' : 'Forecasting',
    'Definition' : 'Techniques consist of a sequence of steps that will lead to an optimal solution to problems, in cases where a solution exists, given restrictions or limitations.'
},
{'Term' : 'Mean Average Deviation',
'Definition' : 'Test!'
},
{'Term' : 'Mean Average Deviation',
'Definition' : 'Test!'
},
]


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
    return render_template('lesson_base.html', all_content=content, terms = key_terms)

@app.route('/forecasting')
def forecasting():
    return render_template('forecasting.html', all_content=content, terms = key_terms)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)