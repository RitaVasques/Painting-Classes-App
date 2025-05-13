from flask import Flask, redirect, url_for, render_template, request, flash
from manage_student import ManageStudent
from student import Student
from forms import StudentForm, IncomeForm, SearchForm
from income import Income
from manage_income import ManageIncome
import plotly.express as px
import pandas as pd

app = Flask(__name__, static_folder='static', template_folder='templates')

myTitle_home = 'Painting Classes App'
myTitle_income = 'Painting Classes - Income'
myTitle_students = 'Painting Classes - Students'

app.config['SECRET_KEY'] = 'its_a_secret'

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html', title=myTitle_home)

# STUDENTS 
@app.route('/students')
def students():
    try:
        # Get students from database
        students_db = ManageStudent.selectAll()
        # Creat an empty obj from students form
        student_form = StudentForm(obj=Student())
        return render_template('students.html', title=myTitle_students, students=students_db, std_form=student_form)
    except Exception as e:
        flash(f'Failed to load student data: {str(e)}', 'error')
        return render_template('students.html', title=myTitle_students, students=[], std_form=student_form)

@app.route('/save', methods=['POST'])
def save():
    # Creat an empty obj from students form
    student = Student()
    student_form = StudentForm(obj=student)
    if student_form.validate_on_submit():
        try:
            # create student with values from form
            student_form.populate_obj(student)
            if not student.student_id:
                # save student in database
                ManageStudent.insert(student)
            else:
                ManageStudent.update(student)
        except Exception as e:
            flash(f'Failed to save student: {str(e)}', 'error')
    # go back to page with updated database
    return redirect(url_for('students'))

@app.route('/clear')
def clear():
    return redirect(url_for('students'))

@app.route('/edit/<int:student_id>')
def edit(student_id):
    try:
        student = ManageStudent.select_by_id(student_id)
        student_form = StudentForm(obj=student)
        # Get list of all students
        students_db = ManageStudent.selectAll()
        return render_template('students.html', title=myTitle_students, students=students_db, std_form=student_form)
    except Exception as e:
        flash('Failed to edit student', 'error')
        return redirect(url_for('students'))

@app.route('/delete/<int:student_id>')
def delete(student_id):
    try:
        student = Student(student_id=student_id)
        ManageStudent.delete(student)
    except Exception as e:
        flash(f'Failed to delete student: {str(e)}', 'error')
    return redirect(url_for('students'))

# INCOME
@app.route('/income', methods=['GET', 'POST'])
def income():
    income_form = IncomeForm()
    search_form = SearchForm()
    results = None

    # get data for the graph
    chart_data = ManageIncome.get_chart_data()
    
    if chart_data:  # Only plot if data exists
        df = pd.DataFrame(chart_data)
        fig = (px.bar(df, x='date', y='total_amount', 
                     labels={'total_amount': 'Income (€)', 'date': 'Date'},
                     color_discrete_sequence=['#ef7538'])
            .update_layout(title_text='Income Over Time',
                          title_x=0.5,
                          title_font=dict(size=18)))
        # Make everything transparent except data
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='black'),
            xaxis=dict(
                showgrid=False,
                linecolor='black',
                tickfont=dict(color='black')
            ),
            yaxis=dict(
                showgrid=True, gridcolor='black',
                linecolor='black',
                tickfont=dict(color='black')
            ),
        )
        # Convert to HTML
        graph_html = fig.to_html(full_html=False, 
                                 config={'displayModeBar': False})  # Removes the menu bar
    else:
        graph_html = '<p>No income data available</p>'
        flash('No income records found in the database', 'info')

    if request.method == 'POST':
        if 'submit' in request.form and request.form['submit'] == 'search': # search form was submitted
            search_form = SearchForm(request.form)
            
            if search_form.validate():
                try:
                    input_id = search_form.search_id.data
                    results = ManageIncome.search_by_id(input_id)
                    if not results:
                        flash(f'No records found for student ID: {input_id}', 'info')
                except Exception as e:
                    flash(f'Search error: {str(e)}', 'error')
                    
        elif 'insert' in request.form:  # Income form was submitted
            income_form = IncomeForm(request.form)
            if income_form.validate_on_submit():
                try:
                    income = Income()
                    income_form.populate_obj(income)
                    student = ManageStudent.select_by_id(income.student_id)
                    if not student:
                        flash('Student not found', 'error')
                    else:
                        ManageIncome.insert(income)
                        return redirect(url_for('income'))
                except Exception as e:
                    flash(f'Error adding record: {str(e)}', 'error')

    return render_template('income.html', 
                         title=myTitle_income, 
                         income_form=income_form,
                         search_form=search_form,
                         results=results,
                         graph_html=graph_html)

@app.route('/clear_inc')
def clear_inc():
    return redirect(url_for('income'))

if __name__ == '__main__':
    app.run(debug=True) 
