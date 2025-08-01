# Accounts

Types:

```python
from surge.types import (
    AccountResponse,
    AttachmentParams,
    ContactRequest,
    ContactResponse,
    UserRequest,
    UserResponse,
    AccountBlastsResponse,
    AccountCampaignsResponse,
    AccountMessagesResponse,
    AccountPhoneNumbersResponse,
    AccountRetrieveStatusResponse,
)
```

Methods:

- <code title="post /accounts">client.accounts.<a href="./src/surge/resources/accounts.py">create</a>(\*\*<a href="src/surge/types/account_create_params.py">params</a>) -> <a href="./src/surge/types/account_response.py">AccountResponse</a></code>
- <code title="patch /accounts/{id}">client.accounts.<a href="./src/surge/resources/accounts.py">update</a>(id, \*\*<a href="src/surge/types/account_update_params.py">params</a>) -> <a href="./src/surge/types/account_response.py">AccountResponse</a></code>
- <code title="post /accounts/{account_id}/blasts">client.accounts.<a href="./src/surge/resources/accounts.py">blasts</a>(account_id, \*\*<a href="src/surge/types/account_blasts_params.py">params</a>) -> <a href="./src/surge/types/account_blasts_response.py">AccountBlastsResponse</a></code>
- <code title="post /accounts/{account_id}/campaigns">client.accounts.<a href="./src/surge/resources/accounts.py">campaigns</a>(account_id, \*\*<a href="src/surge/types/account_campaigns_params.py">params</a>) -> <a href="./src/surge/types/account_campaigns_response.py">AccountCampaignsResponse</a></code>
- <code title="post /accounts/{account_id}/contacts">client.accounts.<a href="./src/surge/resources/accounts.py">contacts</a>(account_id, \*\*<a href="src/surge/types/account_contacts_params.py">params</a>) -> <a href="./src/surge/types/contact_response.py">ContactResponse</a></code>
- <code title="post /accounts/{account_id}/messages">client.accounts.<a href="./src/surge/resources/accounts.py">messages</a>(account_id, \*\*<a href="src/surge/types/account_messages_params.py">params</a>) -> <a href="./src/surge/types/account_messages_response.py">AccountMessagesResponse</a></code>
- <code title="post /accounts/{account_id}/phone_numbers">client.accounts.<a href="./src/surge/resources/accounts.py">phone_numbers</a>(account_id, \*\*<a href="src/surge/types/account_phone_numbers_params.py">params</a>) -> <a href="./src/surge/types/account_phone_numbers_response.py">AccountPhoneNumbersResponse</a></code>
- <code title="get /accounts/{account_id}/status">client.accounts.<a href="./src/surge/resources/accounts.py">retrieve_status</a>(account_id, \*\*<a href="src/surge/types/account_retrieve_status_params.py">params</a>) -> <a href="./src/surge/types/account_retrieve_status_response.py">AccountRetrieveStatusResponse</a></code>
- <code title="post /accounts/{account_id}/users">client.accounts.<a href="./src/surge/resources/accounts.py">users</a>(account_id, \*\*<a href="src/surge/types/account_users_params.py">params</a>) -> <a href="./src/surge/types/user_response.py">UserResponse</a></code>

# Contacts

Methods:

- <code title="get /contacts/{id}">client.contacts.<a href="./src/surge/resources/contacts.py">retrieve</a>(id) -> <a href="./src/surge/types/contact_response.py">ContactResponse</a></code>
- <code title="patch /contacts/{id}">client.contacts.<a href="./src/surge/resources/contacts.py">update</a>(id, \*\*<a href="src/surge/types/contact_update_params.py">params</a>) -> <a href="./src/surge/types/contact_response.py">ContactResponse</a></code>

# Users

Types:

```python
from surge.types import UserCreateTokenResponse
```

Methods:

- <code title="get /users/{id}">client.users.<a href="./src/surge/resources/users.py">retrieve</a>(id) -> <a href="./src/surge/types/user_response.py">UserResponse</a></code>
- <code title="patch /users/{id}">client.users.<a href="./src/surge/resources/users.py">update</a>(id, \*\*<a href="src/surge/types/user_update_params.py">params</a>) -> <a href="./src/surge/types/user_response.py">UserResponse</a></code>
- <code title="post /users/{user_id}/tokens">client.users.<a href="./src/surge/resources/users.py">create_token</a>(user_id, \*\*<a href="src/surge/types/user_create_token_params.py">params</a>) -> <a href="./src/surge/types/user_create_token_response.py">UserCreateTokenResponse</a></code>

# Verifications

Types:

```python
from surge.types import Verification, VerificationCheckResponse
```

Methods:

- <code title="post /verifications">client.verifications.<a href="./src/surge/resources/verifications.py">create</a>(\*\*<a href="src/surge/types/verification_create_params.py">params</a>) -> <a href="./src/surge/types/verification.py">Verification</a></code>
- <code title="post /verifications/{id}/checks">client.verifications.<a href="./src/surge/resources/verifications.py">check</a>(id, \*\*<a href="src/surge/types/verification_check_params.py">params</a>) -> <a href="./src/surge/types/verification_check_response.py">VerificationCheckResponse</a></code>
