from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'counter'

@app.route('/', methods=['POST', 'GET'])
def counter():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template("index.html")

@app.route('/add_two', methods=['POST'])
def add_two():
    session['count'] += 1
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session.clear();
    print(f"Count destroyed!")
    return redirect('/')

@app.route('/add_x', methods=['POST'])
def add_x():
    print(request.form['x'])
    if request.form['x'] != '':
        session['count'] += int(request.form['x']) - 1
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)