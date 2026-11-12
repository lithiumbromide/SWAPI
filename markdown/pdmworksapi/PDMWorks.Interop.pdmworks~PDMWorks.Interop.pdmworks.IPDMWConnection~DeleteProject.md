---
title: "DeleteProject Method (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "DeleteProject"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~DeleteProject.html"
---

# DeleteProject Method (IPDMWConnection)

Deletes the specified project.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DeleteProject( _
   ByVal Name As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection
Dim Name As System.String

instance.DeleteProject(Name)
```

### C#

```csharp
void DeleteProject(
   System.string Name
)
```

### C++/CLI

```cpp
void DeleteProject(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of project to delete

## VBA Syntax

See [PDMWConnection::DeleteProject](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~DeleteProject.html).

## Remarks

Only a vault administrator can use this method.

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)
[IPDMWConnection::CreateProject](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~CreateProject.html)
[IPDMWProject::SetUserPermissions](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~SetUserPermissions.html)
[IPDMWProject::CreateSubProject Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~CreateSubProject.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
