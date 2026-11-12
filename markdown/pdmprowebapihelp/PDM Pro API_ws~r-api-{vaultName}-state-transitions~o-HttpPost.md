---
title: "api/{vaultName}/state/transitions (Post)"
project: ""
interface: "r-api-{vaultName}-state-transitions"
member: "o-HttpPost"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-state-transitions~o-HttpPost.html"
---

# api/{vaultName}/state/transitions (Post)

PDM Pro API Web Service

| Post | api/{vaultName}/state/transitions |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > State Transition Resource Group : api/{vaultName}/state/transitions (Post) |
| --- |

Description

POST: api/{vaultName}/state/transitions Get available transitions for multiple files

Gets the transitions available for multiple files.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| TransitionId | (Response) Transition ID Member of AvailableTransition model | integer |
| TransitionName | (Response) Transition name Member of AvailableTransition model | string |
| Revoke | (Response) Whether revokable Member of AvailableTransition model | boolean |
| Commits | (Response) Number of users who have performed this parallel transition; Commits <= Required Member of AvailableTransition model | integer |
| Required | (Response) Number of users required to perform this parallel transition Member of AvailableTransition model | integer |
| MustEnterComments | (Response) Whether must enter comments Member of AvailableTransition model | boolean |

Request (application/json, text/json)

Body parameter array of file IDs

#### Sample Data

```
[
  1,
  2
]
```

Request (application/xml, text/xml)

Body parameter array of file IDs

#### Sample Data

```
<ArrayOfint xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
  <int>1</int>
  <int>2</int>
</ArrayOfint>
```

Request (application/x-www-form-urlencoded)

Body parameter array of file IDs

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

This operation:

- takes an array of body parameters that are file IDs.
- returns an array of AvailableTransition objects.

See Also

[State Transition Resource Group](PDM%20Pro%20API_ws~g-7b85dfc9-ca5f-4c42-8689-253a31d91dce.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
