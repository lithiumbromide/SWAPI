---
title: "api/{vaultName}/search (Post)"
project: ""
interface: "r-api-{vaultName}-search"
member: "o-HttpPost"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-search~o-HttpPost.html"
---

# api/{vaultName}/search (Post)

PDM Pro API Web Service

| Post | api/{vaultName}/search |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > Search Resource Group : api/{vaultName}/search (Post) |
| --- |

Description

Gets objects in the vault that contain the specified string.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (Required URI parameter) Vault name | string |
| Id | (Response) ID of vault object Member of VaultObject model | integer |
| Type | (Response) An ObjectType; one of: Folder = 0 File = 1 Bom = 3 Member of VaultObject model | ObjectType |

Request (application/json, text/json)

Body parameter contains the string to search the vault for

#### Sample Data

```
"sample string 1"
```

Request (application/xml, text/xml)

Body parameter contains the string to search the vault for

#### Sample Data

```
<string xmlns="http://schemas.microsoft.com/2003/10/Serialization/">sample string 1</string>
```

Request (application/x-www-form-urlencoded)

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

Remarks

This operation:

- takes a body parameter that contains the string to search the vault for.
- returns an array of VaultObjects.

See Also

[Search Resource Group](PDM%20Pro%20API_ws~g-b95b425f-17d8-44cc-ac84-321dc3026434.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
