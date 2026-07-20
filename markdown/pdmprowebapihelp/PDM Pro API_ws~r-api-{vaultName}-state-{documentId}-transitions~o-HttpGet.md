---
title: "api/{vaultName}/state/{documentId}/transitions (Get)"
project: ""
interface: "r-api-{vaultName}-state-{documentId}-transitions"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-state-{documentId}-transitions~o-HttpGet.html"
---

# api/{vaultName}/state/{documentId}/transitions (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/state/{documentId}/transitions |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > State Transition Resource Group : api/{vaultName}/state/{documentId}/transitions (Get) |
| --- |

Description

Get available transitions for single file

Gets the transitions available for the specified file.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| documentId | (URI parameter) Document ID (required) | integer |
| TransitionId | (Response) Transition ID Member of AvailableTransition model | integer |
| TransitionName | (Response) Transition name Member of AvailableTransition model | string |
| Revoke | (Response) 1 if the parallel transition's approval is revokable, 0 if not Member of AvailableTransition model | boolean |
| Commits | (Response) Whether commits Member of AvailableTransition model | integer |
| Required | (Response) Whether required Member of AvailableTransition model | integer |
| MustEnterComments | (Response) Whether must enter comments Member of AvailableTransition model | boolean |

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

Remarks

This operation can return an array of AvailableTransition objects.

See Also

[State Transition Resource Group](PDM%20Pro%20API_ws~g-7b85dfc9-ca5f-4c42-8689-253a31d91dce.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
