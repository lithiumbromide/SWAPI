---
title: "IPDMWConnection Interface Members"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection_members"
member: ""
kind: "members"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html"
---

# IPDMWConnection Interface Members

The following tables list the members exposed by [IPDMWConnection](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AdminDefinedProperties | Gets a collection of vault administrator-defined custom properties. |
| Property | DocumentList | Gets a the list of document names for the specified project. |
| Property | Documents | Gets the documents for the specified project. |
| Property | Groups | Gets a collection of groups. |
| Property | Projects | Gets the SOLIDWORKS Workgroup PDM projects. |
| Property | Statuses | Gets the defined lifecycle statuses. |
| Property | Users | Gets a collection of users. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | CheckIn | Checks the specified closed document into the vault. |
| Method | CreateGroup | Creates a new group. |
| Method | CreateProject | Creates a new project. |
| Method | CreateUser | Creates a new user. |
| Method | DeleteDocument | Deletes the specified document from the vault. |
| Method | DeleteGroup | Deletes the specified group. |
| Method | DeleteProject | Deletes the specified project. |
| Method | DeleteUser | Deletes the specified user. |
| Method | FreeCacheMemory | Frees the cache memory. |
| Method | GetSearchOptionsObject | Gets the search options. |
| Method | GetSpecificDocument | Gets the specified document and version of that document. |
| Method | Login | Logs the user into SOLIDWORKS Workgroup PDM and is required to initialize the IPDMWConnection object for subsequent method calls. |
| Method | Logout | Logs the user out of SOLIDWORKS Workgroup PDM and releases user-specific resources. |
| Method | Refresh | Refreshes the object model using the data in the vault. |
| Method | Search | Searches the vault using the specified search options. |

[Top](#topBookmark)

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[PDMWorks.Interop.pdmworks Namespace](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks_namespace.html)
