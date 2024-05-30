# Exsited Python SDK

Please find the document inside the docs directory.

# Exsited SDK

The Exsited Python SDK provides an easy-to-use library for integrating Exsited services into your project. This includes Custom Integration, Onsite Integration and all APIs.
## Requirements
Python 3.12 and Later

## Create virtual environment & Required Dependency
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


## Configuration

To set up the Exsited SDK, you'll require your `Client ID`, `Client Secret`, and `Redirect URL`. If you have not received these details already, please reach out to your designated client contact to obtain them



## Authentication
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

## Getting Started

**Method:** `test_account_create_basic`

**DTO:** `AccountCreateDTO`

**Steps:**


1 **Create `AccountCreateDTO` Object:** Create an instance of the `AccountCreateDTO` class and populate its mandatory fields using the `AccountDataDTO` object.

    - **Mandatory Fields:**
        - `name`: Set the name of the account (e.g., "Python SDK")
        - `emailAddress`: Set the email address for the account (e.g., "a26@bfei.net")


**Code Example:**

```
Code
```
