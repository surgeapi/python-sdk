# Shared Types

```python
from surgeapi.types import AttachmentParams, Contact
```

# Accounts

Types:

```python
from surgeapi.types import AccountCreateResponse
```

Methods:

- <code title="post /accounts">client.accounts.<a href="./src/surgeapi/resources/accounts.py">create</a>(\*\*<a href="src/surgeapi/types/account_create_params.py">params</a>) -> <a href="./src/surgeapi/types/account_create_response.py">AccountCreateResponse</a></code>

# Blasts

Types:

```python
from surgeapi.types import BlastCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/blasts">client.blasts.<a href="./src/surgeapi/resources/blasts.py">create</a>(account_id, \*\*<a href="src/surgeapi/types/blast_create_params.py">params</a>) -> <a href="./src/surgeapi/types/blast_create_response.py">BlastCreateResponse</a></code>

# Contacts

Types:

```python
from surgeapi.types import ContactCreateResponse, ContactRetrieveResponse
```

Methods:

- <code title="post /accounts/{account_id}/contacts">client.contacts.<a href="./src/surgeapi/resources/contacts.py">create</a>(account_id, \*\*<a href="src/surgeapi/types/contact_create_params.py">params</a>) -> <a href="./src/surgeapi/types/contact_create_response.py">ContactCreateResponse</a></code>
- <code title="get /contacts/{id}">client.contacts.<a href="./src/surgeapi/resources/contacts.py">retrieve</a>(id) -> <a href="./src/surgeapi/types/contact_retrieve_response.py">ContactRetrieveResponse</a></code>

# Messages

Types:

```python
from surgeapi.types import MessageCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/messages">client.messages.<a href="./src/surgeapi/resources/messages.py">create</a>(account_id, \*\*<a href="src/surgeapi/types/message_create_params.py">params</a>) -> <a href="./src/surgeapi/types/message_create_response.py">MessageCreateResponse</a></code>

# Users

Types:

```python
from surgeapi.types import UserCreateResponse, UserRetrieveResponse
```

Methods:

- <code title="post /accounts/{account_id}/users">client.users.<a href="./src/surgeapi/resources/users.py">create</a>(account_id, \*\*<a href="src/surgeapi/types/user_create_params.py">params</a>) -> <a href="./src/surgeapi/types/user_create_response.py">UserCreateResponse</a></code>
- <code title="get /users/{id}">client.users.<a href="./src/surgeapi/resources/users.py">retrieve</a>(id) -> <a href="./src/surgeapi/types/user_retrieve_response.py">UserRetrieveResponse</a></code>

# Verifications

Types:

```python
from surgeapi.types import Verification, VerificationCheckResponse
```

Methods:

- <code title="post /verifications">client.verifications.<a href="./src/surgeapi/resources/verifications.py">create</a>(\*\*<a href="src/surgeapi/types/verification_create_params.py">params</a>) -> <a href="./src/surgeapi/types/verification.py">Verification</a></code>
- <code title="post /verifications/{id}/checks">client.verifications.<a href="./src/surgeapi/resources/verifications.py">check</a>(id, \*\*<a href="src/surgeapi/types/verification_check_params.py">params</a>) -> <a href="./src/surgeapi/types/verification_check_response.py">VerificationCheckResponse</a></code>
