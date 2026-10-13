---
title: "api/{vaultName}/files/{fileId}/{version}/{folderId}/variables (Get)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-{version}-{folderId}-variables"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-{version}-{folderId}-variables~o-HttpGet.html"
---

# api/{vaultName}/files/{fileId}/{version}/{folderId}/variables (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/files/{fileId}/{version}/{folderId}/variables |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}/{version}/{folderId}/variables (Get) |
| --- |

Description

Gets configuration variable information for the specified file.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (Required URI Parameter) Vault name | string |
| fileId | (Required URI Parameter) File ID | integer |
| version | (Required URI Parameter) File version | integer |
| folderId | (URI Parameter) Folder ID, default is 0 | integer |
| ConfigurationName | (Response) Name of configuration (Member of ConfigInfo Model) | string |
| ConfigurationId | (Response) ID of configuration (Member of ConfigInfo Model) | integer |
| Models | (Response) Collection of VariableInfo: VarId: integer VarName: string VarValue: string VarType: VarTypeNone = 0 VarTypeText = 1 VarTypeInt = 2 VarTypeFloat = 3 VarTypeBool = 4 VarTypeDate = 5 Mandatory: boolean VersionFree: boolean (Member of ConfigInfo Model) | Collection of VariableInfo |

Response (application/json, text/json)

#### Sample Data

```
[
  {
    "Models": [
      {
        "VarId": 1,
        "VarName": "sample string 2",
        "VarValue": "sample string 3",
        "VarType": 0,
        "Mandatory": true,
        "VersionFree": true
      },
      {
        "VarId": 1,
        "VarName": "sample string 2",
        "VarValue": "sample string 3",
        "VarType": 0,
        "Mandatory": true,
        "VersionFree": true
      }
    ],
    "ConfigurationName": "sample string 1",
    "ConfigurationId": 2
  },
  {
    "Models": [
      {
        "VarId": 1,
        "VarName": "sample string 2",
        "VarValue": "sample string 3",
        "VarType": 0,
        "Mandatory": true,
        "VersionFree": true
      },
      {
        "VarId": 1,
        "VarName": "sample string 2",
        "VarValue": "sample string 3",
        "VarType": 0,
        "Mandatory": true,
        "VersionFree": true
      }
    ],
    "ConfigurationName": "sample string 1",
    "ConfigurationId": 2
  }
]
```

Response (application/xml, text/xml)

#### Sample Data

```
<ArrayOfConfigInfo xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <ConfigInfo>
    <ConfigurationId>2</ConfigurationId>
    <ConfigurationName>sample string 1</ConfigurationName>
    <Models>
      <VariableInfo>
        <Mandatory>true</Mandatory>
        <VarId>1</VarId>
        <VarName>sample string 2</VarName>
        <VarType>VarTypeNone</VarType>
        <VarValue>sample string 3</VarValue>
        <VersionFree>true</VersionFree>
      </VariableInfo>
      <VariableInfo>
        <Mandatory>true</Mandatory>
        <VarId>1</VarId>
        <VarName>sample string 2</VarName>
        <VarType>VarTypeNone</VarType>
        <VarValue>sample string 3</VarValue>
        <VersionFree>true</VersionFree>
      </VariableInfo>
    </Models>
  </ConfigInfo>
  <ConfigInfo>
    <ConfigurationId>2</ConfigurationId>
    <ConfigurationName>sample string 1</ConfigurationName>
    <Models>
      <VariableInfo>
        <Mandatory>true</Mandatory>
        <VarId>1</VarId>
        <VarName>sample string 2</VarName>
        <VarType>VarTypeNone</VarType>
        <VarValue>sample string 3</VarValue>
        <VersionFree>true</VersionFree>
      </VariableInfo>
      <VariableInfo>
        <Mandatory>true</Mandatory>
        <VarId>1</VarId>
        <VarName>sample string 2</VarName>
        <VarType>VarTypeNone</VarType>
        <VarValue>sample string 3</VarValue>
        <VersionFree>true</VersionFree>
      </VariableInfo>
    </Models>
  </ConfigInfo>
</ArrayOfConfigInfo>
```

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
