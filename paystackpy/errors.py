class PaystackPyError(Exception):
    """
    Python Paystack Error
    """
    pass


class MissingAuthKeyError(PaystackPyError):
    """
    We can't find the authentication key
    """
    pass


class InvalidMethodError(PaystackPyError):
    """
    Invalid or unrecoginised/unimplemented HTTP request method
    """
    pass


class InvalidDataError(PaystackPyError):
    """
    Invalid input recognised. Saves unecessary trip to server
    """
    pass
