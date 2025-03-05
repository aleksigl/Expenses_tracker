from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length, NumberRange, Optional


def integer_only(form, field):
    if not isinstance(field.data, int):
        raise ValidationError("Price must be a whole number.")

class ExpensesForm(FlaskForm):
    expense_name = StringField('Expense Name', validators=[DataRequired()])
    category = SelectField('Category', choices=[('mortgage', 'Mortgage'), ('bills', 'Bills'), ('food', 'Food'), ('doggo', 'Doggo'), ('car', 'Car'), ('hobbies', 'Hobbies'), ('travel', 'Travel'), ('others', 'Others')], validators=[DataRequired()])
    price = IntegerField ('Price (PLN)',  validators=[NumberRange(min=0, max=10000), DataRequired(), integer_only])
    account = SelectField('Account', choices=[('wifeys', "Wifey's"), ('husbands', "Husband's"), ('common', 'Common')], validators=[DataRequired()])
    date = DateField('Date (YYYY-MM-DD)', format='%Y-%m-%d', validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[Optional(), Length(max=500)])
