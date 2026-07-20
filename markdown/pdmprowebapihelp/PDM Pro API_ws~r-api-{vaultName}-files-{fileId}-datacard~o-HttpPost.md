---
title: "api/{vaultName}/files/{fileId}/datacard (Post)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-datacard"
member: "o-HttpPost"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-datacard~o-HttpPost.html"
---

# api/{vaultName}/files/{fileId}/datacard (Post)

PDM Pro API Web Service

| Post | api/{vaultName}/files/{fileId}/datacard |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Data Card Resource Group : api/{vaultName}/files/{fileId}/datacard (Post) |
| --- |

Description

Save file data card

Saves the data card for the specified file and vault.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| fileId | (URI parameter) File ID (required) | integer |
| Models | (Body) Array of VariableInfo_DataCards; each VariableInfo_DataCard consists of: ReadOnly (boolean) Multiline (boolean) VarId (integer) VarName (string) VarValue (string) VarType (one of: VarTypeNone = 0 VarTypeText = 1 VarTypeInt = 2 VarTypeFloat = 3 VarTypeBool = 4 VarTypeDate = 5 Mandatory (boolean) VersionFree (boolean) Member of ConfigInfo_DataCard model (see Remarks ) | Collection of VariableInfo_DataCard |
| ConfigurationName | (Body) Configuration name Member of ConfigInfo_DataCard model (see Remarks ) | string |
| ConfigurationId | (Body) Configuration ID Member of ConfigInfo_DataCard model (see Remarks ) | integer |

Request (application/json, text/json)

Body parameter contains multiple arrays, each consisting of variables to modify (Models), configuration name, and configuration ID.

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

Body parameter contains multiple arrays, each consisting of variables to modify (Models), configuration name, and configuration ID.

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

Body parameter contains multiple arrays, each consisting of variables to modify (Models), configuration name, and configuration ID.

Response (application/json, text/json)

Returns the status of the operation.

#### Sample Data

```
true
```

Response (application/xml, text/xml)

Returns the status of the operation.

#### Sample Data

```
<boolean xmlns="http://schemas.microsoft.com/2003/10/Serialization/">true</boolean>
```

Example

Remarks

Models, ConfigurationName, and ConfigurationId are all members of ConfigInfo_DataCard. This operation can return an array of ConfigInfo_DataCards. See the Request samples.

See Also

[Data Card Resource Group](PDM%20Pro%20API_ws~g-b9fd019f-fc85-4753-9377-bf3fb3a1a5f8.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
