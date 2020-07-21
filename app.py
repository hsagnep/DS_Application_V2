from flask import Flask, render_template
app = Flask(__name__)

content = [
    {
        'Header' : 'Decision Theory',
        'Paragraph' : ['Blah blach','waka taka'],
        'List_Items' : []
    },
{
        'Header' : 'Linear Programming',
        'Paragraph' : ['Waka Waka'],
        'List_Items' : [{'Title' : 'Oppa Gangnam Style',
                        'li' : ['Waluigi','Mario']},]
    },
{
        'Header' : 'Linear Programming Assumptions',
        'Paragraph' : ['Linearity: the impact of decision variables is linear in both constraints and objective function.','Divisibility: non-integer values of decision variables are acceptable.','Certainty: values of parameters are known and constant. (within the scope of the problem)','Non-negativity: negative values of decision variables are not allowed'],
        'List_Items' : []
    },
{
        'Header' : 'Steps of Linear Programming',
        'Paragraph' : [],
        'List_Items' : [{'Title' : '',
                        'li' : ['Model Formulation','Solving the LP','Studying the Results: Output Reports and Sensitivity Analysis']},]
    },
]

key_terms = [{
    'Term' : 'Linear Programming',
    'Definition' : 'Techniques consist of a sequence of steps that will lead to an optimal solution to problems, in cases where a solution exists, given restrictions or limitations.'
},
{'Term' : 'Objective Function',
'Definition' : 'Test!'
}
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



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)