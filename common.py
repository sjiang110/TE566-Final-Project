import datetime

class model():
    def __init__(self):
        self.employees_data = []
        self.customers_data = []
        self.vendors_data = []
        self.payroll_data = payroll()
        self.invoice_history = invoices()
        self.purchase_order_history = purchase_orders()
        self.sale_price_per_unit = 1200.00  # Fixed per the example problem
        self.date = current_date()

        self.income_data = income_statement(sales=0,
                                            cogs=0,
                                            payroll=0,
                                            payroll_withholding=0,
                                            bills=0,
                                            other_income=0,
                                            income_taxes=0)
        self.balance_sheet_data = balance_sheet(cash=2000000,
                                                ar=0,
                                                inventory_data=inventory(107),
                                                lands_buildings=0,
                                                equipment=0,
                                                furniture_fixtures=0,
                                                ap=0,
                                                notes_payable=0,
                                                accruals=0,
                                                mortgage=0)
        self.employees_data.append(
            employee('john', 'smith', '123 address ln', 'apt 100', 'Seattle', 'WA', '12345', '123-45-6789', '0', '60000'))
        self.employees_data.append(
            employee('jane', 'doe', '123 address ln', 'apt 100', 'Seattle', 'WA', '12345', '123-45-6789', '0', '60000'))
        self.employees_data.append(
            employee('sara', 'jiang', '123 address ln', 'apt 100', 'Seattle', 'WA', '12345', '123-45-6789', '0', '150000'))
        self.employees_data.append(
            employee('justin', 'zhou', '123 address ln', 'apt 100', 'Seattle', 'WA', '12345', '123-45-6789', '0', '100000'))
        self.employees_data.append(
            employee('brian', 'lilly', '123 address ln', 'apt 100', 'Seattle', 'WA', '12345', '123-45-6789', '0', '200000'))
        self.employees_data.append(
            employee('kevin', 'lee', '123 address ln', 'apt 100', 'Seattle', 'WA', '12345', '123-45-6789', '0', '45000'))
        self.employees_data.append(
            employee('angela', 'jaw', '123 address ln', 'apt 100', 'Seattle', 'WA', '12345', '123-45-6789', '0', '90000'))
        
        self.customers_data.append(customer('Microcenter', '', '', '', '', '', '', '', '1200.00'))
        self.customers_data.append(customer('Best Buy', '', '', '', '', '', '', '', '1200.00'))
        self.customers_data.append(customer('Newegg', '', '', '', '', '', '', '', '1200.00'))
        self.customers_data.append(customer('Amazon', '', '', '', '', '', '', '', '1200.00'))
        self.customers_data.append(customer('Walmart', '', '', '', '', '', '', '', '1200.00'))
        self.customers_data.append(customer('Target', '', '', '', '', '', '', '', '1200.00'))
        self.customers_data.append(customer('Computer World', '', '', '', '', '', '', '', '1200.00'))
        self.customers_data.append(customer('Rakuten', '', '', '', '', '', '', '', '1200.00'))
        self.customers_data.append(customer('BestPCNow', '', '', '', '', '', '', '', '1200.00'))
        
        self.vendors_data.append(vendor('AMD', 'CPU', '200.00', '', '', '', '', ''))
        self.vendors_data.append(vendor('Asus', 'Motherboard', '100.00', '', '', '', '', ''))
        self.vendors_data.append(vendor('Corsair', 'RAM', '25.00', '', '', '', '', ''))
        self.vendors_data.append(vendor('Asus', 'GPU', '400.00', '', '', '', '', ''))
        self.vendors_data.append(vendor('Samsung', 'SSD', '85.00', '', '', '', '', ''))
        self.vendors_data.append(vendor('Fractal', 'Case', '43.99', '', '', '', '', ''))
        self.vendors_data.append(vendor('Corsair', 'CPU Cooler', '15.00', '', '', '', '', ''))
        self.vendors_data.append(vendor('Corsair', 'Power Supply', '73.45', '', '', '', '', ''))
        self.vendors_data.append(vendor('Box Box', 'Box', '1.85', '', '', '', '', ''))
        self.vendors_data.append(vendor('None', 'Labor', '45.00', '', '', '', '', ''))
        self.vendors_data.append(vendor('Foamys', 'Foam', '0.58', '', '', '', '', ''))
        self.vendors_data.append(vendor('We Luv Cables', 'Cables', '0.13', '', '', '', '', ''))
        self.vendors_data.append(vendor('Only Fans', 'Fans', '2.49', '', '', '', '', ''))

    def reinitialize(self):
        self.__init__()

