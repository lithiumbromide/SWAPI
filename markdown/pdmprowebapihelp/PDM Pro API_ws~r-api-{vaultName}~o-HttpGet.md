---
title: "api/{vaultName} (Get)"
project: ""
interface: "r-api-{vaultName}"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}~o-HttpGet.html"
---

# api/{vaultName} (Get)

PDM Pro API Web Service

| Get | api/{vaultName} |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Vault Resource Group : api/{vaultName} (Get) |
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
  "VaultID": "1008dbe9-546b-4727-9f5d-08dabf9a226e"
}
```

Response (application/xml, text/xml)

#### Sample Data

```
<VaultProp xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <ArchiveServer>sample string 3</ArchiveServer>
  <DatabaseName>sample string 4</DatabaseName>
  <DatabaseServer>sample string 5</DatabaseServer>
  <VaultID>1008dbe9-546b-4727-9f5d-08dabf9a226e</VaultID>
  <VaultType>sample string 2</VaultType>
  <Version>1</Version>
</VaultProp>
```

See Also

[Vault Resource Group](PDM%20Pro%20API_ws~g-4e3666da-2867-45a7-a89f-fe7237448857.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
