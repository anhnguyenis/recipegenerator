from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    search = StringField('(separate each ingredient with a comma ,)', validators=[DataRequired()])

    submit = SubmitField('Search')