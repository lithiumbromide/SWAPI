---
title: "api/{vaultName}/files/{fileId}/transitions?version={version} (Get)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-transitions-version={version}"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-transitions-version={version}~o-HttpGet.html"
---

# api/{vaultName}/files/{fileId}/transitions?version={version} (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/files/{fileId}/transitions?version={version} |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}/transitions?version={version} (Get) |
| --- |

Description

Get file transitions

Gets the state transitions for the specified file.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| fileId | (URI parameter) File ID (required) | integer |
| version | (URI parameter) Version (default value is -1) | integer |
| TransitionId | (Response) Transition ID Member of HistoryTransition model | integer |
| VersionNo | (Response) Version number Member of HistoryTransition model | integer |
| Comment | (Response) Comment Member of HistoryTransition model | string |
| Date | (Response) Date Member of HistoryTransition model | date |
| SourceState | (Response) A StateInfo object; each StateInfo object consists of: StateId (integer) StateName (string) IgnorePreviousPermissions (integer) Member of HistoryTransition model | StateInfo |
| DestinationState | (Response) A StateInfo object; each StateInfo object consists of: StateId (integer) StateName (string) IgnorePreviousPermissions (integer) Member of HistoryTransition model | StateInfo |
| User | (Response) A UserInfo object; each UserInfo object consists of: UserName (string) UserId (integer) Member of HistoryTransition model | UserInfo |

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "TransitionId": 1,
    "VersionNo": 2,
    "Comment": "sample string 3",
    "Date": "2022-07-25T14:02:49.482406-04:00",
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
    "Date": "2022-07-25T14:02:49.482406-04:00",
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
    <Date>2022-07-25T14:02:49.482406-04:00</Date>
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
    <Date>2022-07-25T14:02:49.482406-04:00</Date>
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

Remarks

This operation returns an array of HistoryTransition objects, one for each transition made by the file.

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
