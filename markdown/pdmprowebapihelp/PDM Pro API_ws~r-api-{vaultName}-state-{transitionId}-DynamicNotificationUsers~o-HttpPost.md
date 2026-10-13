---
title: "api/{vaultName}/state/{transitionId}/DynamicNotificationUsers (Post)"
project: ""
interface: "r-api-{vaultName}-state-{transitionId}-DynamicNotificationUsers"
member: "o-HttpPost"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-state-{transitionId}-DynamicNotificationUsers~o-HttpPost.html"
---

# api/{vaultName}/state/{transitionId}/DynamicNotificationUsers (Post)

PDM Pro API Web Service

| Post | api/{vaultName}/state/{transitionId}/DynamicNotificationUsers |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > State Transition Resource Group : api/{vaultName}/state/{transitionId}/DynamicNotificationUsers (Post) |
| --- |

Description

POST: api/{vaultName}/state/{transitionId}/DynamicNotificationUsers Get dynamic notification users

Gets the users to notify when the specified items undergo the specified transition.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| transitionId | (URI parameter) Transition ID (required) | integer |
| FolderId | (Response) ID folder for which notifications are enabled Member of NotificationInfo model | integer |
| Users | (Response) Array of UserInfo objects; each UserInfo consists of: UserName (string) UserId (integer) Member of NotificationInfo model | Collection of UserInfo |

Request (application/json, text/json)

Array of file IDs is passed as a body parameter

#### Sample Data

```
[
  1,
  2
]
```

Request (application/xml, text/xml)

Array of file IDs is passed as a body parameter

#### Sample Data

```
<ArrayOfint xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
  <int>1</int>
  <int>2</int>
</ArrayOfint>
```

Request (application/x-www-form-urlencoded)

Array of file IDs is passed as a body parameter

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "FolderId": 1,
    "Users": [
      {
        "UserName": "sample string 1",
        "UserId": 2
      },
      {
        "UserName": "sample string 1",
        "UserId": 2
      }
    ]
  },
  {
    "FolderId": 1,
    "Users": [
      {
        "UserName": "sample string 1",
        "UserId": 2
      },
      {
        "UserName": "sample string 1",
        "UserId": 2
      }
    ]
  }
]
```

Response (application/xml, text/xml)

#### Sample Data

```
<ArrayOfNotificationInfo xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <NotificationInfo>
    <FolderId>1</FolderId>
    <Users>
      <UserInfo>
        <UserId>2</UserId>
        <UserName>sample string 1</UserName>
      </UserInfo>
      <UserInfo>
        <UserId>2</UserId>
        <UserName>sample string 1</UserName>
      </UserInfo>
    </Users>
  </NotificationInfo>
  <NotificationInfo>
    <FolderId>1</FolderId>
    <Users>
      <UserInfo>
        <UserId>2</UserId>
        <UserName>sample string 1</UserName>
      </UserInfo>
      <UserInfo>
        <UserId>2</UserId>
        <UserName>sample string 1</UserName>
      </UserInfo>
    </Users>
  </NotificationInfo>
</ArrayOfNotificationInfo>
```

Remarks

This operation:

- takes an array of body parameter integers that are file IDs.
- returns an array of NotificationInfos.

See Also

[State Transition Resource Group](PDM%20Pro%20API_ws~g-7b85dfc9-ca5f-4c42-8689-253a31d91dce.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
