---
title: "api/{vaultName}/files/{fileId}/datacard?folderId={folderId} (Post)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-datacard-folderId={folderId}"
member: "o-HttpPost"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-datacard-folderId={folderId}~o-HttpPost.html"
---

# api/{vaultName}/files/{fileId}/datacard?folderId={folderId} (Post)

PDM Pro API Web Service

| Post | api/{vaultName}/files/{fileId}/datacard?folderId={folderId} |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Data Card Resource Group : api/{vaultName}/files/{fileId}/datacard?folderId={folderId} (Post) |
| --- |

Description

Saves the specified data card variables to the specified file.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Name of vault | string |
| fileId | (URI parameter) File ID | integer |
| folderId | (URI parameter) Folder ID | integer |
| Models | (Body parameter) (VariableInfo_DataCard: ReadOnly: boolean Multiline: boolean VarId: integer VarName: string VarValue: string VarType: VarTypeNone = 0 VarTypeText = 1 VarTypeInt = 2 VarTypeFloat = 3 VarTypeBool = 4 VarTypeDate = 5 Mandatory: boolean VersionFree: boolean ) (Member of ConfigInfo_DataCard) | Collection of VariableInfo_DataCard |
| ConfigurationName | (Body parameter) Name of configuration (Member of ConfigInfo_DataCard) | string |
| ConfigurationId | (Body parameter) Configuration ID (Member of ConfigInfo_DataCard) | integer |

Request (application/json, text/json)

#### Sample Data

```
[
  {
    "Models": [
      {
        "ReadOnly": true,
        "Multiline": true,
        "VarId": 3,
        "VarName": "sample string 4",
        "VarValue": "sample string 5",
        "VarType": 0,
        "Mandatory": true,
        "VersionFree": true
      },
      {
        "ReadOnly": true,
        "Multiline": true,
        "VarId": 3,
        "VarName": "sample string 4",
        "VarValue": "sample string 5",
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
        "ReadOnly": true,
        "Multiline": true,
        "VarId": 3,
        "VarName": "sample string 4",
        "VarValue": "sample string 5",
        "VarType": 0,
        "Mandatory": true,
        "VersionFree": true
      },
      {
        "ReadOnly": true,
        "Multiline": true,
        "VarId": 3,
        "VarName": "sample string 4",
        "VarValue": "sample string 5",
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

Request (application/xml, text/xml)

#### Sample Data

```
<ArrayOfConfigInfo_DataCard xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <ConfigInfo_DataCard>
    <ConfigurationId>2</ConfigurationId>
    <ConfigurationName>sample string 1</ConfigurationName>
    <Models>
      <VariableInfo_DataCard>
        <Mandatory>true</Mandatory>
        <VarId>3</VarId>
        <VarName>sample string 4</VarName>
        <VarType>VarTypeNone</VarType>
        <VarValue>sample string 5</VarValue>
        <VersionFree>true</VersionFree>
        <Multiline>true</Multiline>
        <ReadOnly>true</ReadOnly>
      </VariableInfo_DataCard>
      <VariableInfo_DataCard>
        <Mandatory>true</Mandatory>
        <VarId>3</VarId>
        <VarName>sample string 4</VarName>
        <VarType>VarTypeNone</VarType>
        <VarValue>sample string 5</VarValue>
        <VersionFree>true</VersionFree>
        <Multiline>true</Multiline>
        <ReadOnly>true</ReadOnly>
      </VariableInfo_DataCard>
    </Models>
  </ConfigInfo_DataCard>
  <ConfigInfo_DataCard>
    <ConfigurationId>2</ConfigurationId>
    <ConfigurationName>sample string 1</ConfigurationName>
    <Models>
      <VariableInfo_DataCard>
        <Mandatory>true</Mandatory>
        <VarId>3</VarId>
        <VarName>sample string 4</VarName>
        <VarType>VarTypeNone</VarType>
        <VarValue>sample string 5</VarValue>
        <VersionFree>true</VersionFree>
        <Multiline>true</Multiline>
        <ReadOnly>true</ReadOnly>
      </VariableInfo_DataCard>
      <VariableInfo_DataCard>
        <Mandatory>true</Mandatory>
        <VarId>3</VarId>
        <VarName>sample string 4</VarName>
        <VarType>VarTypeNone</VarType>
        <VarValue>sample string 5</VarValue>
        <VersionFree>true</VersionFree>
        <Multiline>true</Multiline>
        <ReadOnly>true</ReadOnly>
      </VariableInfo_DataCard>
    </Models>
  </ConfigInfo_DataCard>
</ArrayOfConfigInfo_DataCard>
```

Request (application/x-www-form-urlencoded)

Response (application/json, text/json)

#### Sample Data

```
true
```

Response (application/xml, text/xml)

#### Sample Data

```
<boolean xmlns="http://schemas.microsoft.com/2003/10/Serialization/">true</boolean>
```

See Also

[Data Card Resource Group](PDM%20Pro%20API_ws~g-b9fd019f-fc85-4753-9377-bf3fb3a1a5f8.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
