from flask import Flask, render_template, request
from data_analysis_tool import analyze_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        csv_content = file.read()
        results, charts = analyze_data(csv_content)
        return render_template('result.html', results=results, charts=charts)

if __name__ == '__main__':
    app.run(debug=True)
