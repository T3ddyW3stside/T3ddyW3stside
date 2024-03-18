from flask import Flask, render_template, request
from language_tool_python import LanguageTool

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_spelling', methods=['POST'])
def check_spelling():
    text = request.form['text']
    language = request.form['language']
    
    # check spelling
    tool = LanguageTool(language)
    matches = tool.check(text)
    
    # correct spelling
    corrected_text = tool.correct(text)
    
    # show correct spelling
    return render_template('results.html', matches=matches, corrected_text=corrected_text)

if __name__ == '__main__':
    app.run(debug=True)
