---
title: "api/{vaultName}/progress/{guid}/result (Get)"
project: ""
interface: "r-api-{vaultName}-progress-{guid}-result"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-progress-{guid}-result~o-HttpGet.html"
---

# api/{vaultName}/progress/{guid}/result (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/progress/{guid}/result |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Progress Resource Group : api/{vaultName}/progress/{guid}/result (Get) |
| --- |

Description

GET: api/{vaultName}/progress/{guid}/result

Gets the result of the specified operation.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| guid | (URI parameter) Operation GUID (required) (see Remarks ) | string |

Response (application/json, text/json)

#### Sample Data

```
{}
```

Response (application/xml, text/xml)

#### Sample Data

```
<z:anyType xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns:z="http://schemas.microsoft.com/2003/10/Serialization/" />
```

Example

[Upload SOLIDWORKS Files to PDM Vault.postman_collection.json](Upload%20SOLIDWORKS%20Files%20to%20PDM%20Vault.postman_collection.json)

|

[Check in SOLIDWORKS Files in PDM Vault.postman_collection.json](Check%20in%20SOLIDWORKS%20Files%20%20in%20PDM%20Vault.postman_collection.json)

Remarks

The operation GUID can be found in the response of

[api/{vaultName}/files/{changesetId}/finishadd (Put)](PDM%20Pro%20API_ws~r-api-{vaultName}-files-{changesetId}-finishadd~o-HttpPut.html)

.

See Also

[Progress Resource Group](PDM%20Pro%20API_ws~g-41efefa2-70af-440a-a06e-5d7156c5dc19.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
