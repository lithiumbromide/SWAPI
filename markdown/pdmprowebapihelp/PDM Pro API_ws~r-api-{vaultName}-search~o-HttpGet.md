---
title: "api/{vaultName}/search (Get)"
project: ""
interface: "r-api-{vaultName}-search"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-search~o-HttpGet.html"
---

# api/{vaultName}/search (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/search |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > Search Resource Group : api/{vaultName}/search (Get) |
| --- |

Description

Gets objects in the specified vault.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (Required URI parameter) Vault name | string |
| Id | (Response) ID of vault object Member of VaultObject model | integer |
| Type | (Response) An ObjectType; one of: Folder = 0 File = 1 Bom = 3 Member of VaultObject model | ObjectType |

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "Id": 1,
    "Type": 0
  },
  {
    "Id": 1,
    "Type": 0
  }
]
```

Response (application/xml, text/xml)

#### Sample Data

```
<ArrayOfVaultObject xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <VaultObject>
    <Id>1</Id>
    <Type>Folder</Type>
  </VaultObject>
  <VaultObject>
    <Id>1</Id>
    <Type>Folder</Type>
  </VaultObject>
</ArrayOfVaultObject>
```

See Also

[Search Resource Group](PDM%20Pro%20API_ws~g-b95b425f-17d8-44cc-ac84-321dc3026434.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
