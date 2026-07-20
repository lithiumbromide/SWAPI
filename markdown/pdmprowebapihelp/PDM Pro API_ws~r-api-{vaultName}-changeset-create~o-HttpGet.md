---
title: "api/{vaultName}/changeset/create (Get)"
project: ""
interface: "r-api-{vaultName}-changeset-create"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-changeset-create~o-HttpGet.html"
---

# api/{vaultName}/changeset/create (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/changeset/create |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Stage Resource Group : api/{vaultName}/changeset/create (Get) |
| --- |

Description

GET: api/{vaultName}/changeset/create Generate changesetId

Gets a changeset ID for the specified vault.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |

Response (application/json, text/json)

Returns the new changeset ID

#### Sample Data

```
1
```

Response (application/xml, text/xml)

Returns the new changeset ID

#### Sample Data

```
<int xmlns="http://schemas.microsoft.com/2003/10/Serialization/">1</int>
```

Example

[Upload SOLIDWORKS Files to PDM Vault.postman_collection.json](Upload%20SOLIDWORKS%20Files%20to%20PDM%20Vault.postman_collection.json)

See Also

[Stage Resource Group](PDM%20Pro%20API_ws~g-ab7aa0c7-6261-4685-9682-f6301732b3ab.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
