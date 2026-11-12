---
title: "CreateSubProject Method (IPDMWProject)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWProject"
member: "CreateSubProject"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~CreateSubProject.html"
---

# CreateSubProject Method (IPDMWProject)

Creates a child project to this project.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSubProject( _
   ByVal Name As System.String, _
   ByVal Description As System.String _
) As PDMWProject
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWProject
Dim Name As System.String
Dim Description As System.String
Dim value As PDMWProject

value = instance.CreateSubProject(Name, Description)
```

### C#

```csharp
PDMWProject CreateSubProject(
   System.string Name,
   System.string Description
)
```

### C++/CLI

```cpp
PDMWProject^ CreateSubProject(
   System.String^ Name,
   System.String^ Description
)
```

### Parameters

- `Name`: New child project name
- `Description`: Child project description

### Return Value

Newly created [IPDMWProject](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject.html) object

## VBA Syntax

See [PDMWProject::CreateSubProject](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWProject~CreateSubProject.html).

## See Also

[IPDMWProject Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject.html)
[IPDMWProject Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject_members.html)
[IPDMWProject::SubProjects Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~SubProjects.html)

## Availability

SOLIDWORKS Workgroup PDM 2005 FCS
