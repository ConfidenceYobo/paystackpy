from paystackpy.apiConfig import APIConfig


class Misc(APIConfig):
    def allbanks(self, perpage=50, page=1):
        url = self._url("/bank?perPage={}&page={}".format(perpage, page))
        return self._handle_request('GET', url)

    def balance(self):
        url = self._url("/balance")
        return self._handle_request('GET', url)
