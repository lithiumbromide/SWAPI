---
title: "BOM Resource Group"
project: ""
interface: "g-10274b3f-586c-4202-adb7-851ebf0c973b"
member: ""
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~g-10274b3f-586c-4202-adb7-851ebf0c973b.html"
---

# BOM Resource Group

PDM Pro API Web Service

BOM Resource Group

Spacing

Collapse All

Expand All

| PDM Pro API Web Service : BOM Resource Group |
| --- |

Description

This resource group consists of BOM HTTP requests. You must send

[api/{vaultName}/authenticate](PDM%20Pro%20API_ws~r-api-%7BvaultName%7D-authenticate~o-HttpPost.html)

before calling these. See

[Getting Started](GettingStarted.html)

.

Operations

| Get | api/{vaultName}/bom/{bomDocumentId}/{version}/{folderId}/named GET: api/{VaultName}/bom/{BomDocumentId}/{Version}/{FolderID}/named Get named bom Gets the specified BOM. |
| --- | --- |
| Get | api/{vaultName}/bom/{bomTypeId}/{fileId}/{version}/{folderId}/computed?configId={configId}&latest={latest} GET: api/{VaultName}/bom/{BomTypeId}/{FileID}/{Version}/{FolderID}/weldmentcutlist or api/{VaultName}/bom/{BomTypeId}/{FileID}/{Version}/{FolderID}/computed Get computed BOM Gets the computed BOM. |
| Get | api/{vaultName}/bom/{bomTypeId}/{fileId}/{version}/{folderId}/weldmentcutlist?configId={configId}&latest={latest} GET: api/{VaultName}/bom/{BomTypeId}/{FileID}/{Version}/{FolderID}/weldmentcutlist or api/{VaultName}/bom/{BomTypeId}/{FileID}/{Version}/{FolderID}/computed Get computed BOM Gets the weldment cut list BOM. |

See Also

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
