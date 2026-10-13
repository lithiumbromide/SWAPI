---
title: "Getting Started"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: ""
member: ""
kind: "topic"
source: "pdmworksapi/GettingStarted-pdmworksapi.html"
---

# Getting Started

This topic contains the following information:

- [Application Basics](#ApplicationBasics)
- [Error Handling](#ErrorHandling)
- [Obsolete APIs](#ObsoleteAPIs)

##### Application Basics

Writing a SOLIDWORKS Workgroup PDM API application typically involves:

1. Instantiating a SOLIDWORKS Workgroup PDM connection and logging in.

  When you connect and log in to SOLIDWORKS Workgroup PDM via the API, the SOLIDWORKS Workgroup PDM API object model is implemented as a snapshot of what is in the vault at that time. If the state of the vault changes either through the user interface or the API (for example, by a check in, the creation of a new project, the addition of a note, and so on), you must call [IPDMWConnection::Refresh](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~Refresh.html) to ensure that subsequent API calls return the most current data.

  **IMPORTANT**: Because [IPDMWConnection::CheckIn](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~CheckIn.html) is dependent on **pdmworks_libFNP.dll**, you must ensure that your application can find this DLL. The simplest way for your application to find **pdmworks_libFNP.dll** is to add its location to the PATH environmental variable. See [Microsoft Corp's Dynamic-Link Library Search Order](http://msdn.microsoft.com/en-us/library/windows/desktop/ms682586(v=vs.85).aspx) for details.

  SOLIDWORKS Workgroup PDM API contains several methods that change the state of the SOLIDWORKS Workgroup PDM vault; however, most of the exposed object model contains read-only properties. Therefore, a typical SOLIDWORKS Workgroup PDM application displays and analyzes vault data rather than updates it.
2. Getting and reading the various VB-compatible collections that represent:

  - projects,
  - documents in those projects, and
  - those projects' configurations, references, and other properties.
3. Logging out.

The SOLIDWORKS Workgroup PDM API exposes VB-compatible collections for easy iteration of similar objects using the For Each...Next statement. For example, to iterate over the set of documents in a vault, you could use the following code fragment:

```vb
Dim connection As PDMWConnection
Dim allDocs As PDMWDocuments
Dim document As PDMWDocument

Sub main()
Set connection = CreateObject("PDMWorks.PDMWConnection")
connection.Login "pdmwadmin", "pdmwadmin", "vault_server_name"
Set allDocs = connection.documents

For Each document In allDocs
     'Access each PDMWDocument here
Next
connection.Logout

End Sub
```

[Back to top](#Top)

##### Error Handling

When appropriate, the SOLIDWORKS Workgroup PDM API returns an error status code, for example, when performing [IPDMWProperties::Update](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties~Update.html). Sometimes, directly returning a status code is not possible, for example, when retrieving a document via [IPDMWConnection::GetSpecificDocument](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~GetSpecificDocument.html).

If an error status is returned, it is in the form of a SOLIDWORKS Workgroup PDM error code (a 32-bit value). This code returns 0 for success and non-0 for error.

SOLIDWORKS recommends that you use the intrinsic Visual Basic Err object to get rich error information. In this case, the Err.number field does not correspond directly to the SOLIDWORKS Workgroup PDM error code, but mappings back to the error code are provided. The Err.Description field is filled with a descriptive text field indicating the error. In this way, better tracing of errors can be done through the Err object.

In Visual Basic 5.0, error handling can easily be accomplished with the On Error Resume Next statement. For example:

```vb
On Error Resume Next
Dim conn
Set conn = CreateObject(PDMWorks.PDMWConnection)
conn.Login user, incorrect password, vault
Err.number contains the error number
Err.description contains the appropriate error description
```

[Back to top](#Top)

##### Obsolete APIs

SOLIDWORKS Workgroup PDM is continually enhancing its APIs. In most instances, when an existing API is superseded by a new API, the new API has the same name as the existing API followed by a number. A higher number indicates a more recent API.

Superseded APIs are not supported. Help topics for superseded APIs are marked as obsolete.

SOLIDWORKS recommends that you use the newest APIs in your code, and, whenever possible, update your existing code to use the newest APIs.

[Back to top](#Top)
