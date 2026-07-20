---
title: "Data Card Resource Group"
project: ""
interface: "g-b9fd019f-fc85-4753-9377-bf3fb3a1a5f8"
member: ""
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~g-b9fd019f-fc85-4753-9377-bf3fb3a1a5f8.html"
---

# Data Card Resource Group

PDM Pro API Web Service

Data Card Resource Group

Spacing

Collapse All

Expand All

| PDM Pro API Web Service : Data Card Resource Group |
| --- |

Description

This resource group consists of Data card HTTP requests. You must send

[api/{vaultName}/authenticate](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-authenticate~o-HttpPost.html)

before calling these. See

[Getting Started](GettingStarted.html)

.

Operations

| Post | api/{vaultName}/files/{fileId}/{folderId}/datacard Saves the data card for the specified file |
| --- | --- |
| Get | api/{vaultName}/files/{fileId}/{version}/datacard?folderId={folderId} GET: api/{VaultName}/files/{FileID}/{Version}/datacard Get file data card Gets the data card for the specified file, file version, and vault. |
| Post | api/{vaultName}/files/{fileId}/datacard?folderId={folderId} Saves the specified data card variables to the specified file. |
| Get | api/{vaultName}/folders/{folderId}/datacard GET: api/{VaultName}/folders/{FolderID}/datacard Get folder data card Gets the data card for the specified folder and vault. |

See Also

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
