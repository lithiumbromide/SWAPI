---
title: "CreateProject Method (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "CreateProject"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~CreateProject.html"
---

# CreateProject Method (IPDMWConnection)

Creates a new project.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateProject( _
   ByVal Name As System.String, _
   ByVal Description As System.String, _
   ByVal Parent As System.String _
) As PDMWProject
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection
Dim Name As System.String
Dim Description As System.String
Dim Parent As System.String
Dim value As PDMWProject

value = instance.CreateProject(Name, Description, Parent)
```

### C#

```csharp
PDMWProject CreateProject(
   System.string Name,
   System.string Description,
   System.string Parent
)
```

### C++/CLI

```cpp
PDMWProject^ CreateProject(
   System.String^ Name,
   System.String^ Description,
   System.String^ Parent
)
```

### Parameters

- `Name`: Name of new project
- `Description`: Description of new project
- `Parent`: Name of parent project of new project or an empty string if the new project is at the root level

### Return Value

[IPDMWProject](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject.html) object

## VBA Syntax

See [PDMWConnection::CreateProject](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~CreateProject.html).

## Remarks

Only a vault administrator can use this method.

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)
[IPDMWConnection::DeleteProject Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~DeleteProject.html)
[IPDMWProject::SetUserPermissions Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~SetUserPermissions.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
