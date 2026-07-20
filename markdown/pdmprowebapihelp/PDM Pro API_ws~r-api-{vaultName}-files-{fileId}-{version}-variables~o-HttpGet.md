---
title: "api/{vaultName}/files/{fileId}/{version}/variables (Get)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-{version}-variables"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-{version}-variables~o-HttpGet.html"
---

# api/{vaultName}/files/{fileId}/{version}/variables (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/files/{fileId}/{version}/variables |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}/{version}/variables (Get) |
| --- |

Description

Get file variables

Gets the specified file's variables.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| fileId | (URI parameter) File ID (required) | integer |
| version | (URI parameter) File version (required) | integer |
| ConfigurationName | (Response) Configuration name Member of ConfigInfo model (see Remarks ) | string |
| ConfigurationId | (Response) Configuration ID Member of ConfigInfo model (see Remarks ) | integer |
| Models | (Response) Array of VariableInfos; each VariableInfo consists of: VarId (integer) VarName (string) VarValue (string) VarType (one of: VarTypeNone = 0 VarTypeText = 1 VarTypeInt = 2 VarTypeFloat = 3 VarTypeBool = 4 VarTypeDate = 5 Mandatory (boolean) VersionFree (boolean) Member of ConfigInfo model (see Remarks ) | Collection of VariableInfo |

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

Remarks

This operation can return an array of ConfigInfos. See the Response examples.

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
