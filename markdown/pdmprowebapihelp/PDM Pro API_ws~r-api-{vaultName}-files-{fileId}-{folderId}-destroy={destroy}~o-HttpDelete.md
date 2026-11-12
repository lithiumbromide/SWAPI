---
title: "api/{vaultName}/files/{fileId}/{folderId}?destroy={destroy} (Delete)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-{folderId}-destroy={destroy}"
member: "o-HttpDelete"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-{folderId}-destroy={destroy}~o-HttpDelete.html"
---

# api/{vaultName}/files/{fileId}/{folderId}?destroy={destroy} (Delete)

PDM Pro API Web Service

| Delete | api/{vaultName}/files/{fileId}/{folderId}?destroy={destroy} |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}/{folderId}?destroy={destroy} (Delete) |
| --- |

Description

Deletes the specified file.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (Required URI parameter) Vault name | string |
| fileId | (Required URI parameter) File ID | integer |
| folderId | (URI parameter) Folder ID; default is 0 | integer |
| destroy | (URI parameter) True to destroy, false to not | boolean |
| Id | (Response parameter) File type: Folder = 0 File = 1 Bom = 3 (Member of ObjectInfoShort Model) | integer |
| Name | (Response parameter) File name | string |
| Type | (Response parameter) File type Folder = 0 File = 1 Bom = 3 | ObjectType |
| Status | (Response parameter) Status code: Success = 0 Failure = 1 (Member of ObjectInfoShort Model) | StatusOperation |
| Warning | (Response parameter) Warning: Message: string IsBlocking: boolean IsError: boolean (Member of ObjectInfoShort Model) | BaseWarningModel |

Response (application/json, text/json)

#### Sample Data

```
{
  "Id": 1,
  "Name": "sample string 2",
  "Type": 0,
  "Status": 0,
  "Warning": null
}
```

Response (application/xml, text/xml)

#### Sample Data

```
<ObjectInfoShort xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <Id>1</Id>
  <Name>sample string 2</Name>
  <Status>Success</Status>
  <Type>Folder</Type>
  <Warning i:nil="true" />
</ObjectInfoShort>
```

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
