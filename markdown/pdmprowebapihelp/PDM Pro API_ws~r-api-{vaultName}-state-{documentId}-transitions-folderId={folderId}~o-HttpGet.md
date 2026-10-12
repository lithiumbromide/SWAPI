---
title: "api/{vaultName}/state/{documentId}/transitions?folderId={folderId} (Get)"
project: ""
interface: "r-api-{vaultName}-state-{documentId}-transitions-folderId={folderId}"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-state-{documentId}-transitions-folderId={folderId}~o-HttpGet.html"
---

# api/{vaultName}/state/{documentId}/transitions?folderId={folderId} (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/state/{documentId}/transitions?folderId={folderId} |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > State Transition Resource Group : api/{vaultName}/state/{documentId}/transitions?folderId={folderId} (Get) |
| --- |

Description

Gets the transitions available for the specified file.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (Required URI parameter) Name of vault | string |
| documentId | (Required URI parameter) File ID | integer |
| folderId | (URI parameter) Folder ID, default is 0 | integer |
| TransitionId | (Response) Transition ID (Member of AvailableTransition Model) | integer |
| TransitionName | (Response) Transition name (Member of AvailableTransition Model) | string |
| Revoke | (Response) Whether a revoke (Member of AvailableTransition Model) | boolean |
| Commits | (Response) Number of users who have performed this parallel transition; Commits <= Required (Member of AvailableTransition Model) | integer |
| Required | (Response) Number of required (Member of AvailableTransition Model) | integer |
| MustEnterComments | (Response) Whether must enter comments (Member of AvailableTransition Model) | boolean |

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "TransitionId": 1,
    "TransitionName": "sample string 2",
    "Revoke": true,
    "Commits": 4,
    "Required": 5,
    "MustEnterComments": true
  },
  {
    "TransitionId": 1,
    "TransitionName": "sample string 2",
    "Revoke": true,
    "Commits": 4,
    "Required": 5,
    "MustEnterComments": true
  }
]
```

Response (application/xml, text/xml)

#### Sample Data

```
<ArrayOfAvailableTransition xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <AvailableTransition>
    <Commits>4</Commits>
    <MustEnterComments>true</MustEnterComments>
    <Required>5</Required>
    <Revoke>true</Revoke>
    <TransitionId>1</TransitionId>
    <TransitionName>sample string 2</TransitionName>
  </AvailableTransition>
  <AvailableTransition>
    <Commits>4</Commits>
    <MustEnterComments>true</MustEnterComments>
    <Required>5</Required>
    <Revoke>true</Revoke>
    <TransitionId>1</TransitionId>
    <TransitionName>sample string 2</TransitionName>
  </AvailableTransition>
</ArrayOfAvailableTransition>
```

See Also

[State Transition Resource Group](PDM%20Pro%20API_ws~g-7b85dfc9-ca5f-4c42-8689-253a31d91dce.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
