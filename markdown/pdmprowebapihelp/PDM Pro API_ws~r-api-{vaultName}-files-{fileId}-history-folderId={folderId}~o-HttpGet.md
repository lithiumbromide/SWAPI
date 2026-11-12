---
title: "api/{vaultName}/files/{fileId}/history?folderId={folderId} (Get)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-history-folderId={folderId}"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-history-folderId={folderId}~o-HttpGet.html"
---

# api/{vaultName}/files/{fileId}/history?folderId={folderId} (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/files/{fileId}/history?folderId={folderId} |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}/history?folderId={folderId} (Get) |
| --- |

Description

Gets a specified file's history.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (Required URI Parameter) Vault name | string |
| fileId | (Required URI Parameter) File ID | integer |
| folderId | (URI Parameter) Folder ID, default is 0 | integer |
| DocumentId | (Response) Document ID (Member of HistoryBase model) | integer |
| Version | (Response) File version (Member of HistoryBase model) | integer |
| User | (Response) UserInfo: UserName: string UserId: integer (Member of HistoryBase model) | UserInfo |
| Date | (Response) Date (Member of HistoryBase model) | date |
| HistoryType | (Response) HistoryType: None = 0 Share = 1 Rename = 2 Move = 3 Rollback = 4 Delete = 5 Version = 7 Label = 9 Transition = 10 Revision = 11 ColdStore = 12 VerFreeVar = 18 PendingState = 20 ParallelState = 21 VersionOverwrite = 22 Branch = 23 DocUndoLock = 24 DocBranchMerge = 25 DocLock = 26 DocUndoLock2 = 27 (Member of HistoryBase model) | HistoryType |
| Event | (Response) Event (Member of HistoryBase model) | string |
| Comment | (Response) Comment (Member of HistoryBase model) | string |

Response (application/json, text/json, application/xml, text/xml)

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
