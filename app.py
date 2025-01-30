from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        display = request.form['display']
        try:
            result = eval(display)
            return render_template('index.html', result=result)
        except Exception as e:
            return render_template('index.html', result='Error')
    return render_template('index.html', result='')

if __name__ == '__main__':
    app.run(debug=True)
