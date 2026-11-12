---
title: "api/{vaultName}/files/{fileId}/bominfo?folderId={folderId} (Get)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-bominfo-folderId={folderId}"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-bominfo-folderId={folderId}~o-HttpGet.html"
---

# api/{vaultName}/files/{fileId}/bominfo?folderId={folderId} (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/files/{fileId}/bominfo?folderId={folderId} |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}/bominfo?folderId={folderId} (Get) |
| --- |

Description

GET: api/{VaultName}/files/{FileID}/bominfo Get file BOM info

Gets the BOM information for the specified file.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (Required URI parameter) Vault name | string |
| fileId | (Required URI parameter) File ID | integer |
| folderId | (URI parameter) Folder ID (default value is 0) | integer |
| NamedBOM | (Response) A NamedBOMInfoList; each NamedBOMInfoList consists of: BOMList (array of NamedBOMInfo objects; each NamedBOMInfo consists of: Folder (Folder object that consists of FolderId (integer) and FolderPath (string)) Config (Config object that consists of ConfigurationName (string) and ConfigurationId (integer)) BOMId (integer) BOMName (string) VersionNo (integer) SavedBOM (boolean) Member of BOMInfo model | NamedBOMInfoList |
| ComputedBOM | (Response) A ComputedBOMInfoList; each ComputedBOMInfoList consists of: BOMList (array of ComputedBOMInfo objects; each ComputedBOMInfo consists of: Folder (Folder object that consists of FolderId (integer) and FolderPath (string)) Configs (Array of Config objects, each Config object consists of: ConfigurationName (string) ConfigurationId (integer) BOMId (integer) BOMName (string) Member of BOMInfo model | ComputedBOMInfoList |
| WeldmentCutlistBOM | (Response) A ComputedBOMInfoList; each ComputedBOMInfoList consists of: BOMList (array of ComputedBOMInfo objects; each ComputedBOMInfo consists of: Folder (Folder object that consists of FolderId (integer) and FolderPath (string)) Configs (Array of Config objects, each Config object consists of: ConfigurationName (string) ConfigurationId (integer) BOMId (integer) BOMName (string) Member of BOMInfo model | ComputedBOMInfoList |
| WeldmentBOM | (Response) A ComputedBOMInfoList; each ComputedBOMInfoList consists of: BOMList (array of ComputedBOMInfo objects; each ComputedBOMInfo consists of: Folder (Folder object that consists of FolderId (integer) and FolderPath (string)) Configs (Array of Config objects, each Config object consists of: ConfigurationName (string) ConfigurationId (integer) BOMId (integer) BOMName (string) Member of BOMInfo model | ComputedBOMInfoList |

Response (application/json, text/json)

#### Sample Data

```
{
  "NamedBOM": {
    "BOMList": [
      {
        "Folder": {
          "FolderId": 1,
          "FolderPath": "sample string 2"
        },
        "Config": {
          "ConfigurationName": "sample string 1",
          "ConfigurationId": 2
        },
        "BOMId": 1,
        "BOMName": "sample string 2",
        "VersionNo": 3,
        "SavedBOM": true
      },
      {
        "Folder": {
          "FolderId": 1,
          "FolderPath": "sample string 2"
        },
        "Config": {
          "ConfigurationName": "sample string 1",
          "ConfigurationId": 2
        },
        "BOMId": 1,
        "BOMName": "sample string 2",
        "VersionNo": 3,
        "SavedBOM": true
      }
    ]
  },
  "ComputedBOM": {
    "BOMList": [
      {
        "Folder": {
          "FolderId": 1,
          "FolderPath": "sample string 2"
        },
        "Configs": [
          {
            "ConfigurationName": "sample string 1",
            "ConfigurationId": 2
          },
          {
            "ConfigurationName": "sample string 1",
            "ConfigurationId": 2
          }
        ],
        "BOMId": 1,
        "BOMName": "sample string 2"
      },
      {
        "Folder": {
          "FolderId": 1,
          "FolderPath": "sample string 2"
        },
        "Configs": [
          {
            "ConfigurationName": "sample string 1",
            "ConfigurationId": 2
          },
          {
            "ConfigurationName": "sample string 1",
            "ConfigurationId": 2
          }
        ],
        "BOMId": 1,
        "BOMName": "sample string 2"
      }
    ]
  },
  "WeldmentCutlistBOM": {
    "BOMList": [
      {
        "Folder": {
          "FolderId": 1,
          "FolderPath": "sample string 2"
        },
        "Configs": [
          {
            "ConfigurationName": "sample string 1",
            "ConfigurationId": 2
          },
          {
            "ConfigurationName": "sample string 1",
            "ConfigurationId": 2
          }
        ],
        "BOMId": 1,
        "BOMName": "sample string 2"
      },
      {
        "Folder": {
          "FolderId": 1,
          "FolderPath": "sample string 2"
        },
        "Configs": [
          {
            "ConfigurationName": "sample string 1",
            "ConfigurationId": 2
          },
          {
            "ConfigurationName": "sample string 1",
            "ConfigurationId": 2
          }
        ],
        "BOMId": 1,
        "BOMName": "sample string 2"
      }
    ]
  },
  "WeldmentBOM": {
    "BOMList": [
      {
        "Folder": {
          "FolderId": 1,
          "FolderPath": "sample string 2"
        },
        "Configs": [
          {
            "ConfigurationName": "sample string 1",
            "ConfigurationId": 2
          },
          {
            "ConfigurationName": "sample string 1",
            "ConfigurationId": 2
          }
        ],
        "BOMId": 1,
        "BOMName": "sample string 2"
      },
      {
        "Folder": {
          "FolderId": 1,
          "FolderPath": "sample string 2"
        },
        "Configs": [
          {
            "ConfigurationName": "sample string 1",
            "ConfigurationId": 2
          },
          {
            "ConfigurationName": "sample string 1",
            "ConfigurationId": 2
          }
        ],
        "BOMId": 1,
        "BOMName": "sample string 2"
      }
    ]
  }
}
```

Response (application/xml, text/xml)

#### Sample Data

```
<BOMInfo xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <ComputedBOM>
    <BOMList>
      <ComputedBOMInfo>
        <BOMId>1</BOMId>
        <BOMName>sample string 2</BOMName>
        <Configs>
          <Config>
            <ConfigurationId>2</ConfigurationId>
            <ConfigurationName>sample string 1</ConfigurationName>
          </Config>
          <Config>
            <ConfigurationId>2</ConfigurationId>
            <ConfigurationName>sample string 1</ConfigurationName>
          </Config>
        </Configs>
        <Folder>
          <FolderId>1</FolderId>
          <FolderPath>sample string 2</FolderPath>
        </Folder>
      </ComputedBOMInfo>
      <ComputedBOMInfo>
        <BOMId>1</BOMId>
        <BOMName>sample string 2</BOMName>
        <Configs>
          <Config>
            <ConfigurationId>2</ConfigurationId>
            <ConfigurationName>sample string 1</ConfigurationName>
          </Config>
          <Config>
            <ConfigurationId>2</ConfigurationId>
            <ConfigurationName>sample string 1</ConfigurationName>
          </Config>
        </Configs>
        <Folder>
          <FolderId>1</FolderId>
          <FolderPath>sample string 2</FolderPath>
        </Folder>
      </ComputedBOMInfo>
    </BOMList>
  </ComputedBOM>
  <NamedBOM>
    <BOMList>
      <NamedBOMInfo>
        <BOMId>1</BOMId>
        <BOMName>sample string 2</BOMName>
        <Config>
          <ConfigurationId>2</ConfigurationId>
          <ConfigurationName>sample string 1</ConfigurationName>
        </Config>
        <Folder>
          <FolderId>1</FolderId>
          <FolderPath>sample string 2</FolderPath>
        </Folder>
        <SavedBOM>true</SavedBOM>
        <VersionNo>3</VersionNo>
      </NamedBOMInfo>
      <NamedBOMInfo>
        <BOMId>1</BOMId>
        <BOMName>sample string 2</BOMName>
        <Config>
          <ConfigurationId>2</ConfigurationId>
          <ConfigurationName>sample string 1</ConfigurationName>
        </Config>
        <Folder>
          <FolderId>1</FolderId>
          <FolderPath>sample string 2</FolderPath>
        </Folder>
        <SavedBOM>true</SavedBOM>
        <VersionNo>3</VersionNo>
      </NamedBOMInfo>
    </BOMList>
  </NamedBOM>
  <WeldmentBOM>
    <BOMList>
      <ComputedBOMInfo>
        <BOMId>1</BOMId>
        <BOMName>sample string 2</BOMName>
        <Configs>
          <Config>
            <ConfigurationId>2</ConfigurationId>
            <ConfigurationName>sample string 1</ConfigurationName>
          </Config>
          <Config>
            <ConfigurationId>2</ConfigurationId>
            <ConfigurationName>sample string 1</ConfigurationName>
          </Config>
        </Configs>
        <Folder>
          <FolderId>1</FolderId>
          <FolderPath>sample string 2</FolderPath>
        </Folder>
      </ComputedBOMInfo>
      <ComputedBOMInfo>
        <BOMId>1</BOMId>
        <BOMName>sample string 2</BOMName>
        <Configs>
          <Config>
            <ConfigurationId>2</ConfigurationId>
            <ConfigurationName>sample string 1</ConfigurationName>
          </Config>
          <Config>
            <ConfigurationId>2</ConfigurationId>
            <ConfigurationName>sample string 1</ConfigurationName>
          </Config>
        </Configs>
        <Folder>
          <FolderId>1</FolderId>
          <FolderPath>sample string 2</FolderPath>
        </Folder>
      </ComputedBOMInfo>
    </BOMList>
  </WeldmentBOM>
  <WeldmentCutlistBOM>
    <BOMList>
      <ComputedBOMInfo>
        <BOMId>1</BOMId>
        <BOMName>sample string 2</BOMName>
        <Configs>
          <Config>
            <ConfigurationId>2</ConfigurationId>
            <ConfigurationName>sample string 1</ConfigurationName>
          </Config>
          <Config>
            <ConfigurationId>2</ConfigurationId>
            <ConfigurationName>sample string 1</ConfigurationName>
          </Config>
        </Configs>
        <Folder>
          <FolderId>1</FolderId>
          <FolderPath>sample string 2</FolderPath>
        </Folder>
      </ComputedBOMInfo>
      <ComputedBOMInfo>
        <BOMId>1</BOMId>
        <BOMName>sample string 2</BOMName>
        <Configs>
          <Config>
            <ConfigurationId>2</ConfigurationId>
            <ConfigurationName>sample string 1</ConfigurationName>
          </Config>
          <Config>
            <ConfigurationId>2</ConfigurationId>
            <ConfigurationName>sample string 1</ConfigurationName>
          </Config>
        </Configs>
        <Folder>
          <FolderId>1</FolderId>
          <FolderPath>sample string 2</FolderPath>
        </Folder>
      </ComputedBOMInfo>
    </BOMList>
  </WeldmentCutlistBOM>
</BOMInfo>
```

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
