from flask import Flask, request, render_template, redirect, url_for, jsonify

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


@app.route("/api/v1/expenses/", methods=["GET"])
def get_expenses_api():
    return jsonify(expenses.all())


@app.route("/api/v1/expenses/<int:expense_id>", methods=["GET"])
def get_expense_api(expense_id):
    try:
        expense = expenses.get(expense_id - 1)
        return jsonify(expense)
    except ValueError:
        return jsonify({"error": "Expense not found"}), 404


@app.route("/api/v1/expenses", methods=["POST"])
def add_expense_api():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    try:
        expenses.create(data)
        expenses.save_all()
        return jsonify(data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/v1/expenses/<int:expense_id>", methods=["PUT"])
def update_expense_api(expense_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    try:
        expenses.update(expense_id - 1, data)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/expenses/<int:expense_id>", methods=["DELETE"])
def delete_expense_api(expense_id):
    try:
        expenses.delete(expense_id - 1)
        return jsonify({"message": "Expense successfully deleted"}), 200
    except ValueError:
        return jsonify({"error": "Expense not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
