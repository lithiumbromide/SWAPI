---
title: "SubProjects Property (IPDMWProject)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWProject"
member: "SubProjects"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~SubProjects.html"
---

# SubProjects Property (IPDMWProject)

Gets the child projects for this project.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SubProjects As PDMWProjects
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWProject
Dim value As PDMWProjects

value = instance.SubProjects
```

### C#

```csharp
PDMWProjects SubProjects {get;}
```

### C++/CLI

```cpp
property PDMWProjects^ SubProjects {
   PDMWProjects^ get();
}
```

### Property Value

Collection of child [projects](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProjects.html) for this project

## VBA Syntax

See [PDMWProject::SubProjects](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWProject~SubProjects.html).

## See Also

[IPDMWProject Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject.html)
[IPDMWProject Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject_members.html)
[IPDMWProject::CreateSubProject Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~CreateSubProject.html)

## Availability

SOLIDWORKS Workgroup PDM 2005 SP1
