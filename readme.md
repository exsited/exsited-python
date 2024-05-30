# Exsited Python SDK
The Exsited Python SDK provides an easy-to-use library for integrating Exsited services into your project. This includes Custom Integration, Onsite Integration and all APIs.

***
## Table of Contents
- [Requirements](#Requirements)
- [Installation](#Installation)
- [Configuration](#Configuration)
- [Authentication](#Authentication)
- [Getting Started](#Getting-Started)
- [Testing](#Testing)
- [API Documentation](#API-Documentation)
# Requirements
Python 3.12 and Later

# Installation
```bash
# Install virtualenv
pip install virtualenv

# Create Virtual Environment
python -m venv venv

# Active virtual Environment from windows
venv\Scripts\activate

# Upgrade the pip
python -m pip install --upgrade pip


# Install setup tools
pip install setuptools

# Install app Dependency
pip install -e .
```


# Configuration

To set up the Exsited SDK, you'll require your `Client ID`, `Client Secret`, and `Redirect URL`. If you have not received these details already, please reach out to your designated client contact to obtain them



# Authentication
1. **Locate `common_data.py`:** Open the SKD project directory on an IDE and navigate to the `common_data.py` file which is located in the following path: `tests/common/common_data.py`.
2. **Update `get_request_token_dto` function:** Within the `common_data.py` class, locate the method named `get_request_token_dto` and update it with the credentials you were provided.
<img src="blob:https://webalive.atlassian.net/c058a466-42ce-405e-b3ca-dfbbb81a9939#media-blob-url=true&id=ee9aff06-3e79-4823-b0bf-9ef83f5d3c9a&collection=contentId-558825510&contextId=558825510&mimeType=image%2Fpng&name=image.png&size=435487&width=2049&height=922&alt=image.png" alt="">

3. **Provide Credential Values:** Populate the mandatory fields (`clientId`, `clientSecret`, `redirectUri`, and `ExsitedUrl`) within the `RequestTokenDTO` object. However, **replace the placeholder values**  in the following code block with your actual credentials:

### Code Example:
```python
def get_request_token_dto():
    return RequestTokenDTO(
        grantType="client_credentials",
        clientId="[YOUR_CLIENT_ID]",  # Replace with your actual Client ID
        clientSecret="[YOUR_CLIENT_SECRET]",  # Replace with your actual Client Secret
        redirectUri="[YOUR_REDIRECT_URI]",  # Replace with your actual Redirect URL
        ExsitedUrl="[YOUR_EXSITED_SERVER_URL]" # Replace with your Exsited server URL, 
    )
 ```
### Credentials Table
| Key          | value                     | 
|--------------|---------------------------|
| clientId     | "[YOUR_CLIENT_ID]"        | 
| clientSecret | "[YOUR_CLIENT_SECRET]"    | 
| redirectUri  | "YOUR_REDIRECT_URI"       | 
| ExsitedUrl   | [YOUR_EXSITED_SERVER_URL] | 

# Getting Started
Follow the common pattern to test the functions on the SDK. All the tests can be done on the test files located in the Tests directory.

### Testing SDK Functions

### Method: `test_account_create_basic`
***

### Request Parameters

| Parameter       | Description                                             | Type             | Required |
|-----------------|---------------------------------------------------------|------------------|----------|
| account         | Contains the account details to be created.             | `AccountDataDTO` | Yes      |
| account.name    | The name of the account.                                | `str`            | Yes      |
| account.emailAddress | The email address associated with the account.     | `str`            | Yes      |

### Example Request Data (JSON Representation)

```json
{
  "account": {
    "name": "Example Name",
    "emailAddress": "example@example.com"
  }
}
```
### Function Signature
```Python
def test_account_create_basic():
    SDKConfig.PRINT_REQUEST_DATA = False
    SDKConfig.PRINT_RAW_RESPONSE = False

    autobill_sdk: AutoBillSDK = AutoBillSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        # You will edit the following request_data
        request_data = AccountCreateDTO(account=AccountDataDTO(name="Example Name", emailAddress="example@example.com"))
        
        response = autobill_sdk.account.create(request_data=request_data)
        print(response)
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)
```

### Method: `test_order_create_basic`
***
| Parameter  | Description                                 | Type | Required |
|------------|---------------------------------------------|------|----------|
| accountId  | The ID of the account associated with the order. | str  | Yes      |
| item_id    | The ID of the item being ordered.           | str  | Yes      |
| quantity   | The quantity of the item being ordered.     | str  | Yes      |

```json
{
  "order": {
    "accountId": "30PS79",
    "lines": [
      {
        "item_id": "ITEM-0055",
        "quantity": "1"
      }
    ]
  }
}
```
### Function Signature
```Python
def test_order_create_basic():
    SDKConfig.PRINT_REQUEST_DATA = True
    SDKConfig.PRINT_RAW_RESPONSE = False

    autobill_sdk = AutoBillSDK().init_sdk(request_token_dto=CommonData.get_request_token_dto())

    try:
        # You will edit the following request_data
        request_data = OrderCreateDTO(order=OrderDataDTO(accountId="30PS79").add_line(item_id="ITEM-0055", quantity="1"))
        response = autobill_sdk.order.create(request_data=request_data)
        print(response)
        
    except ABException as ab:
        print(ab)
        print(ab.get_errors())
        print(ab.raw_response)

```
***
### Response
| Field    | Description                                                 |
|----------|-------------------------------------------------------------|
| response | The response from the the method being called.              |
| errors   | Any errors encountered during the account creation process. |

### Error Handling
| Field           | Description                                             |
|-----------------|---------------------------------------------------------|
| ab              | The exception object.                                   |
| ab.get_errors() | A list of errors that occurred during the account creation process. |
| ab.raw_response | The raw response data from the API call, useful for debugging. |

# Testing
### Executing Functions
To test the SDK functions, adhere to the common pattern outlined below. All tests should be conducted using the provided test files located in the "Tests" directory.

1. Set up the environment: Ensure that the SDK configuration is appropriately initialized for testing purposes.

2. Customize request data: Adjust the `request_data` as needed for the specific function being tested.

3. Execute the function: Call the desired function from the SDK, updating the `request_data` inside the function body.

### Required Fields
Check out the following documentation to find details on the DTO classes. 

[DTO Classes Documentation](https://webalive.atlassian.net/wiki/spaces/~61ad8c41744c4d006959553f/pages/560889859/DTO+classes)
### Account

| Function Name                     | Required Fields                |
|-----------------------------------|--------------------------------|
| test_account_create_basic        | name, emailAddress            |
| test_account_update_info         | id (Account ID)               |
| test_account_list_basic          | n/a                            |
| test_account_details             | id (Account ID)               |
| test_account_delete              | id (Account ID)               |
| test_account_payment_methods_add | processorType, default, paymentProcessor, reference |
| test_account_payment_card_methods_add | processorType, default, paymentProcessor, reference, cardType, token, cardNumber, expiryMonth, expiryYear |
| test_list_payment_methods        | account_id (Account ID)       |
| test_delete_payment_methods      | account_id (Account ID), reference |
| test_payment_method_details      | account_id (Account ID), reference |

### Order 
| Function                   | Required Parameters               |
|----------------------------|-----------------------------------|
| test_order_create_basic   | accountId, item_id, quantity (Item Quantity) |
| test_order_list_basic     | n/a                               |
| test_order_details        | id (Order ID)                     |
| test_order_cancel         | id (Order ID), effective_date     |
| test_order_usage_add      | chargeItemUuid, chargingPeriod, quantity, startTime, endTime, type |


### Invoice 
| Function              | Required Parameters |
|-----------------------|----------------------|
| test_invoice_list    | n/a                  |
| test_invoice_details | id                   |

# API Documentation
