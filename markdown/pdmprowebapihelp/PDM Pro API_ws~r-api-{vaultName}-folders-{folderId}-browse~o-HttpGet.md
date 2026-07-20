---
title: "api/{vaultName}/folders/{folderId}/browse (Get)"
project: ""
interface: "r-api-{vaultName}-folders-{folderId}-browse"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-folders-{folderId}-browse~o-HttpGet.html"
---

# api/{vaultName}/folders/{folderId}/browse (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/folders/{folderId}/browse |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Folder Resource Group : api/{vaultName}/folders/{folderId}/browse (Get) |
| --- |

Description

GET: api/{VaultName}/folders/{FolderID}/browse Get browse folder

Gets the files and folders in the specified folder.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| folderId | (URI parameter) ID of folder in which to browse (required) | integer |
| Id | (Response) ID of object Member of ObjectInfo model | integer |
| Name | (Response) Name of object Member of ObjectInfo model | string |
| Size | (Response) Size of object Member of ObjectInfo model | integer |
| ModifiedDate | (Response) Modification date Member of ObjectInfo model | date |
| Version | (Response) Version Member of ObjectInfo model | integer |
| State | (Response) State Member of ObjectInfo model | string |
| StateId | (Response) State ID Member of ObjectInfo model | integer |
| ParentFolderId | (Response) Parent folder ID Member of ObjectInfo model | integer |
| Path | (Response) Folder path Member of ObjectInfo model | string |
| Type | (Response) An ObjectType; one of: Folder = 0 File = 1 Bom = 3 Member of ObjectInfo model | ObjectType |
| IsLocked | (Response) Whether the object is locked Member of ObjectInfo model | integer |
| LockedBy | (Response) Locked by user Member of ObjectInfo model | integer |
| IsShared | (Response) Whether the object is shared Member of ObjectInfo model | integer |
| IsToolbox | (Response) Whether the object is in the toolbox Member of ObjectInfo model | integer |
| IsDeleted | (Response) Whether the object is deleted Member of ObjectInfo model | integer |

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "Id": 1,
    "Name": "sample string 2",
    "Size": 3,
    "ModifiedDate": "2024-11-27T09:52:31.3283221-05:00",
    "Version": 5,
    "State": "sample string 6",
    "StateId": 7,
    "ParentFolderId": 8,
    "Path": "sample string 9",
    "Type": 0,
    "IsLocked": 10,
    "LockedBy": 11,
    "IsShared": 12,
    "IsToolbox": 13,
    "IsDeleted": 14
  },
  {
    "Id": 1,
    "Name": "sample string 2",
    "Size": 3,
    "ModifiedDate": "2024-11-27T09:52:31.3283221-05:00",
    "Version": 5,
    "State": "sample string 6",
    "StateId": 7,
    "ParentFolderId": 8,
    "Path": "sample string 9",
    "Type": 0,
    "IsLocked": 10,
    "LockedBy": 11,
    "IsShared": 12,
    "IsToolbox": 13,
    "IsDeleted": 14
  }
]
```

Response (application/xml, text/xml)

#### Sample Data

```
<ArrayOfObjectInfo xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <ObjectInfo>
    <Id>1</Id>
    <IsDeleted>14</IsDeleted>
    <IsLocked>10</IsLocked>
    <IsShared>12</IsShared>
    <IsToolbox>13</IsToolbox>
    <LockedBy>11</LockedBy>
    <ModifiedDate>2024-11-27T09:52:31.3283221-05:00</ModifiedDate>
    <Name>sample string 2</Name>
    <ParentFolderId>8</ParentFolderId>
    <Path>sample string 9</Path>
    <Size>3</Size>
    <State>sample string 6</State>
    <StateId>7</StateId>
    <Type>Folder</Type>
    <Version>5</Version>
  </ObjectInfo>
  <ObjectInfo>
    <Id>1</Id>
    <IsDeleted>14</IsDeleted>
    <IsLocked>10</IsLocked>
    <IsShared>12</IsShared>
    <IsToolbox>13</IsToolbox>
    <LockedBy>11</LockedBy>
    <ModifiedDate>2024-11-27T09:52:31.3283221-05:00</ModifiedDate>
    <Name>sample string 2</Name>
    <ParentFolderId>8</ParentFolderId>
    <Path>sample string 9</Path>
    <Size>3</Size>
    <State>sample string 6</State>
    <StateId>7</StateId>
    <Type>Folder</Type>
    <Version>5</Version>
  </ObjectInfo>
</ArrayOfObjectInfo>
```

Example

See the examples for

[api/{vaultName}/authenticate](PDM%20Pro%20API_ws~r-api-{vaultName}-authenticate~o-HttpPost.html)

.

Example

[Modify File Datacards.postman_collection.json](Modify%20File%20Datacards.postman_collection.json)

Remarks

This operation returns an array of ObjectInfo objects.

See Also

[Folder Resource Group](PDM%20Pro%20API_ws~g-ebc7dbbc-e61a-4479-954a-e443044cd655.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
