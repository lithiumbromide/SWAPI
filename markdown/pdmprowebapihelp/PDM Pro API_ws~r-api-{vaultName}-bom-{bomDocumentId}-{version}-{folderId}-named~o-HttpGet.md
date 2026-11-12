---
title: "api/{vaultName}/bom/{bomDocumentId}/{version}/{folderId}/named (Get)"
project: ""
interface: "r-api-{vaultName}-bom-{bomDocumentId}-{version}-{folderId}-named"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-bom-{bomDocumentId}-{version}-{folderId}-named~o-HttpGet.html"
---

# api/{vaultName}/bom/{bomDocumentId}/{version}/{folderId}/named (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/bom/{bomDocumentId}/{version}/{folderId}/named |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > BOM Resource Group : api/{vaultName}/bom/{bomDocumentId}/{version}/{folderId}/named (Get) |
| --- |

Description

GET: api/{VaultName}/bom/{BomDocumentId}/{Version}/{FolderID}/named Get named bom

Gets the specified BOM.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required in URI) | string |
| bomDocumentId | (URI parameter) BOM ID (required in URI) | integer |
| version | (URI parameter) Version (required in URI) | integer |
| folderId | (URI parameter) Folder ID (required in URI) | integer |
| Columns | (Response) Array of BOMColumns; each BOMColumn consists of: ColumnNo (integer) ColumnName (string) Member of NamedBOM model | Collection of BOMColumn |
| Values | (Response) Array of NamedBOMRows; each NamedBOMRow consists of: RowNo (integer) ColumnNo (integer) Value (string) Member of NamedBOM model | Collection of NamedBOMRow |

Response (application/json, text/json)

#### Sample Data

```
{
  "Columns": [
    {
      "ColumnNo": 1,
      "ColumnName": "sample string 2"
    },
    {
      "ColumnNo": 1,
      "ColumnName": "sample string 2"
    }
  ],
  "Values": [
    {
      "RowNo": 1,
      "ColumnNo": 2,
      "Value": "sample string 3"
    },
    {
      "RowNo": 1,
      "ColumnNo": 2,
      "Value": "sample string 3"
    }
  ]
}
```

Response (application/xml, text/xml)

#### Sample Data

```
<NamedBOM xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <Columns>
    <BOMColumn>
      <ColumnName>sample string 2</ColumnName>
      <ColumnNo>1</ColumnNo>
    </BOMColumn>
    <BOMColumn>
      <ColumnName>sample string 2</ColumnName>
      <ColumnNo>1</ColumnNo>
    </BOMColumn>
  </Columns>
  <Values>
    <NamedBOMRow>
      <ColumnNo>2</ColumnNo>
      <RowNo>1</RowNo>
      <Value>sample string 3</Value>
    </NamedBOMRow>
    <NamedBOMRow>
      <ColumnNo>2</ColumnNo>
      <RowNo>1</RowNo>
      <Value>sample string 3</Value>
    </NamedBOMRow>
  </Values>
</NamedBOM>
```

See Also

[BOM Resource Group](PDM%20Pro%20API_ws~g-10274b3f-586c-4202-adb7-851ebf0c973b.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
