from paystackpy.errors import InvalidDataError
import random
# random.seed(123)


def validate_amount(amount):
    if not amount:
        raise InvalidDataError("Amount to be charged is required")

    if isinstance(amount, int) or isinstance(amount, float):
        if amount < 0:
            raise InvalidDataError("Invalid amount! Amount must not be a negative number")
        return amount
    else:
        raise InvalidDataError("Amount should be a number or a float data type")


def validate_interval(interval):

    interval = interval if interval.lower() in ['hourly', 'daily', 'weekly', 'monthly', 'annually'] else None
    if not interval:
        raise InvalidDataError("Please provide a valid plan interval")
    return interval


def reference_gen():
    possibilities = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    token = ""
    token_length = 12

    for i in range(0, token_length):
        math_random = random.random()
        if math_random < 1:
            math_random = random.uniform(0.1, 0.9)
        token += possibilities[round(math_random * len(possibilities))]

    return token
