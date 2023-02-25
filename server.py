from flask import Flask, render_template, session,redirect,request

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if "visits" not in session:
        session["visits"] = 0
    else:
        session['visits'] += 1
    if "count" not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template("index.html", visits=session["visits"],count=session["count"])

@app.route('/increment', methods =['POST'])
def increment():
    if request.method == "POST":
        increment = int(request.form['increment'])
        session['count'] += increment-1
        return redirect('/')

@app.route('/count2')
def count2():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return redirect('/')

@app.route('/custom')
def custom():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return redirect('/')

@app.route('/reset')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response. Try again.'

if __name__ == "__main__":
    app.run(debug=True)