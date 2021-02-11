# paystackpy
===============================

Overview
--------

A Paystack ( https://paystack.com/ ) API wrapper with python

Documentation
-------------

Please see https://paystack.com/docs/api/ for the most up-to-date documentation for the Paystack API.


# Installation

pip install paystackpy

# Example

```python
from paystackpy import Transaction, Customer, Plan, Transfer, Verification
```
"""
All Response objects are formatted as dictionary containing status_code, status, message and data
"""

#Instantiate the transaction object to handle transactions.
#Pass in your authorization key - if not set as environment variable PAYSTACK_AUTHORIZATION_KEY
```python
transaction = Transaction(authorization_key="sk_mypaystackauthorizationkey")
response = transaction.charge("customer@domain.com", "CustomerAUTHcode", 10000) #Charge a customer in Kobo.
response  = transaction.verify("refcode") #Verify a transaction given a reference code "refcode".
```

#Instantiate the customer class to manage customers
```python
customer = Customer(authorization_key="sk_mypaystackauthorizationkey")
response = customer.create("customer2@gmail.com", "John", "Doe", phone="080*********") #Add new customer
response = customer.getone(1234) #Get customer with id of 1234
response = customer.getall() #Get all customers
```

#Instantiate the plan class to manage plans
```python
plan = Plan(authorization_key="sk_mypaystackauthorizationkey")
response = plan.create("Test Plan", 150000, 'Weekly') #Add new plan
response = plan.getone(240) #Get plan with id of 240
response = plan.getall() #Get all plans
```

#Instantiate the transaction class for transfer
```python
transfer = Transfer(authorization_key="sk_mypaystackauthorizationkey")
response = transfer.create_transfer_recipient(receipt_type="nuban", name="Customer", metadata={}, account_number="092********", bank_code="058", currency="NGN", description="SOME TEXT", authorization_code="code")

```

#Verify BVN match
```python
verify = Verification(authorization_key="sk_mypaystackauthorizationkey")
response = verify.verify_bvn_match("bvn", "account_number", "bank_code", "first_name", "last_name")
```

#Resolve BVN standard
```python
verify = Verification(authorization_key="sk_mypaystackauthorizationkey")
response = verify.resolve_bvn_standard("bvn")
```

#Resolve BVN premium
```python
verify = Verification(authorization_key="sk_mypaystackauthorizationkey")
response = verify.resolve_bvn_premium("bvn")
```

#Resolve Account number
```python
verify = Verification(authorization_key="sk_mypaystackauthorizationkey")
response = verify.resolve_account_number("account_number", "bank_code")
```

#Resolve Card BIN
```python
verify = Verification(authorization_key="sk_mypaystackauthorizationkey")
response = verify.resolve_card_bin("bin")
```
