---
title: "api/{vaultName}/notifications?all={all}&pageNo={pageNo}&pageSize={pageSize} (Get)"
project: ""
interface: "r-api-{vaultName}-notifications-all={all}-pageNo={pageNo}-pageSize={pageSize}"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-notifications-all={all}-pageNo={pageNo}-pageSize={pageSize}~o-HttpGet.html"
---

# api/{vaultName}/notifications?all={all}&pageNo={pageNo}&pageSize={pageSize} (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/notifications?all={all}&pageNo={pageNo}&pageSize={pageSize} |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Notification Resource Group : api/{vaultName}/notifications?all={all}&pageNo={pageNo}&pageSize={pageSize} (Get) |
| --- |

Description

GET: api/{VaultName}/notifications Get user notifications

Gets the user notifications.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| all | (URI parameter) Whether to retrieve all notifications (default value is true) | boolean |
| pageNo | (URI parameter) Page number (default value is 0) | integer |
| pageSize | (URI parameter) Page size (default value is 0) | integer |
| MessageId | (Response) Message ID Member of Messages model | integer |
| Type | (Response) MsgType object; one of: Msgt_All = 0 Msgt_UserMsg = 1 Msgt_NotificationFile = 2 Msgt_NotificationFolder = 3 Msgt_NotificationErp = 4 Msgt_NotificationItem = 5 Msgt_NotificationTask = 6 Msgt_NotificationUpgr = 7 Member of Messages model | MsgType |
| Subject | (Response) Subject text Member of Messages model | string |
| Message | (Response) Message text Member of Messages model | string |
| Time | (Response) Date Member of Messages model | date |
| Sender | (Response) A UserInfo object that consists of: UserName (string) UserId (integer) Member of Messages model | UserInfo |
| New | (Response) Whether the notification is new Member of Messages model | boolean |

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "MessageId": 1,
    "Type": 0,
    "Subject": "sample string 2",
    "Message": "sample string 3",
    "Time": "2024-11-27T09:52:31.0644265-05:00",
    "Sender": {
      "UserName": "sample string 1",
      "UserId": 2
    },
    "New": true
  },
  {
    "MessageId": 1,
    "Type": 0,
    "Subject": "sample string 2",
    "Message": "sample string 3",
    "Time": "2024-11-27T09:52:31.0644265-05:00",
    "Sender": {
      "UserName": "sample string 1",
      "UserId": 2
    },
    "New": true
  }
]
```

Response (application/xml, text/xml)

#### Sample Data

```
<ArrayOfMessages xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <Messages>
    <Message>sample string 3</Message>
    <MessageId>1</MessageId>
    <New>true</New>
    <Sender>
      <UserId>2</UserId>
      <UserName>sample string 1</UserName>
    </Sender>
    <Subject>sample string 2</Subject>
    <Time>2024-11-27T09:52:31.0644265-05:00</Time>
    <Type>Msgt_All</Type>
  </Messages>
  <Messages>
    <Message>sample string 3</Message>
    <MessageId>1</MessageId>
    <New>true</New>
    <Sender>
      <UserId>2</UserId>
      <UserName>sample string 1</UserName>
    </Sender>
    <Subject>sample string 2</Subject>
    <Time>2024-11-27T09:52:31.0644265-05:00</Time>
    <Type>Msgt_All</Type>
  </Messages>
</ArrayOfMessages>
```

Remarks

This operation can return an array of Message objects.

See Also

[Notification Resource Group](PDM%20Pro%20API_ws~g-a913ab1d-ff6c-435e-bc6e-8e6294326caa.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
