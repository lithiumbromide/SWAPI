---
title: "api/{vaultName}/folders/{folderId}?destroy={destroy} (Delete)"
project: ""
interface: "r-api-{vaultName}-folders-{folderId}-destroy={destroy}"
member: "o-HttpDelete"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-folders-{folderId}-destroy={destroy}~o-HttpDelete.html"
---

# api/{vaultName}/folders/{folderId}?destroy={destroy} (Delete)

PDM Pro API Web Service

| Delete | api/{vaultName}/folders/{folderId}?destroy={destroy} |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > Folder Resource Group : api/{vaultName}/folders/{folderId}?destroy={destroy} (Delete) |
| --- |

Description

DELETE: api/{VaultName}/folders/{FolderID} Delete folder

Deletes the specified folder.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| folderId | (URI parameter) Folder ID (required) | integer |
| destroy | (URI parameter) Whether to delete the folder (default value is false) | boolean |
| Id | (Response) Deleted folder ID Member of ObjectInfoShort model | integer |
| Name | (Response) Deleted folder name Member of ObjectInfoShort model | string |
| Type | (Response) An ObjectType object; one of: Folder = 0 File = 1 Bom = 3 Member of ObjectInfoShort model | ObjectType |
| Status | (Response) A StatusOperation object; one of: Success = 0 Failure = 1 Member of ObjectInfoShort model | StatusOperation |
| Warning | (Response) A BaseWarningModel object that consists of: Message (string) IsBlocking (boolean) IsError (boolean) Member of ObjectInfoShort model | BaseWarningModel |

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

[Folder Resource Group](PDM%20Pro%20API_ws~g-ebc7dbbc-e61a-4479-954a-e443044cd655.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
