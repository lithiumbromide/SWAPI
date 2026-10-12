---
title: "api/{vaultName}/delete/computetree (Post)"
project: ""
interface: "r-api-{vaultName}-delete-computetree"
member: "o-HttpPost"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-delete-computetree~o-HttpPost.html"
---

# api/{vaultName}/delete/computetree (Post)

PDM Pro API Web Service

| Post | api/{vaultName}/delete/computetree |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > Vault Resource Group : api/{vaultName}/delete/computetree (Post) |
| --- |

Description

POST: api/{VaultName}/delete/computetree Delete compute tree

Deletes the specified items in the specified vault.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| FolderIDs | (Body parameter) Array of folder IDs Member of DeleteComputeTree model | Collection of integer |
| FileIDs | (Body parameter) Array of file IDs Member of DeleteComputeTree model | Collection of integer |
| Destroy | (Body parameter) Whether to destroy Member of DeleteComputeTree model | boolean |
| FileCount | (Response) Number of files deleted Member of DelResult model | integer |
| FolderCount | (Response) Number of folders deleted Member of DelResult model | integer |
| XRefWarnings | (Response) An XRefWarning object that consists of: ParentProjectID (integer) ObjectType (PweObjectType that is one of: ObjType_NoObject = 0 ObjType_File= 1 ObjType_InternalComponent = 2 ObjType_SavedBOM = 3 ObjType_Item = 4 ObjType_CutListItem = 5 ) ChildObjectType (PweObjectType; see ObjectType) DocumentID (integer) Version (integer) ChildDocumentID (integer) ChildProjectID (integer) ChildVersion (integer) Member of DelResult model | String |

Request (application/json, text/json)

#### Sample Data

```
{
  "FolderIDs": [
    1,
    2
  ],
  "FileIDs": [
    1,
    2
  ],
  "Destroy": true
}
```

Request (application/xml, text/xml)

#### Sample Data

```
<DeleteComputeTree xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <Destroy>true</Destroy>
  <FileIDs xmlns:d2p1="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
    <d2p1:int>1</d2p1:int>
    <d2p1:int>2</d2p1:int>
  </FileIDs>
  <FolderIDs xmlns:d2p1="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
    <d2p1:int>1</d2p1:int>
    <d2p1:int>2</d2p1:int>
  </FolderIDs>
</DeleteComputeTree>
```

Request (application/x-www-form-urlencoded)

Response (application/json, text/json)

#### Sample Data

```
{
  "FileCount": 1,
  "FolderCount": 2,
  "XRefWarnings": [
    {
      "ParentProjectID": 1,
      "ObjectType": 0,
      "ChildObjectType": 0,
      "DocumentID": 2,
      "Version": 3,
      "ChildDocumentID": 4,
      "ChildProjectID": 5,
      "ChildVersion": 6
    },
    {
      "ParentProjectID": 1,
      "ObjectType": 0,
      "ChildObjectType": 0,
      "DocumentID": 2,
      "Version": 3,
      "ChildDocumentID": 4,
      "ChildProjectID": 5,
      "ChildVersion": 6
    }
  ],
  "BranchRefWarnings": [
    {
      "DocumentID": 1,
      "ProjectID": 2,
      "ObjectType": 0,
      "BranchName": "sample string 3",
      "BranchDeleted": 4
    },
    {
      "DocumentID": 1,
      "ProjectID": 2,
      "ObjectType": 0,
      "BranchName": "sample string 3",
      "BranchDeleted": 4
    }
  ],
  "LockedFiles": [
    {
      "DocumentID": 1,
      "ProjectID": 2,
      "ObjectType": 3,
      "UserID": 4,
      "InUserState": true
    },
    {
      "DocumentID": 1,
      "ProjectID": 2,
      "ObjectType": 3,
      "UserID": 4,
      "InUserState": true
    }
  ],
  "FileNames": {
    "1": "sample string 2",
    "3": "sample string 4"
  },
  "UserNameMap": {
    "1": "sample string 2",
    "3": "sample string 4"
  },
  "FolderPaths": {
    "1": "sample string 2",
    "3": "sample string 4"
  },
  "LocalFiles": [
    "sample string 1",
    "sample string 2"
  ],
  "LocalFolders": [
    "sample string 1",
    "sample string 2"
  ],
  "VaultItems": [
    {
      "ProjectID": 1,
      "DocumentID": 2,
      "ObjectType": 3,
      "Flags": 4
    },
    {
      "ProjectID": 1,
      "DocumentID": 2,
      "ObjectType": 3,
      "Flags": 4
    }
  ]
}
```

Response (application/xml, text/xml)

#### Sample Data

