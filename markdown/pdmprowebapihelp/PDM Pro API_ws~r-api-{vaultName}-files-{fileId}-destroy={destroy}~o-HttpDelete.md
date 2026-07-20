---
title: "api/{vaultName}/files/{fileId}?destroy={destroy} (Delete)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-destroy={destroy}"
member: "o-HttpDelete"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-destroy={destroy}~o-HttpDelete.html"
---

# api/{vaultName}/files/{fileId}?destroy={destroy} (Delete)

PDM Pro API Web Service

| Delete | api/{vaultName}/files/{fileId}?destroy={destroy} |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}?destroy={destroy} (Delete) |
| --- |

Description

Delete file

Deletes the specified file

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| fileId | (URI parameter) File ID (required) | integer |
| destroy | (URI parameter) Whether to delete the file (default value is false) | boolean |
| Id | (Response) ID of object Member of ObjectInfoShort model | integer |
| Name | (Response) Name of object Member of ObjectInfoShort model | string |
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

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
