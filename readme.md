# AutoBill Python SDK

Please find the document inside the docs directory.

# Exsited SDK
[![PyPI version]]()
[![Github forks]]()
[![Github stars]]()
[![Downloads()]]()


Supercharge your apps with AutoBill! Our developer-friendly SDK unlocks the power of AutoBill in your Python code and helps you build stellar applications with features like automated billing, customer management, and payments.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Authentication](#authentication)
- [Usage Examples](#usage-examples)
- [Helper Methods](#helper-methods)
- [API Documentation](#api-documentation)



## Installation

To install this SDK in your project:
<pre><code> # pip install exsited-python </code></pre>


## Configuration

To configure the Exsited SDK, you'll need to retrieve your Client ID, Client Secret, and Redirect URL from your Autobill System. Here's a step-by-step guide:

1. **Log in to Application:** Access your <a href="https://app-stage.exsited.com/">Autobill System</a> using your valid email and password.
<img src="blob:https://webalive.atlassian.net/ed942f83-c477-499f-ae7e-78f09677d5b0#media-blob-url=true&id=5fd9bc92-b8a9-4f3d-b160-a37a6b914250&collection=contentId-558825510&contextId=558825510&mimeType=image%2Fpng&name=AutobillPng.png&size=68060&width=975&height=455&alt=AutobillPng.png" alt="">
2. **Navigate to Applications Settings:** Upon successful login, proceed to the Dashboard section. Locate and click on "Settings" from the top navigation bar.
<img src="blob:https://webalive.atlassian.net/9d5f54e5-a718-40e3-97a7-df89499f8239#media-blob-url=true&id=92f7e299-4540-4aea-9ebf-751ac5e04b94&collection=contentId-558825510&contextId=558825510&width=1897&height=889&alt=image-20240529-063757.png" alt="">
3. **Search and Select Application:** In the top left corner search bar, enter "App" and select "Applications" from the displayed options.
<img src="blob:https://webalive.atlassian.net/217a4a45-558f-40ec-8e58-388c34d7781f#media-blob-url=true&id=327fb53b-4348-48a0-b8ec-a020f35b8df1&collection=contentId-558825510&contextId=558825510&width=1872&height=782&alt=image-20240529-064056.png" alt="">
4. **Locate and Copy Credentials:** From the application list, choose the desired application. Hover over the "Name" field and click on it. A popup window will appear, providing your required credentials: Client ID, Client Secret, and Redirect URL.
<img src="blob:https://webalive.atlassian.net/1a7fed14-ba3b-4d9b-a0d6-fe58c961e866#media-blob-url=true&id=83e2d392-ed92-4e5b-afe2-02b6aa0083d2&collection=contentId-558825510&contextId=558825510&width=1902&height=1023&alt=image-20240529-064610.png" alt="">
5. **Close the Popup:** Once you've copied the credentials, click the "Close" button or "X" icon to dismiss the popup.
<img src="blob:https://webalive.atlassian.net/331cd837-f2a1-489d-97ee-0864dcd11e16#media-blob-url=true&id=37cf2cab-9b12-4bb7-805f-72c6b3e715fe&collection=contentId-558825510&contextId=558825510&width=802&height=669&alt=image-20240529-064738.png" alt="">


## Authentication

Now that you have the necessary credentials, you can configure authentication within the Exsited SDK:

1. **Locate `common_data.py`:** Open your project/SDK in an IDE and navigate to the `common_data.py` class using the following path: `tests/common/common_data.py`.
2. **Identify `get_request_token_dto` Method:** Within the `common_data.py` class, locate the method named `get_request_token_dto`.
<img src="blob:https://webalive.atlassian.net/c058a466-42ce-405e-b3ca-dfbbb81a9939#media-blob-url=true&id=ee9aff06-3e79-4823-b0bf-9ef83f5d3c9a&collection=contentId-558825510&contextId=558825510&mimeType=image%2Fpng&name=image.png&size=435487&width=2049&height=922&alt=image.png" alt="">

3. **Provide Credential Values:** Populate the mandatory fields (`grantType`, `clientId`, `clientSecret`, `redirectUri`, and `autoBillUrl`) within the `RequestTokenDTO` object. However, **replace the placeholder values**  in the following code block with your actual credentials:


```python
def get_request_token_dto():
    return RequestTokenDTO(
        grantType="client_credentials",
        clientId="[YOUR_CLIENT_ID]",  # Replace with your actual Client ID
        clientSecret="[YOUR_CLIENT_SECRET]",  # Replace with your actual Client Secret
        redirectUri="[YOUR_REDIRECT_URI]",  # Replace with your actual Redirect URL
        autoBillUrl="[https://api-stage.exsited.com]" # Replace with your Exsited server URL, 
    )
   ```
| key          | value                        | description               |
|--------------|------------------------------|---------------------------|
| grantType    | "client_credentials"         | Description of grantType  |
| clientId     | "[YOUR_CLIENT_ID]"           | Description of clientId   |
| clientSecret | "[YOUR_CLIENT_SECRET]"       | Description of clientSecret |
| redirectUri  | "YOUR_REDIRECT_URI"          | Description of redirectUri |
| autoBillUrl  | ["https://api-stage.exsited.com"] | Description of autoBillUrl |



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
