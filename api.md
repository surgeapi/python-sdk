# Accounts

Types:

```python
from surgeapi.types import AccountStatus, AccountCreateResponse, AccountUpdateResponse
```

Methods:

- <code title="post /accounts">client.accounts.<a href="./src/surgeapi/resources/accounts.py">create</a>(\*\*<a href="src/surgeapi/types/account_create_params.py">params</a>) -> <a href="./src/surgeapi/types/account_create_response.py">AccountCreateResponse</a></code>
- <code title="patch /accounts/{id}">client.accounts.<a href="./src/surgeapi/resources/accounts.py">update</a>(id, \*\*<a href="src/surgeapi/types/account_update_params.py">params</a>) -> <a href="./src/surgeapi/types/account_update_response.py">AccountUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/status">client.accounts.<a href="./src/surgeapi/resources/accounts.py">check_status</a>(account_id, \*\*<a href="src/surgeapi/types/account_check_status_params.py">params</a>) -> <a href="./src/surgeapi/types/account_status.py">AccountStatus</a></code>

# Blasts

Types:

```python
from surgeapi.types import BlastBlastsResponse
```

Methods:

- <code title="post /accounts/{account_id}/blasts">client.blasts.<a href="./src/surgeapi/resources/blasts.py">blasts</a>(account_id, \*\*<a href="src/surgeapi/types/blast_blasts_params.py">params</a>) -> <a href="./src/surgeapi/types/blast_blasts_response.py">BlastBlastsResponse</a></code>

# Campaigns

Types:

```python
from surgeapi.types import Campaign
```

Methods:

- <code title="post /accounts/{account_id}/campaigns">client.campaigns.<a href="./src/surgeapi/resources/campaigns.py">campaigns</a>(account_id, \*\*<a href="src/surgeapi/types/campaign_campaigns_params.py">params</a>) -> <a href="./src/surgeapi/types/campaign.py">Campaign</a></code>

# Contacts

Types:

```python
from surgeapi.types import (
    Contact,
    ContactCreateResponse,
    ContactRetrieveResponse,
    ContactUpdateResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/contacts">client.contacts.<a href="./src/surgeapi/resources/contacts.py">create</a>(account_id, \*\*<a href="src/surgeapi/types/contact_create_params.py">params</a>) -> <a href="./src/surgeapi/types/contact_create_response.py">ContactCreateResponse</a></code>
- <code title="get /contacts/{id}">client.contacts.<a href="./src/surgeapi/resources/contacts.py">retrieve</a>(id) -> <a href="./src/surgeapi/types/contact_retrieve_response.py">ContactRetrieveResponse</a></code>
- <code title="patch /contacts/{id}">client.contacts.<a href="./src/surgeapi/resources/contacts.py">update</a>(id, \*\*<a href="src/surgeapi/types/contact_update_params.py">params</a>) -> <a href="./src/surgeapi/types/contact_update_response.py">ContactUpdateResponse</a></code>

# Messages

Types:

```python
from surgeapi.types import MessageSendResponse
```

Methods:

- <code title="post /accounts/{account_id}/messages">client.messages.<a href="./src/surgeapi/resources/messages.py">send</a>(account_id, \*\*<a href="src/surgeapi/types/message_send_params.py">params</a>) -> <a href="./src/surgeapi/types/message_send_response.py">MessageSendResponse</a></code>

# PhoneNumbers

Types:

```python
from surgeapi.types import PhoneNumber
```

Methods:

- <code title="post /accounts/{account_id}/phone_numbers">client.phone_numbers.<a href="./src/surgeapi/resources/phone_numbers.py">create</a>(account_id, \*\*<a href="src/surgeapi/types/phone_number_create_params.py">params</a>) -> <a href="./src/surgeapi/types/phone_number.py">PhoneNumber</a></code>

# Tokens

Types:

```python
from surgeapi.types import TokenCreateTokenResponse
```

Methods:

- <code title="post /users/{user_id}/tokens">client.tokens.<a href="./src/surgeapi/resources/tokens.py">create_token</a>(user_id, \*\*<a href="src/surgeapi/types/token_create_token_params.py">params</a>) -> <a href="./src/surgeapi/types/token_create_token_response.py">TokenCreateTokenResponse</a></code>

# Users

Types:

```python
from surgeapi.types import UserRetrieveResponse, UserUpdateResponse, UserUsersResponse
```

Methods:

- <code title="get /users/{id}">client.users.<a href="./src/surgeapi/resources/users.py">retrieve</a>(id) -> <a href="./src/surgeapi/types/user_retrieve_response.py">UserRetrieveResponse</a></code>
- <code title="patch /users/{id}">client.users.<a href="./src/surgeapi/resources/users.py">update</a>(id, \*\*<a href="src/surgeapi/types/user_update_params.py">params</a>) -> <a href="./src/surgeapi/types/user_update_response.py">UserUpdateResponse</a></code>
- <code title="post /accounts/{account_id}/users">client.users.<a href="./src/surgeapi/resources/users.py">users</a>(account_id, \*\*<a href="src/surgeapi/types/user_users_params.py">params</a>) -> <a href="./src/surgeapi/types/user_users_response.py">UserUsersResponse</a></code>

# Verifications

Types:

```python
from surgeapi.types import Verification, VerificationCheckResponse
```

Methods:

- <code title="post /verifications">client.verifications.<a href="./src/surgeapi/resources/verifications.py">create</a>(\*\*<a href="src/surgeapi/types/verification_create_params.py">params</a>) -> <a href="./src/surgeapi/types/verification.py">Verification</a></code>
- <code title="post /verifications/{id}/checks">client.verifications.<a href="./src/surgeapi/resources/verifications.py">check</a>(id, \*\*<a href="src/surgeapi/types/verification_check_params.py">params</a>) -> <a href="./src/surgeapi/types/verification_check_response.py">VerificationCheckResponse</a></code>
