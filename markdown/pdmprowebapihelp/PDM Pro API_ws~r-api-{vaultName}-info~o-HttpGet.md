---
title: "api/{vaultName}/info (Get)"
project: ""
interface: "r-api-{vaultName}-info"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-info~o-HttpGet.html"
---

# api/{vaultName}/info (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/info |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Vault Resource Group : api/{vaultName}/info (Get) |
| --- |

Description

GET: api/{VaultName} or api/{VaultName}/info Get vault properties

Gets the properties of the specified vault.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| Version | (Response) Vault version Member of VaultProp model | integer |
| VaultType | (Response) Type of vault Member of VaultProp model | string |
| ArchiveServer | (Response) Archive server Member of VaultProp model | string |
| DatabaseName | (Response) Database name Member of VaultProp model | string |
| DatabaseServer | (Response) Database server Member of VaultProp model | string |
| VaultID | (Response) Vault ID Member of VaultProp model | globally unique identifier |

Response (application/json, text/json)

#### Sample Data

```
{
  "Version": 1,
  "VaultType": "sample string 2",
  "ArchiveServer": "sample string 3",
  "DatabaseName": "sample string 4",
  "DatabaseServer": "sample string 5",
  "VaultID": "e2a87d6d-8f9f-4c1c-a40c-39b81d9f9f56"
}
```

Response (application/xml, text/xml)

#### Sample Data

```
<VaultProp xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <ArchiveServer>sample string 3</ArchiveServer>
  <DatabaseName>sample string 4</DatabaseName>
  <DatabaseServer>sample string 5</DatabaseServer>
  <VaultID>e2a87d6d-8f9f-4c1c-a40c-39b81d9f9f56</VaultID>
  <VaultType>sample string 2</VaultType>
  <Version>1</Version>
</VaultProp>
```

See Also

[Vault Resource Group](PDM%20Pro%20API_ws~g-4e3666da-2867-45a7-a89f-fe7237448857.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
