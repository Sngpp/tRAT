from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'Rome', 'Madrid', 'Berlin'],
        'answer_index': 0,
    },
    {
        'question': 'What is the largest country in the world?',
        'options': ['Russia', 'China', 'United States', 'Canada'],
        'answer_index': 0,
    },
    {
        'question': 'What is the currency of Japan?',
        'options': ['Yen', 'Euro', 'Dollar', 'Pound'],
        'answer_index': 0,
    },
    {
        'question': 'Who wrote the Harry Potter books?',
        'options': ['J.K. Rowling', 'Stephen King', 'George R.R. Martin', 'Dan Brown'],
        'answer_index': 0,
    },
    {
        'question': 'What is the highest mountain in the world?',
        'options': ['Mount Everest', 'Mount Kilimanjaro', 'Mount Fuji', 'Mount Rushmore'],
        'answer_index': 0,
    },
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz/<int:question_index>', methods=['GET', 'POST'])
def quiz(question_index):
    question = questions[question_index]
    options = question['options']
    total_questions = len(questions)
    current_question_index = question_index
    next_question_index = question_index + 1 if question_index < total_questions - 1 else None
    score_message = get_score_message(question)
    feedback = None

    if request.method == 'POST':
        selected_option_index = int(request.form['answer'])
        if selected_option_index == question['answer_index']:
            if 'score' not in question:
                question['score'] = 4
            elif question['score'] == 2:
                question['score'] = 4
            elif question['score'] == 1:
                question['score'] = 2
            feedback = 'Correct!'
        else:
            if 'score' not in question:
                question['score'] = 0
            feedback = f'Incorrect. The correct answer is {options[question["answer_index"]]}.'
            question['score'] = max(0, question['score'] - 1)

    return render_template(
        'quiz.html',
        question=question['question'],
        options=options,
        total_questions=total_questions,
        current_question_index=current_question_index,
        next_question_index=next_question_index,
        feedback=feedback,
        score_message=score_message,
    )

@app.route('/score')
def score():
    total_score = sum(question.get('score', 0) for question in questions)
    return render_template('score.html', total_score=total_score)


def get_score_message(question):
    if 'score' in question:
        return f"Score: {question['score']}"
    return "Score: 0"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81,debug=True)
