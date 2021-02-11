from paystackpy.errors import InvalidDataError


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
