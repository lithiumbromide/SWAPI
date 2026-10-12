---
title: "api/{vaultName}/state/{transitionId}/changestate?revoke={revoke} (Post)"
project: ""
interface: "r-api-{vaultName}-state-{transitionId}-changestate-revoke={revoke}"
member: "o-HttpPost"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-state-{transitionId}-changestate-revoke={revoke}~o-HttpPost.html"
---

# api/{vaultName}/state/{transitionId}/changestate?revoke={revoke} (Post)

PDM Pro API Web Service

| Post | api/{vaultName}/state/{transitionId}/changestate?revoke={revoke} |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > State Transition Resource Group : api/{vaultName}/state/{transitionId}/changestate?revoke={revoke} (Post) |
| --- |

Description

POST: api/{vaultName}/state/{transitionId}/changestate Change state

Changes the state of the specified documents.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| transitionId | (URI parameter) Transition ID (required) | integer |
| revoke | (URI parameter) Whether a revoke (default value is false) | boolean |
| Comment | (Body parameter) Comment | string |
| NotificationComment | (Body parameter) Notification comment | string |
| Documents | (Body parameter) Array of file IDs | Collection of integer |
| NotifyUsers | (Body parameter) Array of user IDs | Collection of integer |
| Password | (Body parameter) Password | string |
| Id | (Response) File ID | integer |
| IsSuccess | (Response) Whether transition is successful | boolean |
| Warning | (Response) A BaseWarningModel object that consists of: Message (string) IsBlocking (boolean) IsError (boolean) | BaseWarningModel |

Request (application/json, text/json)

#### Sample Data

```
{
  "Comment": "sample string 1",
  "NotificationComment": "sample string 2",
  "Documents": [
    1,
    2
  ],
  "NotifyUsers": [
    1,
    2
  ],
  "Password": "sample string 3"
}
```

Request (application/xml, text/xml)

#### Sample Data

```
<TransitionModel xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <Comment>sample string 1</Comment>
  <Documents xmlns:d2p1="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
    <d2p1:int>1</d2p1:int>
    <d2p1:int>2</d2p1:int>
  </Documents>
  <NotificationComment>sample string 2</NotificationComment>
  <NotifyUsers xmlns:d2p1="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
    <d2p1:int>1</d2p1:int>
    <d2p1:int>2</d2p1:int>
  </NotifyUsers>
  <Password>sample string 3</Password>
</TransitionModel>
```

Request (application/x-www-form-urlencoded)

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "Id": 1,
    "IsSuccess": true,
    "Warning": null
  },
  {
    "Id": 1,
    "IsSuccess": true,
    "Warning": null
  }
]
```

Response (application/xml, text/xml)

#### Sample Data

```
<ArrayOfTransitionResultModel xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <TransitionResultModel>
    <Id>1</Id>
    <IsSuccess>true</IsSuccess>
    <Warning i:nil="true" />
  </TransitionResultModel>
  <TransitionResultModel>
    <Id>1</Id>
    <IsSuccess>true</IsSuccess>
    <Warning i:nil="true" />
  </TransitionResultModel>
</ArrayOfTransitionResultModel>
```

Remarks

This operation:

- takes TransitionModel body parameters.
- returns an array of TransitionResultModels.

See Also

[State Transition Resource Group](PDM%20Pro%20API_ws~g-7b85dfc9-ca5f-4c42-8689-253a31d91dce.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
