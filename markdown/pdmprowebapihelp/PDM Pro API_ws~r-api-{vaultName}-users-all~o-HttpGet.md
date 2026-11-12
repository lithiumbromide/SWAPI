---
title: "api/{vaultName}/users/all (Get)"
project: ""
interface: "r-api-{vaultName}-users-all"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-users-all~o-HttpGet.html"
---

# api/{vaultName}/users/all (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/users/all |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > User Resource Group : api/{vaultName}/users/all (Get) |
| --- |

Description

GET: api/{VaultName}/users or api/{VaultName}/users/all Get users

Gets the users of the specified vault.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| UserInfo | (Response) A UserInfo object that consists of: UserName (string) UserId (integer) Member of UserInfoFull model | UserInfo |
| FullName | (Response) User name Member of UserInfoFull model | string |
| Initials | (Response) User initials Member of UserInfoFull model | string |

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "UserInfo": {
      "UserName": "sample string 1",
      "UserId": 2
    },
    "FullName": "sample string 1",
    "Initials": "sample string 2"
  },
  {
    "UserInfo": {
      "UserName": "sample string 1",
      "UserId": 2
    },
    "FullName": "sample string 1",
    "Initials": "sample string 2"
  }
]
```

Response (application/xml, text/xml)

#### Sample Data

```
<ArrayOfUserInfoFull xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <UserInfoFull>
    <FullName>sample string 1</FullName>
    <Initials>sample string 2</Initials>
    <UserInfo>
      <UserId>2</UserId>
      <UserName>sample string 1</UserName>
    </UserInfo>
  </UserInfoFull>
  <UserInfoFull>
    <FullName>sample string 1</FullName>
    <Initials>sample string 2</Initials>
    <UserInfo>
      <UserId>2</UserId>
      <UserName>sample string 1</UserName>
    </UserInfo>
  </UserInfoFull>
</ArrayOfUserInfoFull>
```

See Also

[User Resource Group](PDM%20Pro%20API_ws~g-09a63486-9278-41ff-970c-d47012e2bea1.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
