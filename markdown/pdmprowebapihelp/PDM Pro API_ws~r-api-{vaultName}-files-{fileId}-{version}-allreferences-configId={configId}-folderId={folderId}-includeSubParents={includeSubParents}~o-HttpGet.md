---
title: "api/{vaultName}/files/{fileId}/{version}/allreferences?configId={configId}&folderId={folderId}&includeSubParents={includeSubParents} (Get)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-{version}-allreferences-configId={configId}-folderId={folderId}-includeSubParents={includeSubParents}"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-{version}-allreferences-configId={configId}-folderId={folderId}-includeSubParents={includeSubParents}~o-HttpGet.html"
---

# api/{vaultName}/files/{fileId}/{version}/allreferences?configId={configId}&folderId={folderId}&includeSubParents={includeSubParents} (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/files/{fileId}/{version}/allreferences?configId={configId}&folderId={folderId}&includeSubParents={includeSubParents} |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}/{version}/allreferences?configId={configId}&folderId={folderId}&includeSubParents={includeSubParents} (Get) |
| --- |

Description

GET: api/{VaultName}/files/{FileID}/{Version}/allreferences Get all file references

Gets the reference tree of the specified file.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (Required URI parameter) Vault name | string |
| fileId | (Required URI parameter) File ID | integer |
| version | (Required URI parameter) Version | integer |
| configId | (URI parameter) Config ID (default value is -1) | integer |
| folderId | (URI parameter) Folder ID (default value is 0) | integer |
| includeSubParents | (URI parameter) Whether to include sub parents (default value is false) | boolean |
| File | (Response) A FileInfo object that consists of: File object that consists of: FileId (integer) File Name (string) Folder object that consists of: FolderId (integer) FolderPath Version (integer) Config object that consists of : ConfigurationName (string) ConfigurationId (integer) Member of FileRef model | FileInfo |
| IsCyclic | (Response) Whether the file reference is self-referential Member of FileRef model | boolean |
| IsToolbox | (Response) Whether the file reference is a toolbox item Member of FileRef model | integer |
| ObjectType | (Response) PweObjectType model; one of: ObjType_NoObject = 0 ObjType_File = 1 ObjType_InternalComponent = 2 ObjType_SavedBOM = 3 ObjType_Item = 4 ObjType_CutListItem = 5 Member of FileRef model | PweObjectType |
| Warnings | (Response) An array of BaseWarningModels; each BaseWarningModel consists of: Message (string) IsBlocking (boolean) IsError (boolean) Member of FileRef model | Collection of BaseWarningModel |
| References | (Response) The file reference's references; an array of FileRefs; each FileRef consists of: File (FileInfo) IsCyclic (boolean) IsToolbox (integer) ObjectType (PweObjectType) Warnings (Array of BaseWarningModels) References (Array of FileRefs) Member of FileRef model | Collection of FileRef |

Response (application/json)

Response (text/json)

Response (application/xml)

Response (text/xml)

Remarks

This operation can return multiple FileRef objects.

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
