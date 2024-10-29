from flask import Flask, render_template

app = Flask(__name__)
acronyms = [
    ("Gerardo M.", "brb"),
    ("Millonoel R.", "smh"),
]
@app.route('/')
def hello():
    html_content = "<h1>My classmates favorite acronyms</h1>"
    for name, acronym in acronyms:
        html_content += f"<p>{name} : {acronym}</p>"
    return html_content

@app.route('/calvario')
def favorite_acronym():
    return render_template('my_template_1.html')

