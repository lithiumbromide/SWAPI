---
title: "api/{vaultName}/files/{fileId}/transitions?version={version}&folderId={folderId} (Get)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-transitions-version={version}-folderId={folderId}"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-transitions-version={version}-folderId={folderId}~o-HttpGet.html"
---

# api/{vaultName}/files/{fileId}/transitions?version={version}&folderId={folderId} (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/files/{fileId}/transitions?version={version}&folderId={folderId} |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}/transitions?version={version}&folderId={folderId} (Get) |
| --- |

Description

Gets the file transitions for the specified file.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (Required URI Parameter) Vault name | string |
| fileId | (Required URI Parameter) File ID | integer |
| version | (URI Parameter) File version, default is -1 | integer |
| folderId | (URI Parameter) Folder ID, default is 0 | integer |
| TransitionId | (Response) Transition ID (Member of HistoryTransition Model) | integer |
| VersionNo | (Response) Version number (Member of HistoryTransition Model) | integer |
| Comment | (Response) Comment (Member of HistoryTransition Model) | string |
| Date | (Response) Date (Member of HistoryTransition Model) | date |
| SourceState | (Response) Source StateInfo: StateId: integer StateName: string IgnorePreviousPermissions: integer (Member of HistoryTransition Model) | StateInfo |
| DestinationState | (Response) Destination StateInfo: StateId: integer StateName: string IgnorePreviousPermissions: integer (Member of HistoryTransition Model) | StateInfo |
| User | (Response) UserInfo: UserName: string UserId: integer (Member of HistoryTransition Model) | UserInfo |

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "TransitionId": 1,
    "VersionNo": 2,
    "Comment": "sample string 3",
    "Date": "2024-11-27T09:52:30.6765737-05:00",
    "SourceState": {
      "StateId": 1,
      "StateName": "sample string 2",
      "IgnorePreviousPermissions": 3
    },
    "DestinationState": {
      "StateId": 1,
      "StateName": "sample string 2",
      "IgnorePreviousPermissions": 3
    },
    "User": {
      "UserName": "sample string 1",
      "UserId": 2
    }
  },
  {
    "TransitionId": 1,
    "VersionNo": 2,
    "Comment": "sample string 3",
    "Date": "2024-11-27T09:52:30.6765737-05:00",
    "SourceState": {
      "StateId": 1,
      "StateName": "sample string 2",
      "IgnorePreviousPermissions": 3
    },
    "DestinationState": {
      "StateId": 1,
      "StateName": "sample string 2",
      "IgnorePreviousPermissions": 3
    },
    "User": {
      "UserName": "sample string 1",
      "UserId": 2
    }
  }
]
```

Response (application/xml, text/xml)

#### Sample Data

```
<ArrayOfHistoryTransition xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <HistoryTransition>
    <Comment>sample string 3</Comment>
    <Date>2024-11-27T09:52:30.6765737-05:00</Date>
    <DestinationState>
      <IgnorePreviousPermissions>3</IgnorePreviousPermissions>
      <StateId>1</StateId>
      <StateName>sample string 2</StateName>
    </DestinationState>
    <SourceState>
      <IgnorePreviousPermissions>3</IgnorePreviousPermissions>
      <StateId>1</StateId>
      <StateName>sample string 2</StateName>
    </SourceState>
    <TransitionId>1</TransitionId>
    <User>
      <UserId>2</UserId>
      <UserName>sample string 1</UserName>
    </User>
    <VersionNo>2</VersionNo>
  </HistoryTransition>
  <HistoryTransition>
    <Comment>sample string 3</Comment>
    <Date>2024-11-27T09:52:30.6765737-05:00</Date>
    <DestinationState>
      <IgnorePreviousPermissions>3</IgnorePreviousPermissions>
      <StateId>1</StateId>
      <StateName>sample string 2</StateName>
    </DestinationState>
    <SourceState>
      <IgnorePreviousPermissions>3</IgnorePreviousPermissions>
      <StateId>1</StateId>
      <StateName>sample string 2</StateName>
    </SourceState>
    <TransitionId>1</TransitionId>
    <User>
      <UserId>2</UserId>
      <UserName>sample string 1</UserName>
    </User>
    <VersionNo>2</VersionNo>
  </HistoryTransition>
</ArrayOfHistoryTransition>
```

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
