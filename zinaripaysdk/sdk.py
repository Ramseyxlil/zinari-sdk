import requests  
  
class Transaction:  
    def __init__(self, data):  
        self.id = data.get("id")  
        self.unique_id = data.get("uniqueId")  
        self.status = data.get("status")  
        self.cryptocurrency_amount = data.get("cryptocurrencyAmount")  
        self.cryptocurrency = data.get("cryptocurrency")  
        self.blockchain_confirmations = data.get("blockchainConfirmations")  
        self.amount_received = data.get("amountReceived")  
        self.exchange_rate = data.get("exchangeRate")  
        self.type = data.get("type")  
        self.details = data.get("details", {})  
        self.fiat_amount = data.get("fiatAmount")  
        self.fiat_currency = data.get("fiatCurrency")  
        self.blockchain_transaction_id = data.get("blockchainTransactionId")  
        self.webhook_url_called = data.get("webhookUrlCalled")  
  
    def to_dict(self):  
        return {  
            "id": self.id,  
            "uniqueId": self.unique_id,  
            "status": self.status,  
            "cryptocurrencyAmount": self.cryptocurrency_amount,  
            "cryptocurrency": self.cryptocurrency,  
            "blockchainConfirmations": self.blockchain_confirmations,  
            "amountReceived": self.amount_received,  
            "exchangeRate": self.exchange_rate,  
            "type": self.type,  
            "details": self.details,  
            "fiatAmount": self.fiat_amount,  
            "fiatCurrency": self.fiat_currency,  
            "blockchainTransactionId": self.blockchain_transaction_id,  
            "webhookUrlCalled": self.webhook_url_called  
        }  
  
class CreateTransactionResponse:  
    def __init__(self, data):  
        self.id = data.get("id")  
        self.fiat_tax = data.get("fiatTax")  
        self.fiat_fee = data.get("fiatFee")  
        self.exchange_rate = data.get("exchangeRate")  
        self.cryptocurrency_tax = data.get("cryptocurrencyTax")  
        self.cryptocurrency_fee = data.get("cryptocurrencyFee")  
        self.cryptocurrency = data.get("cryptocurrency")  
        self.cryptocurrency_amount = data.get("cryptocurrencyAmount")  
        self.fiat_amount = data.get("fiatAmount")  
        self.fiat_currency = data.get("fiatCurrency")  
        self.status = data.get("status")  
        self.address = data.get("address")  
        self.blockchain_confirmations = data.get("blockchainConfirmations")  
  
    def to_dict(self):  
        return {  
            "id": self.id,  
            "fiatTax": self.fiat_tax,  
            "fiatFee": self.fiat_fee,  
            "exchangeRate": self.exchange_rate,  
            "cryptocurrencyTax": self.cryptocurrency_tax,  
            "cryptocurrencyFee": self.cryptocurrency_fee,  
            "cryptocurrency": self.cryptocurrency,  
            "cryptocurrencyAmount": self.cryptocurrency_amount,  
            "fiatAmount": self.fiat_amount,  
            "fiatCurrency": self.fiat_currency,  
            "status": self.status,  
            "address": self.address,  
            "blockchainConfirmations": self.blockchain_confirmations  
        }  
  
class Wallet:  
    def __init__(self, data):  
        self.id = data.get("id")  
        self.currency = data.get("currency")  
        self.amount = data.get("amount")  
  
    def to_dict(self):  
        return {  
            "id": self.id,  
            "currency": self.currency,  
            "amount": self.amount  
        }  
  
class WithdrawResponse:  
    def __init__(self, data):  
        self.id = data.get("id")  
        self.balance = data.get("balance")  
  
    def to_dict(self):  
        return {  
            "id": self.id,  
            "balance": self.balance  
        }  
  
class ZinariPaySDK:  
    BASE_URL = "https://openapi.zinari.io/v1/"  
  
    def __init__(self, api_key):  
        self.api_key = api_key  
        self.headers = {  
            "Authorization": f"Bearer {self.api_key}",  
            "Content-Type": "application/json"  
        }  
  
    def _post(self, endpoint, data):  
        response = requests.post(self.BASE_URL + endpoint, json=data, headers=self.headers)  
        response.raise_for_status()  
        return response.json()  
  
    def _get(self, endpoint):  
        response = requests.get(self.BASE_URL + endpoint, headers=self.headers)  
        response.raise_for_status()  
        return response.json()  
  
    def get_payment_link(self, fiat_amount, notification_email, details=None, success_redirect_uri=None, failure_redirect_uri=None):  
        data = {  
            "fiatAmount": fiat_amount,  
            "notificationEmailAddress": notification_email,  
            "details": details,  
            "successRedirectUri": success_redirect_uri,  
            "failureRedirectUri": failure_redirect_uri  
        }  
        return self._post("paylink", data)  
  
    def create_transaction(self, cryptocurrency, fiat_amount, notification_email, details=None):  
        data = {  
            "cryptocurrency": cryptocurrency,  
            "fiatAmount": fiat_amount,  
            "notificationEmailAddress": notification_email,  
            "details": details  
        }  
        response = self._post("create-transaction", data)  
        return CreateTransactionResponse(response)  
  
    def get_transaction_by_id(self, transaction_id):  
        response = self._get(f"transaction/{transaction_id}")  
        return Transaction(response)  
  
    def list_transactions(self, mode="prod"):  
        endpoint = "transactions" if mode == "prod" else "transactions/dev"  
        response = self._get(endpoint)  
        return [Transaction(tx) for tx in response.get("data", [])]  
  
    def get_wallets(self):  
        response = self._get("wallets")  
        return [Wallet(wallet) for wallet in response]  
  
    def get_wallet_by_id(self, wallet_id):  
        response = self._get(f"wallet/{wallet_id}")  
        return Wallet(response)  
  
    def withdraw_from_wallet(self, wallet_id, amount, address):  
        data = {  
            "amount": amount,  
            "address": address  
        }  
        response = self._post(f"withdraw/{wallet_id}", data)  
        return WithdrawResponse(response)  
  
    def get_exchange_rate(self, from_currency, to_currency):  
        endpoint = f"exchange-rate?from={from_currency}&to={to_currency}"  
        return self._get(endpoint)  