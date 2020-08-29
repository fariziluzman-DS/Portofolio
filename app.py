from flask import Flask,render_template,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/index.html')
def back():
    return render_template('index.html')

@app.route('/ig')
def ig():
    return redirect("https://www.instagram.com/fl_manov/")

@app.route('/tw')
def tw():
    return redirect("https://twitter.com/fl_manov")

@app.route('/lin')
def lin():
    return redirect("https://www.linkedin.com/in/farizi-luzman-85648919/")

@app.route('/gh')
def gh():
    return redirect("https://github.com/fariziluzman-DS")

if __name__ == '__main__':
    app.run(debug=True, port=3000)


