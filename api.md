# Shared Types

```python
from surgeapi.types import Error
```

# Accounts

Types:

```python
from surgeapi.types import (
    Account,
    AccountParams,
    AccountStatus,
    AccountUpdateParams,
    Organization,
    OrganizationParams,
)
```

Methods:

- <code title="post /accounts">client.accounts.<a href="./src/surgeapi/resources/accounts.py">create</a>(\*\*<a href="src/surgeapi/types/account_create_params.py">params</a>) -> <a href="./src/surgeapi/types/account.py">Account</a></code>
- <code title="patch /accounts/{id}">client.accounts.<a href="./src/surgeapi/resources/accounts.py">update</a>(id, \*\*<a href="src/surgeapi/types/account_update_params.py">params</a>) -> <a href="./src/surgeapi/types/account.py">Account</a></code>
- <code title="get /accounts/{account_id}/status">client.accounts.<a href="./src/surgeapi/resources/accounts.py">retrieve_status</a>(account_id, \*\*<a href="src/surgeapi/types/account_retrieve_status_params.py">params</a>) -> <a href="./src/surgeapi/types/account_status.py">AccountStatus</a></code>

# Blasts

Types:

```python
from surgeapi.types import Blast, BlastParams
```

Methods:

- <code title="post /accounts/{account_id}/blasts">client.blasts.<a href="./src/surgeapi/resources/blasts.py">create</a>(account_id, \*\*<a href="src/surgeapi/types/blast_create_params.py">params</a>) -> <a href="./src/surgeapi/types/blast.py">Blast</a></code>

# Campaigns

Types:

```python
from surgeapi.types import Campaign, CampaignParams
```

Methods:

- <code title="post /accounts/{account_id}/campaigns">client.campaigns.<a href="./src/surgeapi/resources/campaigns.py">create</a>(account_id, \*\*<a href="src/surgeapi/types/campaign_create_params.py">params</a>) -> <a href="./src/surgeapi/types/campaign.py">Campaign</a></code>

# Contacts

Types:

```python
from surgeapi.types import Contact, ContactParams
```

Methods:

- <code title="post /accounts/{account_id}/contacts">client.contacts.<a href="./src/surgeapi/resources/contacts.py">create</a>(account_id, \*\*<a href="src/surgeapi/types/contact_create_params.py">params</a>) -> <a href="./src/surgeapi/types/contact.py">Contact</a></code>
- <code title="get /contacts/{id}">client.contacts.<a href="./src/surgeapi/resources/contacts.py">retrieve</a>(id) -> <a href="./src/surgeapi/types/contact.py">Contact</a></code>
- <code title="patch /contacts/{id}">client.contacts.<a href="./src/surgeapi/resources/contacts.py">update</a>(id, \*\*<a href="src/surgeapi/types/contact_update_params.py">params</a>) -> <a href="./src/surgeapi/types/contact.py">Contact</a></code>

# Messages

Types:

```python
from surgeapi.types import AttachmentParams, Message, MessageParams
```

Methods:

- <code title="post /accounts/{account_id}/messages">client.messages.<a href="./src/surgeapi/resources/messages.py">create</a>(account_id, \*\*<a href="src/surgeapi/types/message_create_params.py">params</a>) -> <a href="./src/surgeapi/types/message.py">Message</a></code>

# PhoneNumbers

Types:

```python
from surgeapi.types import PhoneNumber, PhoneNumberPurchaseParams
```

Methods:

- <code title="post /accounts/{account_id}/phone_numbers">client.phone_numbers.<a href="./src/surgeapi/resources/phone_numbers.py">purchase</a>(account_id, \*\*<a href="src/surgeapi/types/phone_number_purchase_params.py">params</a>) -> <a href="./src/surgeapi/types/phone_number.py">PhoneNumber</a></code>

# Users

Types:

```python
from surgeapi.types import User, UserParams, UserTokenParams, UserTokenResponse
```

Methods:

- <code title="post /accounts/{account_id}/users">client.users.<a href="./src/surgeapi/resources/users.py">create</a>(account_id, \*\*<a href="src/surgeapi/types/user_create_params.py">params</a>) -> <a href="./src/surgeapi/types/user.py">User</a></code>
- <code title="get /users/{id}">client.users.<a href="./src/surgeapi/resources/users.py">retrieve</a>(id) -> <a href="./src/surgeapi/types/user.py">User</a></code>
- <code title="patch /users/{id}">client.users.<a href="./src/surgeapi/resources/users.py">update</a>(id, \*\*<a href="src/surgeapi/types/user_update_params.py">params</a>) -> <a href="./src/surgeapi/types/user.py">User</a></code>
- <code title="post /users/{user_id}/tokens">client.users.<a href="./src/surgeapi/resources/users.py">create_token</a>(user_id, \*\*<a href="src/surgeapi/types/user_create_token_params.py">params</a>) -> <a href="./src/surgeapi/types/user_token_response.py">UserTokenResponse</a></code>

# Verifications

Types:

```python
from surgeapi.types import (
    Verification,
    VerificationCheck,
    VerificationCheckParams,
    VerificationParams,
)
```

Methods:

- <code title="post /verifications">client.verifications.<a href="./src/surgeapi/resources/verifications.py">create</a>(\*\*<a href="src/surgeapi/types/verification_create_params.py">params</a>) -> <a href="./src/surgeapi/types/verification.py">Verification</a></code>
- <code title="post /verifications/{id}/checks">client.verifications.<a href="./src/surgeapi/resources/verifications.py">check</a>(id, \*\*<a href="src/surgeapi/types/verification_check_params.py">params</a>) -> <a href="./src/surgeapi/types/verification_check.py">VerificationCheck</a></code>