class current_date():
    def __init__(self):
        self._date = datetime.date.today()
        self.months_advanced = 0

    def advance_a_month(self):
        self.months_advanced += 1

    @property
    def date(self):
        delta = datetime.timedelta(self.months_advanced * 365 / 12)
        return (datetime.date.today() + delta).isoformat()

class employee():
    def __init__(self, firstname, lastname, address1, address2,
                 city, state, zipcode, ssn, witholdings, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.ssn = ssn
        self.witholdings = int(witholdings)
        self.salary = float(salary)

class customer():
    def __init__(self, companyname, firstname, lastname, address1, address2,
                 city, state, zipcode, price):
        self.companyname = companyname
        self.firstname = firstname
        self.lastname = lastname
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.price = float(price)

class vendor():
    def __init__(self, companyname, part, price_per_unit, address1, address2, city,
                 state, zipcode):
        self.companyname = companyname
        self.part = part
        self.price_per_unit = float(price_per_unit)
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zipcode = zipcode

class payroll():
    def __init__(self, todal_dispursement=0, total_witholdings=0):
        self.payroll_events = []
        self.total_dispursement = todal_dispursement
        self.total_witholdings = total_witholdings

    def add_payroll_event(self, event):
        self.payroll_events.append(event)
        self.total_dispursement += event.dispursement
        self.total_witholdings += event.witholdings
        return self.total_dispursement + self.total_witholdings

class payroll_event():
    def __init__(self, employee, date_paid, bounce=0):
        self.lastname = employee.lastname
        self.date_paid = date_paid
        self.bounce = bounce
        self.salary = employee.salary/12.0
        self.federal_tax = 1559.45 + (self.salary - 7850) * 0.28
        self.state_tax = self.salary * 0.0495
        self.social_sec_tax = self.salary * 0.062
        self.medicare_tax = self.salary * 0.0145
        self.dispursement = self.salary - self.witholdings

    @property
    def witholdings(self):
        return self.federal_tax + self.state_tax + self.social_sec_tax + self.medicare_tax

class part():
    def __init__(self, price_per_unit, quantity, bom_qty):
        self.price_per_unit = float(price_per_unit)
        self.quantity = int(quantity)
        self.bom_qty = int(bom_qty)

    @property
    def value(self):
        return self.price_per_unit * self.quantity

    @property
    def re_order(self):
        if self.quantity < 100:
            return 'X'
        return ''

class inventory():
    def __init__(self, complete_units):
        self.parts = {}
        self.parts['CPU'] = part('200.00', '142', 1)
        self.parts['Motherboard'] = part('100.00', '59', 1)
        self.parts['GPU'] = part('400.00', '32', 1)
        self.parts['RAM'] = part('25.00', '245', 2)
        self.parts['SSD'] = part('85.00', '42', 2)
        self.parts['Case'] = part('43.99', '531', 1)
        self.parts['CPU Cooler'] = part('15.00', '600', 1)
        self.parts['Power Supply'] = part('73.45', '234', 1)
        self.parts['Box'] = part('1.85', '1100', 1)
        self.parts['Foam'] = part('0.58', '4231', 3)
        self.parts['Labor'] = part('45.00', '50000', 1)
        self.parts['Cables'] = part('0.13', '100000', 5)
        self.parts['Fans'] = part('2.49', '4233', 3)
        self.complete_units = complete_units
        
    def units_possible_to_build(self):
        units_possible = [p.quantity/p.bom_qty for name, p in self.parts.iteritems()]
        if units_possible:
            return min(units_possible)
        else:
            return 0

    def purchase_part(self, part_name, additional_qty):
        self.parts[part_name].quantity += additional_qty

    def purchase_complete_unit(self, qty):
        self.complete_units -= qty
        
    def build_complete_unit(self, qty):
        units_to_build = min(self.units_possible_to_build(), qty)
        for name, p in self.parts.iteritems():
            self.parts[name].quantity -= units_to_build * p.bom_qty
        self.complete_units += units_to_build

    @property
    def cog_per_unit(self):
        count = 0
        for name, p in self.parts.iteritems():
            count += p.price_per_unit * p.bom_qty
        return count

    @property
    def total(self):
        count = 0
        for name, p in self.parts.iteritems():
            count += p.value
        return count

    @property
    def complete_units_to_build(self):
        return self.units_possible_to_build()

    @property
    def complete_units_cost(self):
        return self.complete_units * self.cog_per_unit

class purchase_orders():
    def __init__(self):
        self.po_events = []
        self.po_number = 1

    def create_po(self, supplier, part, quantity, price_per_unit, total, date_paid):
        self.po_events.append(purchase_order(self.po_number, supplier, part, quantity, price_per_unit, total, date_paid))
        self.po_number += 1

class purchase_order():
    def __init__(self, number, supplier, part, quantity, price_per_unit, total, date_paid):
        self.number = number
        self.supplier = supplier
        self.part = part
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.total = total
        self.date_paid = date_paid

class invoices():
    def __init__(self):
        self.invoice_events = []
        self.invoice_number = 1

    def create_invoice(self, customer, quantity, price_per_unit, total, date_paid):
        self.invoice_events.append(invoice(self.invoice_number, customer, quantity, price_per_unit, total, date_paid))
        self.invoice_number += 1

class invoice():
    def __init__(self, number, customer, quantity, price_per_unit, total, date_paid):
        self.number = number
        self.customer = customer
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.total = total
        self.date_paid = date_paid

class income_statement():
    def __init__(self, sales, cogs, payroll, payroll_withholding, bills,
                 other_income, income_taxes):
        self.sales = sales
        self.cogs = cogs
        self.payroll = payroll
        self.payroll_withholding = payroll_withholding
        self.bills = bills
        self.expense_accounts = monthly_expenses(maintenance=1250*2,
                                                 cleaning=416.67*2,
                                                 water=416.67*2,
                                                 sewage=833.33*2,
                                                 electricity=1250*2,
                                                 travel=833.33*2,
                                                 donuts=416.67*2,
                                                 gas=1250*2,
                                                 internet=833.33*2,
                                                 phone=833.33*2)
        self.other_income = other_income
        self.income_taxes = income_taxes

    @property
    def annual_expenses(self):
        return self.expense_accounts.total_expenses

    @property
    def gross_profit(self):
        return self.sales - self.cogs

    @property
    def expenses(self):
        return self.payroll + self.bills + self.annual_expenses

    @property
    def operating_income(self):
        return self.gross_profit - self.expenses

    @property
    def net_income(self):
        return self.operating_income - self.income_taxes

class balance_sheet():
    def __init__(self, cash, ar, inventory_data, lands_buildings, equipment, furniture_fixtures,
                 ap, notes_payable, accruals, mortgage):
        self.cash = cash
        self.ar = ar
        self.lands_buildings = lands_buildings
        self.equipment = equipment
        self.furniture_fixtures = furniture_fixtures
        self.ap = ap
        self.notes_payable = notes_payable
        self.accruals = accruals
        self.mortgage = mortgage
        self.inventory_data = inventory_data

    @property
    def total_current_assets(self):
        return self.cash + self.ar + self.inventory_data.total

    @property
    def total_fixed_assets(self):
        return self.lands_buildings + self.equipment + self.furniture_fixtures

    @property
    def total_assets(self):
        return self.total_current_assets + self.total_fixed_assets

    @property
    def total_current_liabilities(self):
        return self.ap + self.notes_payable + self.accruals

    @property
    def total_long_term_debt(self):
        return self.mortgage

    @property
    def total_liabilities(self):
        return self.total_current_liabilities + self.total_long_term_debt

    @property
    def net_worth(self):
        return self.total_assets - self.total_liabilities

class monthly_expenses():
    def __init__(self, maintenance, cleaning, water, sewage, electricity, travel, donuts, gas, internet, phone):
        self.maintenance = maintenance
        self.cleaning = cleaning
        self.water = water
        self.sewage = sewage
        self.electricity = electricity
        self.travel = travel
        self.donuts = donuts
        self.gas = gas
        self.internet = internet
        self.phone = phone
        self.total_expenses = self.total_monthly_expenses

    @property
    def total_monthly_expenses(self):
        return self.maintenance + self.cleaning + self.water + self.sewage + self.electricity + self.travel + self.donuts + self.gas + self.internet + self.phone