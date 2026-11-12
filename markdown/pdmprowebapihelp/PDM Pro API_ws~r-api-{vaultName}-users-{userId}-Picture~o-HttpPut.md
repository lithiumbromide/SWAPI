---
title: "api/{vaultName}/users/{userId}/Picture (Put)"
project: ""
interface: "r-api-{vaultName}-users-{userId}-Picture"
member: "o-HttpPut"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-users-{userId}-Picture~o-HttpPut.html"
---

# api/{vaultName}/users/{userId}/Picture (Put)

PDM Pro API Web Service

| Put | api/{vaultName}/users/{userId}/Picture |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > User Resource Group : api/{vaultName}/users/{userId}/Picture (Put) |
| --- |

Description

PUT: api/{VaultName}/users/{UserID}/Picture Put user picture

Saves the picture of the specified user.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| userId | (URI parameter) User ID (required) | integer |

Response (application/json, text/json)

Returns true if picture saved, false if not

#### Sample Data

```
true
```

Response (application/xml, text/xml)

Returns true if picture saved, false if not

#### Sample Data

```
<boolean xmlns="http://schemas.microsoft.com/2003/10/Serialization/">true</boolean>
```

See Also

[User Resource Group](PDM%20Pro%20API_ws~g-09a63486-9278-41ff-970c-d47012e2bea1.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
