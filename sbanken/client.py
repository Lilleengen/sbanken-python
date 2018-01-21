import json

import requests
from requests.auth import HTTPBasicAuth


class SbankenAPI:
    api_root = 'https://api.sbanken.no'

    def __init__(self, client_id, secret):
        self.client_id = client_id
        self.secret = secret
        self.token = False

    def get_token(self):
        if not self.token:
            token_request = requests.post(self.api_root + '/identityserver/connect/token',
                                          {'grant_type': 'client_credentials'},
                                          auth=HTTPBasicAuth(self.client_id, self.secret))

            self.token = json.loads(token_request.text)['access_token']

        return self.token

    def get_header(self):
        token = self.get_token()
        return {
            'Authorization': 'Bearer ' + token,
        }

    def get_accounts(self, user_id):
        accounts_request = requests.get(self.api_root + '/bank/api/v1/accounts/' + user_id,
                                        headers=self.get_header())

        return json.loads(accounts_request.text)['items']

    def get_account(self, user_id, account_number):
        accounts_request = requests.get(self.api_root + '/bank/api/v1/accounts/' + user_id + '/' + account_number,
                                        headers=self.get_header())

        return json.loads(accounts_request.text)['item']

    def get_transactions(self, user_id, account_number):
        transactions_request = requests.get(
            self.api_root + '/bank/api/v1/transactions/' + user_id + '/' + account_number,
            headers=self.get_header())

        return json.loads(transactions_request.text)['items']

    def transfer(self, user_id, account_to, account_from, amount, message):
        transfer_request = requests.post(
            self.api_root + '/bank/api/v1/transfers/' + user_id,
            json={'fromAccount': account_from, 'toAccount': account_to, 'amount': amount, 'message': message},
            headers=self.get_header())

        return json.loads(transfer_request.text)

    def get_customer(self, user_id):
        accounts_request = requests.get(self.api_root + '/customers/api/v1/customers/' + user_id,
                                        headers=self.get_header())
        print(accounts_request)
        return json.loads(accounts_request.text)['item']
