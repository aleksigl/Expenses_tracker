from flask import Flask, request, render_template, redirect, url_for

from forms import ExpensesForm
from models import expenses

app = Flask(__name__)
app.config["SECRET_KEY"] = "qwerty"


@app.route("/expenses/", methods=["GET", "POST"])
def expenses_list():
    form = ExpensesForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            try:
                if not isinstance(form.data, dict):
                    raise ValueError("Invalid form data format.")
                expenses.create(dict(form.data))
                expenses.save_all()
                return redirect(url_for("expenses_list"))
            except Exception as e:
                error = str(e)

    return render_template("Expenses.html", form=form, expenses=expenses.all(), error=error)


@app.route("/expenses/<int:expense_id>/", methods=["GET", "POST"])
def expenses_details(expense_id):
    expense_data = expenses.get(expense_id - 1)

    if not expense_data:
        return redirect(url_for("expenses_list"))
    form = ExpensesForm(data=expense_data)

    if request.method == "POST":
        if form.validate_on_submit():
            expenses.update(expense_id - 1, form.data)
        return redirect(url_for("expenses_list"))

    return render_template("Expense.html", form=form, expense=expense_data, expense_id=expense_id)

@app.route("/expenses/delete/<int:expense_id>/", methods=["POST"])
def delete_expense(expense_id):
    del expenses.expenses[expense_id - 1]
    expenses.save_all()
    return redirect(url_for("expenses_list"))


if __name__ == "__main__":
    app.run(debug=True)
