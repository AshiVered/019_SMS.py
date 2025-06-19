# 019_SMS.py


This repository provides a basic example of how to use the 019 Mobile (Israeli cellular provider) SMS API with Python.

## Setup Instructions

### 1. Obtain Your API Token

Edit the `GetToken.py` file and enter your credentials (e.g., username, password, and company ID).  
Then run the script to retrieve your access token.

A valid token will look something like this:  
eyJ0eXAiOiJqd3QiLCJhbGci5iJIUzI1NiJ9.eyJmaXJzdF9rZXkiOiI0NzAiLCJzZWNvbmRfa2V5IjoiOTQ1MjUiLCJpc3N1ZQRBdCI6IjE5LTA2LTIwMjUgMTY6NDI6SDMiLCJ0dGwiOjYzMDcyMDAwfQ.EJycTcLkEKPxaPVgGNGmxeEBo1BKbf6kxS-No8ICKk1

### 2. Send an SMS

Edit the `SendSMS.py` file and fill in the required fields, such as the destination number, message content, and the token you received in step 1.  
Then run the script to send your message.

## Full API Documentation

For detailed information on the API, refer to the official documentation:  
[https://docs.019sms.co.il/sms/](https://docs.019sms.co.il/sms/)


