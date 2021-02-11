from paystackpy.apiConfig import APIConfig


class Verification(APIConfig):
    def verify_bvn_match(self, bvn, account_number, bank_code, first_name=None,
                         last_name=None):
        url = self._url("/bvn/match")
        payload = {
            "bvn": bvn,
            "account_number": account_number,
            "bank_code": bank_code,
            "fist_name": first_name,
            "last_name": last_name
        }
        return self._handle_request('POST', url, payload)

    def resolve_bvn_standard(self, bvn):
        url = self._url("/bank/resolve_bvn/{}".format(bvn))
        return self._handle_request('GET', url)

    def resolve_bvn_premium(self, bvn):
        url = self._url("/identity/bvn/resolve/{}".format(bvn))
        return self._handle_request('GET', url)

    def resolve_account_number(self, account_number, bank_code):
        url = self._url("/bank/resolve?account_number={0}&bank_code={1}".format(account_number, bank_code))
        return self._handle_request('GET', url)

    def resolve_card_bin(self, card_bin):
        url = self._url("/bank/decision/bin/{}".format(card_bin))
        return self._handle_request('GET', url)
