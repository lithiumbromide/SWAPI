---
title: "api/{vaultName}/searchvariables (Post)"
project: ""
interface: "r-api-{vaultName}-searchvariables"
member: "o-HttpPost"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-searchvariables~o-HttpPost.html"
---

# api/{vaultName}/searchvariables (Post)

PDM Pro API Web Service

| Post | api/{vaultName}/searchvariables |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Search Resource Group : api/{vaultName}/searchvariables (Post) |
| --- |

Description

Specifies parameters and variables for a search.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (Required URI parameter) Name of vault | string |
| Name | (Body and Response parameter) File name or folder name or empty; supports "%" wildcard search (Member of SearchVariables Model) (See Remarks) | string |
| ObjectTypeCriteria | (Body parameter) Files = 1, Folders = 2, or Files and folders = 3 (Member of SearchVariables Model) | SearchObjectTypeCriteria |
| StartPath | (Body parameter) Relative folder path where the search begins; if empty, search starts at vault root (Member of SearchVariables Model) | string |
| PathCriteria | (Body parameter) Current folder = 1, Current folder and subfolders = 2, All folders = 3 (Member of SearchVariables Model) | SearchPathCriteria |
| VersionCriteria | (Body parameter) Search in latest version of files = 1 Search in all versions of files = 2 (Member of SearchVariables Model) | SearchVersionCriteria |
| SearchOperand | (Body parameter) None = 0 AND = 1 OR = 2 (Member of SearchVariables Model) | SearchOperand |
| Variables | (Body parameter) List of variables to search for; can be empty (Member of SearchVariables Model) (See Remarks) | Collection of SearchVariable |
| Id | (Response) File ID (Member of ObjectInfo Model) | integer |
| Size | (Response) File size (Member of ObjectInfo Model) | integer |
| ModifiedDate | (Response) Modification date (Member of ObjectInfo Model) | date |
| Version | (Response) File version (Member of ObjectInfo Model) | integer |
| State | (Response) Workflow state (Member of ObjectInfo Model) | string |
| StateId | (Response) Workflow state ID (Member of ObjectInfo Model) | integer |
| ParentFolderId | (Response) Parent folder ID (Member of ObjectInfo Model) | integer |
| Path | (Response) Folder path (Member of ObjectInfo Model) | string |
| Type | (Response) Folder = 0 File = 1 Bom = 3 (Member of ObjectInfo Model) | ObjectType |
| IsLocked | (Response) Whether the file is checked out (Member of ObjectInfo Model) | integer |
| LockedBy | (Response) ID of user who checked out the file (Member of ObjectInfo Model) | integer |
| IsShared | (Response) Whether the file is shared (Member of ObjectInfo Model) | integer |
| IsToolbox | (Response) Whether the file is a toolbox item (Member of ObjectInfo Model) | integer |
| IsDeleted | (Response) Whether the file is deleted (Member of ObjectInfo Model) | integer |

Request (application/json, text/json)

#### Sample Data

```
{
  "Name": "sample string 1",
  "ObjectTypeCriteria": 1,
  "StartPath": "sample string 2",
  "PathCriteria": 1,
  "VersionCriteria": 1,
  "SearchOperand": 0,
  "Variables": [
    {
      "VariableName": "sample string 1",
      "SearchValue": "sample string 2"
    },
    {
      "VariableName": "sample string 1",
      "SearchValue": "sample string 2"
    }
  ]
}
```

Request (application/xml, text/xml)

#### Sample Data

```
<SearchVariablesModel xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <Name>sample string 1</Name>
  <ObjectTypeCriteria>File</ObjectTypeCriteria>
  <PathCriteria>CurrentFolder</PathCriteria>
  <SearchOperand>NONE</SearchOperand>
  <StartPath>sample string 2</StartPath>
  <Variables>
    <SearchVariable>
      <SearchValue>sample string 2</SearchValue>
      <VariableName>sample string 1</VariableName>
    </SearchVariable>
    <SearchVariable>
      <SearchValue>sample string 2</SearchValue>
      <VariableName>sample string 1</VariableName>
    </SearchVariable>
  </Variables>
  <VersionCriteria>LatestVersion</VersionCriteria>
</SearchVariablesModel>
```

Request (application/x-www-form-urlencoded)

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "Id": 1,
    "Name": "sample string 2",
    "Size": 3,
    "ModifiedDate": "2024-11-27T09:51:59.716492-05:00",
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
    "ModifiedDate": "2024-11-27T09:51:59.716492-05:00",
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
    <ModifiedDate>2024-11-27T09:51:59.716492-05:00</ModifiedDate>
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
    <ModifiedDate>2024-11-27T09:51:59.716492-05:00</ModifiedDate>
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

[Use Search Variables.postman_collection.json](Use%20Search%20Variables.postman_collection.json)

Remarks

If Name and Variables are provided, search returns all items matching variables and name (+ other criteria).

If Name is empty and Variables are provided, search returns all items matching the variables (+ other criteria).

If Variables are empty and only Name is provided, search returns all items matching the name (+ other criteria).

If Name and Variables are empty, search returns all items based on other criteria.

See Also

[Search Resource Group](PDM%20Pro%20API_ws~g-b95b425f-17d8-44cc-ac84-321dc3026434.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
