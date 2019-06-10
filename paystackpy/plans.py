import paystackpy.utils as utils
from paystackpy.apiConfig import APIConfig


class Plan(APIConfig):
    def create(self, name, amount, interval, description=None, \
               send_invoices=False, send_sms=False, hosted_page=False, hosted_page_url=None, hosted_page_summary=None,
               currency=None):
        """
        Creates a new plan. Returns the plan details created

        args:
        name -- Name of the plan to create
        amount -- Amount to attach to this plan
        interval -- 'hourly', 'daily', 'weekly', 'monthly', 'annually'
        description -- Plan Description (optional)
        
        """
        interval = utils.validate_interval(interval)
        amount = utils.validate_amount(amount)

        url = self._url("/plan/")
        payload = {
            "name": name,
            "amount": amount,
            "interval": interval,
            "currency": currency,
            "send_sms": send_sms,
            "description": description,
            "hosted_page": hosted_page,
            "send_invoices": send_invoices,
            "hosted_page_url": hosted_page_url,
            "hosted_page_summary": hosted_page_summary,
        }
        return self._handle_request('POST', url, payload)

    def update(self, plan_id, name, amount, interval, description=None, \
               send_invoices=False, send_sms=False, hosted_page=False, hosted_page_url=None, hosted_page_summary=None,
               currency=None):
        """
        Updates an existing plan given a plan id. Returns the plan details updated.
        
        args:
        plan_id -- Plan Id to update
        name -- New plan name
        amount -- New Amount to attach to this plan
        interval -- 'hourly', 'daily', 'weekly', 'monthly', 'annually'
        description -- Plan Description (optional)
        """
        interval = utils.validate_interval(interval)
        amount = utils.validate_amount(amount)

        url = self._url("/plan/{}/".format(plan_id))
        payload = {
            "name": name,
            "amount": amount,
            "interval": interval,
            "currency": currency,
            "send_sms": send_sms,
            "description": description,
            "hosted_page": hosted_page,
            "send_invoices": send_invoices,
            "hosted_page_url": hosted_page_url,
            "hosted_page_summary": hosted_page_summary,
        }
        return self._handle_request('PUT', url, payload)

    def getall(self, pagination=10):
        """
        Gets all plans
        """
        url = self._url("/plan/?perPage=" + str(pagination))
        return self._handle_request('GET', url)

    def getone(self, plan_id):
        """
        Gets one plan with the given plan id
        Requires: plan_id
        """
        url = self._url("/plan/{}/".format(plan_id))
        return self._handle_request('GET', url)