```
<DelResult xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Repositories.DTO">
  <BranchRefWarnings>
    <BranchRefWarning>
      <BranchDeleted>4</BranchDeleted>
      <BranchName>sample string 3</BranchName>
      <DocumentID>1</DocumentID>
      <ObjectType>ObjType_NoObject</ObjectType>
      <ProjectID>2</ProjectID>
    </BranchRefWarning>
    <BranchRefWarning>
      <BranchDeleted>4</BranchDeleted>
      <BranchName>sample string 3</BranchName>
      <DocumentID>1</DocumentID>
      <ObjectType>ObjType_NoObject</ObjectType>
      <ProjectID>2</ProjectID>
    </BranchRefWarning>
  </BranchRefWarnings>
  <FileCount>1</FileCount>
  <FileNames xmlns:d2p1="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
    <d2p1:KeyValueOflongstring>
      <d2p1:Key>1</d2p1:Key>
      <d2p1:Value>sample string 2</d2p1:Value>
    </d2p1:KeyValueOflongstring>
    <d2p1:KeyValueOflongstring>
      <d2p1:Key>3</d2p1:Key>
      <d2p1:Value>sample string 4</d2p1:Value>
    </d2p1:KeyValueOflongstring>
  </FileNames>
  <FolderCount>2</FolderCount>
  <FolderPaths xmlns:d2p1="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
    <d2p1:KeyValueOflongstring>
      <d2p1:Key>1</d2p1:Key>
      <d2p1:Value>sample string 2</d2p1:Value>
    </d2p1:KeyValueOflongstring>
    <d2p1:KeyValueOflongstring>
      <d2p1:Key>3</d2p1:Key>
      <d2p1:Value>sample string 4</d2p1:Value>
    </d2p1:KeyValueOflongstring>
  </FolderPaths>
  <LocalFiles xmlns:d2p1="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
    <d2p1:string>sample string 1</d2p1:string>
    <d2p1:string>sample string 2</d2p1:string>
  </LocalFiles>
  <LocalFolders xmlns:d2p1="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
    <d2p1:string>sample string 1</d2p1:string>
    <d2p1:string>sample string 2</d2p1:string>
  </LocalFolders>
  <LockedFiles>
    <LockInfo2>
      <DocumentID>1</DocumentID>
      <InUserState>true</InUserState>
      <ObjectType>3</ObjectType>
      <ProjectID>2</ProjectID>
      <UserID>4</UserID>
    </LockInfo2>
    <LockInfo2>
      <DocumentID>1</DocumentID>
      <InUserState>true</InUserState>
      <ObjectType>3</ObjectType>
      <ProjectID>2</ProjectID>
      <UserID>4</UserID>
    </LockInfo2>
  </LockedFiles>
  <UserNameMap xmlns:d2p1="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
    <d2p1:KeyValueOflongstring>
      <d2p1:Key>1</d2p1:Key>
      <d2p1:Value>sample string 2</d2p1:Value>
    </d2p1:KeyValueOflongstring>
    <d2p1:KeyValueOflongstring>
      <d2p1:Key>3</d2p1:Key>
      <d2p1:Value>sample string 4</d2p1:Value>
    </d2p1:KeyValueOflongstring>
  </UserNameMap>
  <VaultItems>
    <DeleteItem>
      <DocumentID>2</DocumentID>
      <Flags>4</Flags>
      <ObjectType>3</ObjectType>
      <ProjectID>1</ProjectID>
    </DeleteItem>
    <DeleteItem>
      <DocumentID>2</DocumentID>
      <Flags>4</Flags>
      <ObjectType>3</ObjectType>
      <ProjectID>1</ProjectID>
    </DeleteItem>
  </VaultItems>
  <XRefWarnings>
    <XRefWarning>
      <ChildDocumentID>4</ChildDocumentID>
      <ChildProjectID>5</ChildProjectID>
      <ChildVersion>6</ChildVersion>
      <DocumentID>2</DocumentID>
      <Version>3</Version>
      <ChildObjectType>ObjType_NoObject</ChildObjectType>
      <ObjectType>ObjType_NoObject</ObjectType>
      <ParentProjectID>1</ParentProjectID>
    </XRefWarning>
    <XRefWarning>
      <ChildDocumentID>4</ChildDocumentID>
      <ChildProjectID>5</ChildProjectID>
      <ChildVersion>6</ChildVersion>
      <DocumentID>2</DocumentID>
      <Version>3</Version>
      <ChildObjectType>ObjType_NoObject</ChildObjectType>
      <ObjectType>ObjType_NoObject</ObjectType>
      <ParentProjectID>1</ParentProjectID>
    </XRefWarning>
  </XRefWarnings>
</DelResult>
```

Remarks

This operation:

- takes a DeleteComputeTree object as a body parameter.
- returns a DelResult object.

The complete DelResult model consists of:

FileCount (integer)

FolderCount (integer)

XRefWarnings (array of XRefWarning objects; each XRefWarning consists of:

ParentProjectID (integer)

ObjectType (PweObjectType that is one of:

ObjType_NoObject = 0

ObjType_File= 1

ObjType_InternalComponent = 2

ObjType_SavedBOM = 3

ObjType_Item = 4

ObjType_CutListItem = 5

)

ChildObjectType (PweObjectType; see ObjectType)

DocumentID (integer)

Version (integer)

ChildDocumentID (integer)

ChildProjectID (integer)

ChildVersion (integer)

)

BranchRefWarnings (array of BranchRefWarning objects; each BranchRefWarning consists of:

DocumentID (integer)

ProjectID (integer)

ObjectType (PweObjectType; see XRefWarnings)

BranchName (string)

BranchDeleted (integer)

)

LockedFiles (array of LockInfo2 objects; each LockInfo2 consists of:

DocumentID (integer)

ProjectID (integer)

ObjectType (integer)

ObjectType (PweObjectType; see BranchRefWarnings)

UserID (integer)

InUserState (boolean)

)

FileNames (dictionary of integer [key] and string [value] pairs)

UserNameMap (dictionary of integer [key] and string [value] pairs)

FolderPaths (dictionary of integer [key] and string [value] pairs)

LocalFiles (array of strings)

LocalFolders (array of strings)

VaultItems (array of DeleteItem objects; each DeleteItem consists of:

ProjectID (integer)

DocumentID (integer)

ObjectType (integer)

Flags (integer)

)

See Also

[Vault Resource Group](PDM%20Pro%20API_ws~g-4e3666da-2867-45a7-a89f-fe7237448857.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
