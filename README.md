# paystackpy
===============================

Overview
--------

A Paystack ( https://paystack.com/ ) API wrapper with python

Documentation
-------------

Please see https://developers.paystack.co/docs for the most up-to-date documentation for the Paystack API.


# Installation

pip install paystackpy

# Example

```python
from paystackpy import Transaction, Customer, Plan, Transfer
```
"""
All Response objects are a dictionay containing status_code, status, message and data
"""

#Instantiate the transaction object to handle transactions.
#Pass in your authorization key - if not set as environment variable PAYSTACK_AUTHORIZATION_KEY
```
transaction = Transaction(authorization_key="sk_mypaystackauthorizationkey")
response = transaction.charge("customer@domain.com", "CustomerAUTHcode", 10000) #Charge a customer in Kobo.
response  = transaction.verify(refcode) #Verify a transaction given a reference code "refcode".
```

#Instantiate the customer class to manage customers
```
customer = Customer(authorization_key="sk_mypaystackauthorizationkey")
response = customer.create("customer2@gmail.com", "John", "Doe", phone="080*********") #Add new customer
response = customer.getone(1234) #Get customer with id of 1234
response = customer.getall() #Get all customers
```

#Instantiate the plan class to manage plans
```
plan = Plan(authorization_key="sk_mypaystackauthorizationkey")
response = plan.create("Test Plan", 150000, 'Weekly') #Add new plan
response = plan.getone(240) #Get plan with id of 240
response = plan.getall() #Get all plans
```

#Instantiate the transaction claas for transfer
```
transfer = Transfer(authorization_key="sk_mypaystackauthorizationkey")
response = transfer.create_transfer_recipient(receipt_type="nuban", name="Customer", metadata={}, account_number="092********", bank_code="058", currency="NGN", description="SOME TEXT", authorization_code="code")

```
