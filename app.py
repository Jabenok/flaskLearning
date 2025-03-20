from flask import Flask, render_template, url_for, request, flash, session, redirect 

app = Flask(__name__)

app.config['SECRET_KEY'] = 'key'

@app.route("/")
def index():
    #print(url_for('index'))
    return render_template('index.html', title="Learning Flask")


@app.route("/about", methods=["POST", "GET"])
def about():

    
    if request.method=='POST':


        if len(request.form['username']) > 2:
            flash("Сообщение успешно отправлено", category='success')
        else:
            flash("Ошибка отправки", category='error')


        print(request.form)
    
    return render_template('about.html', title="About website")

@app.route("/profile/<path:username>")
def profile(username):
    return f"Пользователь: {username}"


@app.route("/login", methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method=='POST' and request.form['username'] == "admin" and request.form["password"]=="admin":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    
    return render_template('login.html', title="Login")


#Если страница не найдена
@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title="Страница не найдена"), 404

if __name__=="__main__":
    app.run(debug=True)