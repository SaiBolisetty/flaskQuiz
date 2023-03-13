from flask import Flask, render_template, request, redirect
import pymssql

app = Flask(__name__)

# Change the connection settings as per your database configuration
connection = pymssql.connect(server='DESKTOP-HME0A24', user='Venkat', password='Password@123', database='VENKAT')

@app.route('/')
def index():
    with connection.cursor(as_dict=True) as cursor:
        cursor.execute('SELECT * FROM questions')
        questions = cursor.fetchall()
    return render_template('index.html', questions=questions)

@app.route('/add_question', methods=['POST'])
def add_question():
    text = request.form['question_text']
    option1 = request.form['option1']
    option2 = request.form['option2']
    option3 = request.form['option3']
    option4 = request.form['option4']
    answer = request.form['answer']
    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO questions (question, option1, option2, option3, option4, answer) VALUES (%s, %s, %s, %s, %s, %s)',
                       (text, option1, option2, option3, option4, answer))
        connection.commit()
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)
