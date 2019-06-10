import paystackpy.utils as utils
from paystackpy.apiConfig import APIConfig


class Transfer(APIConfig):
    def create_transfer_recipient(self, receipt_type='nuban', name=None, metadata=None, account_number=None,
                                  bank_code=None,
                                  currency=None, description=None, authorization_code=None):
        url = self._url("/transferrecipient")
        payload = {
            "receipt_type": receipt_type,
            "name": name,
            "metadata": metadata,
            "account_number": account_number,
            "bank_code": bank_code,
            "currency": currency,
            "description": description,
            "authorization_code": authorization_code
        }
        return self._handle_request('POST', url, payload)

    def get_transfer_recipient(self, perpage=50, page=1):
        url = self._url("/transferrecipient?perPage={}&page={}".format(perpage, page))

        return self._handle_request('GET', url)

    def update_transfer_recipient(self, refcode=None, name=None, email=None):
        url = self._url("/transferrecipient/{}".format(refcode))
        payload = {
            "name": name,
            "email": email
        }
        return self._handle_request('PUT', url, payload)

    def delete_recipient(self, refcode):
        url = self._url("/transferrecipient/{}".format(refcode))

        return self._handle_request('DELETE', url)

    def initiate(self, source=None, amount=None, currency=None, reason=None, recipient=None):
        url = self._url("/transfer")

        amount = utils.validate_amount(amount)

        payload = {
            "source": source,
            "amount": amount,
            "currency": currency,
            "reason": reason,
            "recipient": recipient,
            "reference": utils.reference_gen()
        }

        return self._handle_request('POST', url, payload)

    def all_transfers(self, perpage=50, page=1):
        url = self._url("/transfer?perPage={}&page={}".format(perpage, page))

        return self._handle_request('GET', url)

    def get_transfer(self, ref_or_code):
        url = self._url("/transfer/{}".format(ref_or_code))

        return self._handle_request('GET', url)

    def finalize_transfer(self, transfer_code, otp):
        url = self._url("/transfer/finalize_transfer")

        payload = {
            "otp": otp,
            "transfer_code": transfer_code
        }

        return self._handle_request('POST', url, payload)
