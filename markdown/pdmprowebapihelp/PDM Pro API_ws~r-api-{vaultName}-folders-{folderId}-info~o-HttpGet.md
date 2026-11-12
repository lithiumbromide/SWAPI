---
title: "api/{vaultName}/folders/{folderId}/info (Get)"
project: ""
interface: "r-api-{vaultName}-folders-{folderId}-info"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-folders-{folderId}-info~o-HttpGet.html"
---

# api/{vaultName}/folders/{folderId}/info (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/folders/{folderId}/info |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > Folder Resource Group : api/{vaultName}/folders/{folderId}/info (Get) |
| --- |

Description

GET: api/{VaultName}/folders/{FolderID} or api/{VaultName}/folders/{FolderID}/info Get folder info

Gets information for the specified folder.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| folderId | (URI parameter) Folder ID (required) | integer |
| Folder | (Response) A Folder object that consists of: FolderId (integer) FolderPath (string) Member of FolderInfo model | Folder |
| FolderName | (Response) Folder name Member of FolderInfo model | string |
| ParentFolderId | (Response) Parent folder ID Member of FolderInfo model | integer |

Response (application/json, text/json)

#### Sample Data

```
{
  "Folder": {
    "FolderId": 1,
    "FolderPath": "sample string 2"
  },
  "FolderName": "sample string 1",
  "ParentFolderId": 2
}
```

Response (application/xml, text/xml)

#### Sample Data

```
<FolderInfo xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <Folder>
    <FolderId>1</FolderId>
    <FolderPath>sample string 2</FolderPath>
  </Folder>
  <FolderName>sample string 1</FolderName>
  <ParentFolderId>2</ParentFolderId>
</FolderInfo>
```

See Also

[Folder Resource Group](PDM%20Pro%20API_ws~g-ebc7dbbc-e61a-4479-954a-e443044cd655.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
