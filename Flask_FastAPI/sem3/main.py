from flask import Flask, request, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect

from forms import RegistrationForm
from models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///users.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("DB created")


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data.lower()
        surname = form.surname.data.lower()
        email = form.email.data
        user = User(name=name, surname=surname, email=email)
        if User.query.filter(User.email == email).first():
            flash(f'The e-mail: {email} already in use')
            return redirect(url_for('register'))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered!')
        return redirect(url_for('register'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run()