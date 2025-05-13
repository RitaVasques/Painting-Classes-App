from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, IntegerField, HiddenField, DateField
from wtforms.validators import DataRequired, Email

class StudentForm(FlaskForm):
    student_id = HiddenField('Student_id')
    name = StringField('Full Name', validators=[DataRequired()])
    schedule = StringField('Schedule', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = IntegerField('Phone', validators=[DataRequired()])
    save = SubmitField('Save')

class SearchForm(FlaskForm):
    search_id = IntegerField('Search id', validators=[DataRequired()])
    search = SubmitField('Search')

class IncomeForm(FlaskForm):
    entry_id = HiddenField('Entry_id')
    student_id = IntegerField('Student_id', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    amount = IntegerField('Amount', validators=[DataRequired()])
    insert = SubmitField('Add Income')