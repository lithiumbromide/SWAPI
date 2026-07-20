---
title: "api/{vaultName}/files/{fileId}/{version}/datacard?folderId={folderId} (Get)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-{version}-datacard-folderId={folderId}"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-{version}-datacard-folderId={folderId}~o-HttpGet.html"
---

# api/{vaultName}/files/{fileId}/{version}/datacard?folderId={folderId} (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/files/{fileId}/{version}/datacard?folderId={folderId} |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Data Card Resource Group : api/{vaultName}/files/{fileId}/{version}/datacard?folderId={folderId} (Get) |
| --- |

Description

GET: api/{VaultName}/files/{FileID}/{Version}/datacard Get file data card

Gets the data card for the specified file, file version, and vault.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| fileId | (URI parameter) File ID (required) | integer |
| version | (URI parameter) File version (required) | integer |
| folderId | (URI parameter) Folder ID (default is 0) | integer |
| VariablesWithWriteAllConfigs | (Response) Array of IDs of variables with write-all configurations Member of DataCard model | Collection of integer |
| ConfigVarInfo | (Response) Array of ConfigInfo_DataCards; each ConfigInfo_DataCard consists of: Models (Array of VariableInfo_DataCards; each VariableInfo_DataCard consists of: ReadOnly (boolean) Multiline (boolean) VarId (integer) VarName (string) VarValue (string) VarType (one of: VarTypeNone = 0 VarTypeText = 1 VarTypeInt = 2 VarTypeFloat = 3 VarTypeBool = 4 VarTypeDate = 5 ) Mandatory (boolean) VersionFree (boolean) ) ConfigurationName (string) Configuration Id (integer) Member of DataCard model | Collection of ConfigInfo_DataCard |
| CardVariableInfo | (Response) Array of VariableExtraInfos; each VariableExtraInfo consists of: Variable Id (integer) VariableValueOptions (array of optional string values) Member of DataCard model | Collection of VariableExtraInfo |

Response (application/json, text/json)

#### Sample Data

```
{
  "VariablesWithWriteAllConfigs": [
    1,
    2
  ],
  "ConfigVarInfo": [
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
  ],
  "CardVariableInfo": [
    {
      "VariableId": 1,
      "VariableValueOptions": [
        "sample string 1",
        "sample string 2"
      ]
    },
    {
      "VariableId": 1,
      "VariableValueOptions": [
        "sample string 1",
        "sample string 2"
      ]
    }
  ]
}
```

Response (application/xml, text/xml)

#### Sample Data

```
<DataCard xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <CardVariableInfo>
    <VariableExtraInfo>
      <VariableId>1</VariableId>
      <VariableValueOptions xmlns:d4p1="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
        <d4p1:string>sample string 1</d4p1:string>
        <d4p1:string>sample string 2</d4p1:string>
      </VariableValueOptions>
    </VariableExtraInfo>
    <VariableExtraInfo>
      <VariableId>1</VariableId>
      <VariableValueOptions xmlns:d4p1="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
        <d4p1:string>sample string 1</d4p1:string>
        <d4p1:string>sample string 2</d4p1:string>
      </VariableValueOptions>
    </VariableExtraInfo>
  </CardVariableInfo>
  <ConfigVarInfo>
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
  </ConfigVarInfo>
  <VariablesWithWriteAllConfigs xmlns:d2p1="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
    <d2p1:int>1</d2p1:int>
    <d2p1:int>2</d2p1:int>
  </VariablesWithWriteAllConfigs>
</DataCard>
```

Example

[Modify File Datacards.postman_collection.json](Modify%20File%20Datacards.postman_collection.json)

See Also

[Data Card Resource Group](PDM%20Pro%20API_ws~g-b9fd019f-fc85-4753-9377-bf3fb3a1a5f8.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
