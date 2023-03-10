from common import *
from forms import *
from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.config['SECRET_KEY'] = 'testing'
model = model()



@app.route("/")
def main_page():
    return render_template('index.html', employees=model.employees_data, date=model.date)

@app.route("/employees")
def employees():
    return render_template('employees.html', employees=model.employees_data)

@app.route("/add-employee", methods=['GET', 'POST'])
def add_employee():
    form = EmployeeForm(request.form)
    if request.method == 'POST' and form.validate():
        model.employees_data.append(
            employee(form.firstname.data,
                     form.lastname.data,
                     form.address1.data,
                     form.address2.data,
                     form.city.data,
                     form.state.data,
                     form.zipcode.data,
                     form.ssn.data,
                     form.witholdings.data,
                     form.salary.data))
        return redirect('/')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error))
    return render_template('add_employee.html', form=form)


@app.route("/customers")
def customers():
    return render_template('customers.html', customers=model.customers_data)

@app.route("/add-customer", methods=['GET', 'POST'])
def add_customer():
    form = CustomerForm(request.form)
    if request.method == 'POST' and form.validate():
        model.customers_data.append(
            customer(form.companyname.data,
                     form.firstname.data,
                     form.lastname.data,
                     form.address1.data,
                     form.address2.data,
                     form.city.data,
                     form.state.data,
                     form.zipcode.data,
                     form.price.data))
        return redirect('/')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error))
    return render_template('add_customer.html', form=form)

@app.route("/vendors")
def vendors():
    return render_template('vendors.html', vendors=model.vendors_data)

@app.route("/add-vendor", methods=['GET', 'POST'])
def add_vendor():
    form = VendorForm(request.form)
    if request.method == 'POST' and form.validate():
        model.vendors_data.append(
            vendor(form.companyname.data,
                   form.part.data,
                   form.price_per_unit.data,
                   form.address1.data,
                   form.address2.data,
                   form.city.data,
                   form.state.data,
                   form.zipcode.data,))
        return redirect('/')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error))
    return render_template('add_vendor.html', form=form)

@app.route("/pay-employee", methods=['GET', 'POST'])
def pay_employee():
    form = EmployeePaymentForm(request.form)
    form.employee.choices = [(e.ssn, e.lastname) for e in model.employees_data]
    if request.method == 'POST':
        employee = next(e for e in model.employees_data if e.ssn == form.employee.data)
        total_paid = model.payroll_data.add_payroll_event(payroll_event(employee, model.date.date))
        model.income_data.payroll = model.payroll_data.total_dispursement
        model.income_data.payroll_withholding = model.payroll_data.total_witholdings
        model.balance_sheet_data.cash -= total_paid
        return redirect('/')
    return render_template('pay_employee.html', form=form)

@app.route("/income-statement")
def income_statement():
    return render_template('income_statement.html', income=model.income_data)

@app.route("/balance-sheet")
def balance_sheet():
    return render_template('balance_sheet.html', balancesheet=model.balance_sheet_data, inventory=model.balance_sheet_data.inventory_data)

@app.route("/payroll")
def payroll():
    return render_template('payroll.html', payroll=model.payroll_data)

@app.route("/inventory")
def inventory():
    form = BuildInventoryForm(request.form)
    if request.method == 'POST':
        model.balance_sheet_data.inventory_data.build_complete_unit(form.quantity.data)
        return redirect('/')
    return render_template('inventory.html', inventory=model.balance_sheet_data.inventory_data)

@app.route("/create-invoice", methods=['GET', 'POST'])
def create_invoice():
    form = InvoiceForm(request.form)
    form.customer.choices = [(c.companyname, c.companyname) for c in model.customers_data]
    if request.method == 'POST':
        number_to_invoice = int(form.number_to_invoice.data)
        cost = model.sale_price_per_unit * number_to_invoice
        # Update balance sheet
        model.balance_sheet_data.ar += cost
        # Update income statement
        model.income_data.sales += cost
        model.income_data.cogs += model.balance_sheet_data.inventory_data.cog_per_unit * number_to_invoice
        # Updated inventory
        model.balance_sheet_data.inventory_data.purchase_complete_unit(number_to_invoice)
        # Add to history
        model.invoice_history.create_invoice(form.customer.data, form.number_to_invoice.data, model.sale_price_per_unit, cost, model.date.date)
        return redirect('/')
    return render_template('create_invoice.html', form=form, inventory=model.balance_sheet_data.inventory_data)

@app.route("/invoice-history")
def invoices_history():
    return render_template('invoice_history.html', invoice_history=model.invoice_history)

@app.route("/create-po", methods=['GET', 'POST'])
def create_po():
    form = POForm(request.form)
    form.part.choices = [(p, p) for p in model.balance_sheet_data.inventory_data.parts]
    if request.method == 'POST':
        vendor = next(v for v in model.vendors_data if v.part == form.part.data)
        quantity = int(form.quantity.data)
        cost = vendor.price_per_unit * int(form.quantity.data)
        # Update balance sheet
        model.balance_sheet_data.ap += cost
        # Updated inventory
        model.balance_sheet_data.inventory_data.purchase_part(form.part.data, int(form.quantity.data))
        # Add to history
        model.purchase_order_history.create_po(vendor.companyname, form.part.data, quantity, vendor.price_per_unit, cost, model.date.date)
        return redirect('/')
    return render_template('create_po.html', form=form)

@app.route("/po-history")
def po_history():
    return render_template('po_history.html', purchase_order_history=model.purchase_order_history)

@app.route("/advance-date")
def advance_date():
    model.date.advance_a_month()
    # Update balance sheet
    model.balance_sheet_data.cash -= model.balance_sheet_data.ap
    model.balance_sheet_data.ap = 0
    model.balance_sheet_data.cash += model.balance_sheet_data.ar
    model.balance_sheet_data.ar = 0
    # Update income statement
    model.income_data.expense_accounts.total_expenses += model.income_data.expense_accounts.total_monthly_expenses
    return redirect('/')

@app.route("/re-init")
def re_init():
    model.reinitialize()
    return redirect('/')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)