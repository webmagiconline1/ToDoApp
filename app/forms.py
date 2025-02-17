# filepath: todoapp/app/forms.py
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    done = BooleanField('Done')
    recaptcha = RecaptchaField()
    submit = SubmitField('Add Task')