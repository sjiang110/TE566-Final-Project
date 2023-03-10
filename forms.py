from wtforms import Form, StringField, SelectField, validators


class EmployeeForm(Form):
    firstname = StringField(u'First Name', validators=[validators.input_required()])
    lastname = StringField(u'Last Name', validators=[validators.input_required()])
    address1 = StringField(u'Address 1', validators=[validators.input_required()])
    address2 = StringField(u'Address 2', validators=[validators.optional()])
    city = StringField(u'City', validators=[validators.input_required()])
    state = StringField(u'State', validators=[validators.input_required()])
    zipcode = StringField(u'Zip Code', validators=[validators.input_required()])
    ssn = StringField(u'Social Security Number (numbers only)', validators=[validators.input_required()])
    witholdings = StringField(u'Witholdings', validators=[validators.input_required()])
    salary = StringField(u'Salary (Dollars)', validators=[validators.input_required()])


class CustomerForm(Form):
    companyname = StringField(u'Company Name', validators=[validators.input_required()])
    firstname = StringField(u'First Name', validators=[validators.input_required()])
    lastname = StringField(u'Last Name', validators=[validators.input_required()])
    address1 = StringField(u'Address 1', validators=[validators.input_required()])
    address2 = StringField(u'Address 2', validators=[validators.optional()])
    city = StringField(u'City', validators=[validators.input_required()])
    state = StringField(u'State', validators=[validators.input_required()])
    zipcode = StringField(u'Zip Code', validators=[validators.input_required()])
    price = StringField(u'Price (Dollars)', validators=[validators.input_required()])


class VendorForm(Form):
    companyname = StringField(u'Company Name', validators=[validators.input_required()])
    part = StringField(u'Part', validators=[validators.input_required()])
    price_per_unit = StringField(u'Price/Unit (Dollars)', validators=[validators.input_required()])
    address1 = StringField(u'Address 1', validators=[validators.input_required()])
    address2 = StringField(u'Address 2', validators=[validators.optional()])
    city = StringField(u'City', validators=[validators.input_required()])
    state = StringField(u'State', validators=[validators.input_required()])
    zipcode = StringField(u'Zip Code', validators=[validators.input_required()])


class EmployeePaymentForm(Form):
    employee = SelectField(u'Employee')

class POForm(Form):
    part = SelectField(u'Part')
    quantity = StringField(u'Quantity', validators=[validators.input_required()])

class InvoiceForm(Form):
    customer = SelectField(u'Customer')
    number_to_invoice = StringField(u'Number of Units to Invoice', validators=[validators.input_required()])
    
class BuildInventoryForm(Form):
    quantity = StringField(u'Quantity', validators=[validators.input_required()])