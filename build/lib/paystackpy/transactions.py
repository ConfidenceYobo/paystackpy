import paystackpy.utils as utils
from paystackpy.apiConfig import APIConfig
from paystackpy.errors import InvalidDataError


class Transaction(APIConfig):
    def getall(self, pagination=10):
        """
        Gets all your transactions

        args:
        pagination -- Count of data to return per call 
        """
        url = self._url("/transaction/?perPage=" + str(pagination))
        return self._handle_request('GET', url)

    def getone(self, transaction_id):
        """
        Gets one customer with the given transaction id

        args:
        Transaction_id -- transaction we want to get
        """
        url = self._url("/transaction/{}/".format(transaction_id))
        return self._handle_request('GET', url)

    def totals(self):
        """
        Gets transaction totals
        """
        url = self._url("/transaction/totals/")
        return self._handle_request('GET', url)

    def initialize(self, email, amount, plan=None, reference=None, channel=None, metadata=None):
        """
        Initialize a transaction and returns the response

        args:
        email -- Customer's email address
        amount -- Amount to charge
        plan -- optional
        Reference -- optional
        channel -- channel type to use
        metadata -- a list if json data objects/dicts
        """
        amount = utils.validate_amount(amount)

        if not email:
            raise InvalidDataError("Customer's Email is required for initialization")

        url = self._url("/transaction/initialize")
        payload = {
            "email": email,
            "amount": amount,
            "reference": reference,
            "plan": plan,
            "channels": channel,
            "metadata": {"custom_fields": metadata}
        }
        return self._handle_request('POST', url, payload)

    def charge(self, email, auth_code, amount, reference=None):
        """
        Charges a customer and returns the response

        args:
        auth_code -- Customer's auth code
        email -- Customer's email address
        amount -- Amount to charge
        reference -- optional
        """
        amount = utils.validate_amount(amount)

        if not email:
            raise InvalidDataError("Customer's Email is required to charge")

        if not auth_code:
            raise InvalidDataError("Customer's Auth code is required to charge")

        url = self._url("/transaction/charge_authorization")
        payload = {
            "authorization_code": auth_code,
            "email": email,
            "amount": amount,
            "reference": reference
        }

        return self._handle_request('POST', url, payload)

    def verify(self, reference):
        """
        Verifies a transaction using the provided reference number

        args:
        reference -- reference of the transaction to verify
        """

        reference = str(reference)
        url = self._url("/transaction/verify/{}".format(reference))
        return self._handle_request('GET', url)


