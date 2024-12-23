# Reference
## Contacts
<details><summary><code>client.contacts.<a href="src/surge/contacts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new Contact object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from surge import Surge

client = Surge(
    surge_account="YOUR_SURGE_ACCOUNT",
    token="YOUR_TOKEN",
)
client.contacts.create(
    first_name="Dominic",
    last_name="Toretto",
    phone_number="+18015551234",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**phone_number:** `str` — The contact's phone number in E.164 format.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The contact's first name.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The contact's last name.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/surge/contacts/client.py">show</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a Contact object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from surge import Surge

client = Surge(
    surge_account="YOUR_SURGE_ACCOUNT",
    token="YOUR_TOKEN",
)
client.contacts.show(
    id="ctc_01j9dy8mdzfn3r0e8x1tbdrdrf",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/surge/contacts/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the specified contact by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from surge import Surge

client = Surge(
    surge_account="YOUR_SURGE_ACCOUNT",
    token="YOUR_TOKEN",
)
client.contacts.update(
    id="ctc_01j9dy8mdzfn3r0e8x1tbdrdrf",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Messages
<details><summary><code>client.messages.<a href="src/surge/messages/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sends a Message.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from surge import (
    AttachmentParams,
    MessageConversationContactParams,
    MessageConversationParams,
    Surge,
)

client = Surge(
    surge_account="YOUR_SURGE_ACCOUNT",
    token="YOUR_TOKEN",
)
client.messages.create(
    attachments=[
        AttachmentParams(
            url="https://toretto.family/coronas.gif",
        )
    ],
    body="Thought you could leave without saying goodbye?",
    conversation=MessageConversationParams(
        contact=MessageConversationContactParams(
            first_name="Dominic",
            id="ctc_01j9dy8mdzfn3r0e8x1tbdrdrf",
            last_name="Toretto",
            phone_number="+18015551234",
        ),
        id="cnv_01j9e0dgmdfkj86c877ws0znae",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation:** `MessageConversationParams` 
    
</dd>
</dl>

<dl>
<dd>

**attachments:** `typing.Optional[typing.Sequence[AttachmentParams]]` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[str]` — The message body.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users
<details><summary><code>client.users.<a href="src/surge/users/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new User object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from surge import Surge

client = Surge(
    surge_account="YOUR_SURGE_ACCOUNT",
    token="YOUR_TOKEN",
)
client.users.create(
    first_name="Brian",
    last_name="O'Conner",
    metadata={"email": "boconner@toretti.family", "user_id": 1234},
    photo_url="https://toretti.family/people/brian.jpg",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**first_name:** `str` — The user's first name.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The user's last name.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Set of key-value pairs that will be stored with the user.
    
</dd>
</dl>

<dl>
<dd>

**photo_url:** `typing.Optional[str]` — URL of a photo to be used as the user's avatar.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/surge/users/client.py">show</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a User object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from surge import Surge

client = Surge(
    surge_account="YOUR_SURGE_ACCOUNT",
    token="YOUR_TOKEN",
)
client.users.show(
    id="usr_01j9dwavghe1ttppewekjjkfrx",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Verifications
<details><summary><code>client.verifications.<a href="src/surge/verifications/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new Verification and sends the code to the given phone number.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from surge import Surge

client = Surge(
    surge_account="YOUR_SURGE_ACCOUNT",
    token="YOUR_TOKEN",
)
client.verifications.create(
    phone_number="+18015551234",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**phone_number:** `str` — The phone number to be verified. In E.164 format.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.verifications.<a href="src/surge/verifications/client.py">check</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Checks the code against a verification.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from surge import Surge

client = Surge(
    surge_account="YOUR_SURGE_ACCOUNT",
    token="YOUR_TOKEN",
)
client.verifications.check(
    id="vfn_01jayh15c2f2xamftg0xpyq1nj",
    code="123456",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` — The Verification code that was received.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

