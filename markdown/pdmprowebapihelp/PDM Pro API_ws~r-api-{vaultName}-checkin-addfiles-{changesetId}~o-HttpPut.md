---
title: "api/{vaultName}/checkin/addfiles/{changesetId} (Put)"
project: ""
interface: "r-api-{vaultName}-checkin-addfiles-{changesetId}"
member: "o-HttpPut"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-checkin-addfiles-{changesetId}~o-HttpPut.html"
---

# api/{vaultName}/checkin/addfiles/{changesetId} (Put)

PDM Pro API Web Service

| Put | api/{vaultName}/checkin/addfiles/{changesetId} |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Stage Resource Group : api/{vaultName}/checkin/addfiles/{changesetId} (Put) |
| --- |

Description

PUT: api/{vaultname}/checkin/addfiles/{changesetId=0} Upload files or document ids to changeset to the check in operation

Adds files to a changeset for checkin. (See**Remarks**)

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| changesetId | (URI and Response parameter) Changeset ID = 0 (URI required) | integer |
| References | (Response) Array of FileInfo objects; each FileInfo consists of: File (File object that consists of: FileId (integer) FileName (string) ) Folder (Folder object that consist of: FolderId (integer) FolderPath (string) ) Version (integer) Config (Config object that consists of: ConfigurationName (string) ConfigurationId (integer) ) | Collection of FileInfo |

Response (application/json, text/json)

This request returns a new changeset ID and file references.

#### Sample Data

```
{
  "ChangesetId": 1,
  "References": [
    {
      "File": {
        "FileId": 1,
        "FileName": "sample string 2"
      },
      "Folder": {
        "FolderId": 1,
        "FolderPath": "sample string 2"
      },
      "Version": 1,
      "Config": {
        "ConfigurationName": "sample string 1",
        "ConfigurationId": 2
      }
    },
    {
      "File": {
        "FileId": 1,
        "FileName": "sample string 2"
      },
      "Folder": {
        "FolderId": 1,
        "FolderPath": "sample string 2"
      },
      "Version": 1,
      "Config": {
        "ConfigurationName": "sample string 1",
        "ConfigurationId": 2
      }
    }
  ]
}
```

Response (application/xml, text/xml)

This request returns a new changeset ID and file references.

#### Sample Data

```
<UploadModel xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <ChangesetId>1</ChangesetId>
  <References>
    <FileInfo>
      <Config>
        <ConfigurationId>2</ConfigurationId>
        <ConfigurationName>sample string 1</ConfigurationName>
      </Config>
      <File>
        <FileId>1</FileId>
        <FileName>sample string 2</FileName>
      </File>
      <Folder>
        <FolderId>1</FolderId>
        <FolderPath>sample string 2</FolderPath>
      </Folder>
      <Version>1</Version>
    </FileInfo>
    <FileInfo>
      <Config>
        <ConfigurationId>2</ConfigurationId>
        <ConfigurationName>sample string 1</ConfigurationName>
      </Config>
      <File>
        <FileId>1</FileId>
        <FileName>sample string 2</FileName>
      </File>
      <Folder>
        <FolderId>1</FolderId>
        <FolderPath>sample string 2</FolderPath>
      </Folder>
      <Version>1</Version>
    </FileInfo>
  </References>
</UploadModel>
```

Example

[Check in SOLIDWORKS Files in PDM Vault.postman_collection.json](Check%20in%20SOLIDWORKS%20Files%20%20in%20PDM%20Vault.postman_collection.json)

|

[Program.cs](Program.cs)

|

[Modify File Datacards.postman_collection.json](Modify%20File%20Datacards.postman_collection.json)

Remarks

This request also requires a binary Body that consists of the binary files to add to the changeset. Drag/drop the JSON example to Postman and inspect the Body of the HTTP request. The**Program.cs**example creates the binary file that you can upload using this request.

Send this HTTP request with a changeset ID of 0. If successful, it will return a new changeset ID which you will use in further requests:[api/{vaultName}/checkin/buildtree/{changesetId} (Get)](PDM%20Pro%20API_ws~r-api-{vaultName}-checkin-buildtree-{changesetId}~o-HttpGet.html)and[api/{vaultName}/checkin/{changesetId}/{overrideVersion} (Put)](PDM%20Pro%20API_ws~r-api-{vaultName}-checkin-{changesetId}-{overrideVersion}~o-HttpPut.html)

See Also

[Stage Resource Group](PDM%20Pro%20API_ws~g-ab7aa0c7-6261-4685-9682-f6301732b3ab.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
