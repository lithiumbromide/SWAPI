---
title: "api/{vaultName}/files/{fileId}/{version}/{configId}/{folderId}/whereused?anyVersion={anyVersion} (Get)"
project: ""
interface: "r-api-{vaultName}-files-{fileId}-{version}-{configId}-{folderId}-whereused-anyVersion={anyVersion}"
member: "o-HttpGet"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-{version}-{configId}-{folderId}-whereused-anyVersion={anyVersion}~o-HttpGet.html"
---

# api/{vaultName}/files/{fileId}/{version}/{configId}/{folderId}/whereused?anyVersion={anyVersion} (Get)

PDM Pro API Web Service

| Get | api/{vaultName}/files/{fileId}/{version}/{configId}/{folderId}/whereused?anyVersion={anyVersion} |
| --- | --- |

Collapse All Expand All

| PDM Pro API Web Service > File Resource Group : api/{vaultName}/files/{fileId}/{version}/{configId}/{folderId}/whereused?anyVersion={anyVersion} (Get) |
| --- |

Description

GET: api/{VaultName}/files/{FileID}/{Version}/whereused Get file where usedGets the parent files where the specified file is used.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (Required URI Parameter) Vault name | string |
| fileId | (Required URI Parameter) File ID | integer |
| version | (Required URI Parameter) File version | integer |
| configId | (URI Parameter) Config ID, default value is -1 | integer |
| folderId | (URI Parameter) Folder ID, default value is 0 | integer |
| anyVersion | (URI Parameter) Whether any version, default value is false | boolean |
| File | (Response) FileInfo object: File object: FileID: integer FileName: string Folder object: FolderID: integer FolderPath: string Version: integer Config object: ConfigurationName: string ConfigurationId: integer (Member of FileRef Model) | FileInfo |
| IsCyclic | (Response) Whether is self-referential (Member of FileRef Model) | boolean |
| IsToolbox | (Response) 1 if a Toolbox file, 0 if not (Member of FileRef Model) | integer |
| ObjectType | (Response) Object type: ObjType_NoObject = 0 ObjType_File = 1 ObjType_InternalComponent = 2 ObjType_SavedBOM = 3 ObjType_Item = 4 ObjType_CutListItem = 5 (Member of FileRef model) | PweObjectType |
| Warnings | (Response) An array of BaseWarningModels, each containing: Message = string IsBlocking = boolean IsError = boolean (Member of FileRef model) | Collection of BaseWarningModel |
| References | (Response) An array of FileRefs, each containing: File Info: File: FileId = integer FileName = string Folder: FolderId = integer FolderPath = string Version = integer Config: ConfigurationName = string ConfigurationId = integer IsCyclic: whether self-referential IsToolbox: 1 if in Toolbox, 0 if not ObjectType: PweObjectType containing one of: ObjType_NoObject = 0 ObjType_File = 1 ObjType_InternalComponent = 2 ObjType_SavedBOM = 3 ObjType_Item = 4 ObjType_CutListItem = 5 Warnings: Array of BaseWarningModels, each containing: Message = string IsBlocking = boolean IsError = boolean References: Array of FileRefs, each containing (see above for details): FileInfo IsCyclic IsToolbox ObjectType Warnings References | Collection of FileRef |

Response (application/json)

Response (text/json)

Response (application/xml)

Response (text/xml)

See Also

[File Resource Group](PDM%20Pro%20API_ws~g-0e45981b-3619-4486-b05d-cc362f26dd7c.html) | [PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
