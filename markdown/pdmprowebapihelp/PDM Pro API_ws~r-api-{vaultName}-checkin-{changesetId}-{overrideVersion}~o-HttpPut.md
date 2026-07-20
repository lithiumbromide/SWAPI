---
title: "api/{vaultName}/checkin/{changesetId}/{overrideVersion} (Put)"
project: ""
interface: "r-api-{vaultName}-checkin-{changesetId}-{overrideVersion}"
member: "o-HttpPut"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-checkin-{changesetId}-{overrideVersion}~o-HttpPut.html"
---

# api/{vaultName}/checkin/{changesetId}/{overrideVersion} (Put)

PDM Pro API Web Service

| Put | api/{vaultName}/checkin/{changesetId}/{overrideVersion} |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Stage Resource Group : api/{vaultName}/checkin/{changesetId}/{overrideVersion} (Put) |
| --- |

Description

PUT: api/{vaultName}/checkin/{changesetId}/{overrideVersion=false} Check in files from the changeset

Checks in the specified changeset.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| changesetId | (URI parameter) Changeset ID (required) | integer |
| overrideVersion | (URI parameter) Whether to override the current versions of files (required) | boolean |
| DocumentIds | (Body parameter) Array of document IDs Member of CheckInModel model | Collection of integer |
| Comments | (Body parameter) Checkin comment Member of CheckInModel model | string |
| Version | (Response) A Version model that consists of: Major (integer) Minor (integer) Build (integer) Revision (integer) MajorRevision (integer) MinorRevision (integer) Member of HttpResponseMessage model | Version |
| Content | (Response) GUID of the check-in operation; use the GUID to query for the status of the operation (see api/{vaultName}/progress/{guid}/status ) Member of HttpResponseMessage model | HttpContent |
| StatusCode | (Response) Status code; see https://en.wikipedia.org/wiki/List_of_HTTP_status_codes Member of HttpResponseMessage model | HttpStatusCode |
| ReasonPhrase | (Response) Reason Member of HttpResponseMessage model | string |
| Headers | (Response) Collection of objects Member of HttpResponseMessage model | Collection of Object |
| RequestMessage | (Response) An HttpRequestMessage object that consists of: Version (Version model) Content (HttpContent object consisting of Headers array) Method (HttpMethod object consisting of Method string) RequestUri (URI) Headers (Array of objects) Properties (Dictionary of string [key] and Object [value] Member of HttpResponseMessage model | HttpRequestMessage |
| IsSuccessStatusCode | (Response) True if successful, false if not Member of HttpResponseMessage model | boolean |

Request (application/json, text/json)

The body parameter includes an array of document IDs and comments.

#### Sample Data

```
{
  "DocumentIds": [
    1,
    2
  ],
  "Comments": "sample string 1"
}
```

Request (application/xml, text/xml)

The body parameter includes an array of document IDs and comments.

#### Sample Data

```
<CheckInModel xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <Comments>sample string 1</Comments>
  <DocumentIds xmlns:d2p1="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
    <d2p1:int>1</d2p1:int>
    <d2p1:int>2</d2p1:int>
  </DocumentIds>
</CheckInModel>
```

Request (application/x-www-form-urlencoded)

The body parameter includes an array of document IDs and comments.

Example

[Modify File Datacards.postman_collection.json](Modify%20File%20Datacards.postman_collection.json)

See Also

[Stage Resource Group](PDM%20Pro%20API_ws~g-ab7aa0c7-6261-4685-9682-f6301732b3ab.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
