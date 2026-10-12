---
title: "api/{vaultName}/folders/{parentFolderId} (Put)"
project: ""
interface: "r-api-{vaultName}-folders-{parentFolderId}"
member: "o-HttpPut"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-folders-{parentFolderId}~o-HttpPut.html"
---

# api/{vaultName}/folders/{parentFolderId} (Put)

PDM Pro API Web Service

| Put | api/{vaultName}/folders/{parentFolderId} |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > Folder Resource Group : api/{vaultName}/folders/{parentFolderId} (Put) |
| --- |

Description

PUT: api/{VaultName}/folders/{ParentFolderID} Add folder

Adds a folder to the specified folder.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| parentFolderId | (URI parameter) Parent folder ID (required) | integer |
| Id | (Response) Created folder ID Member of ObjectInfoShort model | integer |
| Name | (Response) Created folder name Member of ObjectInfoShort model | string |
| Type | (Response) An ObjectType object; one of: Folder = 0 File = 1 Bom = 3 Member of ObjectInfoShort model | ObjectType |
| Status | (Response) A StatusOperation object; one of: Success = 0 Failure = 1 Member of ObjectInfoShort model | StatusOperation |
| Warning | (Response) A BaseWarningModel object that consists of: Message (string) IsBlocking (boolean) IsError (boolean) Member of ObjectInfoShort model | BaseWarningModel |

Request (application/json, text/json)

#### Sample Data

```
"sample string 1"
```

Request (application/xml, text/xml)

#### Sample Data

```
<string xmlns="http://schemas.microsoft.com/2003/10/Serialization/">sample string 1</string>
```

Request (application/x-www-form-urlencoded)

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

Remarks

This operation takes a string body parameter that is the name of the folder to add.

See Also

[Folder Resource Group](PDM%20Pro%20API_ws~g-ebc7dbbc-e61a-4479-954a-e443044cd655.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
