
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
Bootstrap(app)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/test")
def okurka_template():
    today=date.today()
    return render_template("okurka.html", today=str(today))

class NameForm(FlaskForm):
    name = StringField('Which actor is your favorite?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/form', methods=['GET', 'POST'])
def form():
    names = ['jana','jirka']
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = NameForm()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
        if name.lower() in names:
            # empty the form field
            form.name.data = ""
            # id = get_id(ACTORS, name)
            # redirect the browser to another route and template
            return print(id)
        else:
            message = "That actor is not in our database."
    return render_template('form.html', names=names, form=form, message=message)
if __name__ == "__main__":
    app.run(host="0.0.0.0")

