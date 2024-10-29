# Zinaripay SDK  
  
Zinaripay SDK is a Python client library designed to simplify integration with the **ZinariPay OpenAPI** [ZinariPay website ](https://pay.zinari.io/). This SDK allows developers to interact seamlessly with various payment functionalities provided by ZinariPay, such as creating payment links, handling transactions, managing wallets, and more.  
  
## Table of Contents  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
  - [Initialization](#initialization)  
  - [Creating a Payment Link](#creating-a-payment-link)  
  - [Creating a Transaction](#creating-a-transaction)  
  - [Retrieving Transaction Status](#retrieving-transaction-status)  
  - [Listing Transactions](#listing-transactions)  
  - [Managing Wallets](#managing-wallets)  
  - [Withdrawing from Wallet](#withdrawing-from-wallet)  
  - [Getting Exchange Rates](#getting-exchange-rates)  
- [Error Handling](#error-handling)  
- [Contributing](#contributing)  
- [License](#license)  
  
## Features  
- Create payment links with custom parameters.  
- Initiate cryptocurrency transactions.  
- Retrieve transaction details by ID.  
- List all transactions.  
- Manage wallet operations.  
- Withdraw funds from wallets.  
- Fetch real-time exchange rates between currencies.  
  
## Installation  
To install the Zinaripay SDK, you need to have Python 3.6 or higher installed. You can install the SDK using pip:  
```bash  
pip install zinaripaysdk  
```  
Alternatively, you can clone the repository and install it locally:  
```bash  
git clone https://github.com/Ramseyxlil/zinaripay-sdk.git  
cd zinaripaysdk  
pip install .  
```  

## Usage  

### Initialization  
To start using the SDK, you need to initialize it with your API key, which you can obtain from your ZinariPay account.  
```python  
from zinaripaysdk import ZinariPaySDK  
  
# Initialize with your API key  
api_key = "your_api_key"  
zinari = ZinariPaySDK(api_key)  
```  

### Creating a Payment Link  
To create a payment link, you can use the `get_payment_link` method. This method requires the fiat amount and the notification email. The response will contain the payment link details.  
```python  
payment_link = zinari.get_payment_link(  
    fiat_amount=80000,  
    notification_email="example@example.com",  
    details={"userId": "2445323", "productId": "PR45346t"},  
    success_redirect_uri="http://localhost:3001",  
    failure_redirect_uri="http://localhost:3001"  
)  
print(payment_link)  # Prints the payment link response details  
```  

### Creating a Transaction  
To initiate a cryptocurrency transaction, use the `create_transaction` method. Provide the cryptocurrency type, fiat amount, and notification email. This method returns a `CreateTransactionResponse` object, containing details of the transaction.  
```python  
transaction = zinari.create_transaction(  
    cryptocurrency="USDT",  
    fiat_amount=15000,  
    notification_email="user@example.com",  
    details={"userId": "lmnopq"}  
)  
  
# Accessing each attribute in the CreateTransactionResponse  
print("Transaction ID:", transaction.id)  
print("Fiat Tax:", transaction.fiat_tax)  
print("Fiat Fee:", transaction.fiat_fee)  
print("Exchange Rate:", transaction.exchange_rate)  
print("Cryptocurrency Tax:", transaction.cryptocurrency_tax)  
print("Cryptocurrency Fee:", transaction.cryptocurrency_fee)  
print("Cryptocurrency:", transaction.cryptocurrency)  
print("Cryptocurrency Amount:", transaction.cryptocurrency_amount)  
print("Fiat Amount:", transaction.fiat_amount)  
print("Fiat Currency:", transaction.fiat_currency)  
print("Status:", transaction.status)  
print("Address:", transaction.address)  
print("Blockchain Confirmations:", transaction.blockchain_confirmations)  

# Using to_dict() to get all attributes in dictionary form
transaction_dict = transaction.to_dict()
print("Transaction as dictionary:", transaction_dict)
```  

### Retrieving Transaction Status  
You can retrieve the status of a transaction by its ID using the `get_transaction_by_id` method, which returns a `Transaction` object with detailed information.  
```python  
transaction_id = "YOUR_TRANSACTION_ID"  
transaction_status = zinari.get_transaction_by_id(transaction_id)  
  
# Accessing each attribute in the Transaction object  
print("Transaction ID:", transaction_status.id)  
print("Unique ID:", transaction_status.unique_id)  
print("Status:", transaction_status.status)  
print("Cryptocurrency Amount:", transaction_status.cryptocurrency_amount)  
print("Cryptocurrency:", transaction_status.cryptocurrency)  
print("Blockchain Confirmations:", transaction_status.blockchain_confirmations)  
print("Amount Received:", transaction_status.amount_received)  
print("Exchange Rate:", transaction_status.exchange_rate)  
print("Type:", transaction_status.type)  
print("Details:", transaction_status.details)  
print("Fiat Amount:", transaction_status.fiat_amount)  
print("Fiat Currency:", transaction_status.fiat_currency)  
print("Blockchain Transaction ID:", transaction_status.blockchain_transaction_id)  
print("Webhook URL Called:", transaction_status.webhook_url_called)  

# Using to_dict() to get all attributes in dictionary form
transaction_dict = transaction_status.to_dict()
print("Transaction as dictionary:", transaction_dict)
```  

### Listing Transactions  
To list transactions, use the `list_transactions` method. You can specify whether to list production or development transactions. This method returns a list of `Transaction` objects.  
```python  
# List production transactions  
transactions = zinari.list_transactions(mode="prod")  
for tx in transactions:  
    print(tx.to_dict())  # Or access each attribute individually as above  
  
# List development transactions  
dev_transactions = zinari.list_transactions(mode="dev")  
for tx in dev_transactions:  
    print(tx.to_dict())  
```  

### Managing Wallets  
You can retrieve all wallets associated with your account using the `get_wallets` method, which returns a list of `Wallet` objects.  
```python  
wallets = zinari.get_wallets()  
for wallet in wallets:  
    print("Wallet ID:", wallet.id)  
    print("Currency:", wallet.currency)  
    print("Amount:", wallet.amount)  
```  
To get details about a specific wallet, use the `get_wallet_by_id` method, which returns a single `Wallet` object.  
```python  
wallet_id = "YOUR_WALLET_ID"  
wallet_details = zinari.get_wallet_by_id(wallet_id)  
  
# Accessing attributes of Wallet  
print("Wallet ID:", wallet_details.id)  
print("Currency:", wallet_details.currency)  
print("Amount:", wallet_details.amount)  
```  

### Withdrawing from Wallet  
To withdraw funds from a wallet, use the `withdraw_from_wallet` method. Provide the wallet ID, amount to withdraw, and destination address. This method returns a `WithdrawResponse` object containing withdrawal details.  
```python  
withdrawal = zinari.withdraw_from_wallet(wallet_id="YOUR_WALLET_ID", amount=100, address="YOUR_CRYPTO_ADDRESS")  
  
# Accessing WithdrawResponse attributes  
print("Transaction ID:", withdrawal.id)  
print("Balance:", withdrawal.balance)  
```  

### Getting Exchange Rates  
To fetch the exchange rate between two currencies, use the `get_exchange_rate` method.  
```python  
exchange_rate = zinari.get_exchange_rate(from_currency="USD", to_currency="EUR")  
print("Exchange Rate:", exchange_rate)  
```  

## Error Handling  
The SDK methods return JSON responses that may contain error messages. Ensure to handle exceptions or check for errors in the response.  
Example of error checking:  
```python  
try:  
    response = zinari.create_transaction(...)  
    if 'error' in response:  
        print(f"Error: {response['error']}")  
except Exception as e:  
    print(f"Exception: {str(e)}")  
```  

## Contributing  
Contributions are always welcome! Follow the steps below to contribute to the Zinaripay SDK:  

### Steps to Contribute  
1. **Fork the Repository**  
   - Go to the [ZinariPay SDK GitHub page](https://github.com/Ramseyxlil/zinaripay-sdk) and click on the “Fork” button to create a copy of the repository in your GitHub account.  

2. **Clone the Forked Repository**  
   - Clone the forked repository from your GitHub account to your local machine:  
     ```bash  
     git clone https://github.com/YOUR_GITHUB_USERNAME/zinaripay-sdk.git  
     cd zinaripay-sdk  
     ```  

3. **Create a New Branch**  
   - It’s recommended to create a new branch for your changes to keep the `main` branch clean:  
     ```bash  
     git checkout -b your-feature-branch  
     ```  

4. **Install Dependencies**  
   - If there are specific dependencies or tools for testing, install them. You can typically do this by running:  
     ```bash  
     pip install -r requirements.txt  
     ```  

5. **Make Your Changes**  
   - Add or improve SDK features, fix bugs, or update documentation.  

6. **Write and Run Tests**  
   - If your changes affect the code, please add appropriate tests in the `tests/` directory. Running tests is essential to ensure the SDK remains stable.  
     ```bash  
     pytest tests/  
     ```  

7. **Commit and Push Your Changes**  
   - Commit your changes with a descriptive message, then push them to your forked repository:  
     ```bash  
     git add .  
     git commit -m "Add your descriptive message here"  
     git push origin your-feature-branch  
     ```  

8. **Create a Pull Request**  
   - Go to the original [ZinariPay SDK GitHub repository](https://github.com/Ramseyxlil/zinaripay-sdk) and click “New pull request.” Select your feature branch, and submit the pull request with a clear explanation of the changes you made.  

### Guidelines for Contributing  
- Ensure your code follows the Python PEP 8 style guide.  
- Test thoroughly with existing tests and any new ones you add.  
- Include docstrings for any new methods and update the documentation as needed.  

The ZinariPay SDK project team will review your pull request. They may ask for some modifications before merging your code into the main branch.  

Happy coding, and thank you for your contributions!  

## License  
This project is licensed under the MIT License. See the LICENSE file for details.
