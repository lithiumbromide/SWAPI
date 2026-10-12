---
title: "api/{vaultName}/bom/{bomTypeId}/{fileId}/{version}/{folderId}/computed?configId={configId}&latest={latest} (Get)"
project: ""
interface: "r-api-{vaultName}-bom-{bomTypeId}-{fileId}-{version}-{folderId}-computed-configId={configId}-latest={latest}"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-bom-{bomTypeId}-{fileId}-{version}-{folderId}-computed-configId={configId}-latest={latest}~o-HttpGet.html"
---

# api/{vaultName}/bom/{bomTypeId}/{fileId}/{version}/{folderId}/computed?configId={configId}&latest={latest} (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/bom/{bomTypeId}/{fileId}/{version}/{folderId}/computed?configId={configId}&latest={latest} |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > BOM Resource Group : api/{vaultName}/bom/{bomTypeId}/{fileId}/{version}/{folderId}/computed?configId={configId}&latest={latest} (Get) |
| --- |

Description

GET: api/{VaultName}/bom/{BomTypeId}/{FileID}/{Version}/{FolderID}/weldmentcutlist or api/{VaultName}/bom/{BomTypeId}/{FileID}/{Version}/{FolderID}/computed Get computed BOM

Gets the computed BOM.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required in URI) | string |
| bomTypeId | (URI parameter) BOM type ID (required in URI) | integer |
| fileId | (URI parameter) File ID (required in URI) | integer |
| version | (URI parameter) Version (required in URI) | integer |
| folderId | (URI parameter) Folder ID (required in URI) | integer |
| configId | (URI parameter) Configuration ID (default is -1) | integer |
| latest | (URI parameter) Whether the latest version (default is false) | boolean |
| Columns | (Response) Array of BOMColumns; each BOMColumn consists of: ColumnNo (integer) ColumnName (string) Member of ComputedBOM model | Collection of BOMColumn |
| File | (Response) BOMRef consists of: File (BOMRow) References (Collection of BOMRef) Member of ComputedBOM model | BOMRef |

Response (application/json)

Response (text/json)

Response (application/xml)

Response (text/xml)

See Also

[BOM Resource Group](PDM%20Pro%20API_ws~g-10274b3f-586c-4202-adb7-851ebf0c973b.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
