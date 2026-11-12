---
title: "Parent Property (IPDMWProject)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWProject"
member: "Parent"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~Parent.html"
---

# Parent Property (IPDMWProject)

Gets or sets the parent project.

## Syntax

### Visual Basic (Declaration)

```vb
Property Parent As PDMWProject
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWProject
Dim value As PDMWProject

instance.Parent = value

value = instance.Parent
```

### C#

```csharp
PDMWProject Parent {get; set;}
```

### C++/CLI

```cpp
property PDMWProject^ Parent {
   PDMWProject^ get();
   void set (    PDMWProject^ value);
}
```

### Property Value

[Parent project](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject.html)

## VBA Syntax

See [PDMWProject::Parent](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWProject~Parent.html).

## Remarks

Only a vault administrator can set the parent of a project.

## See Also

[IPDMWProject Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject.html)
[IPDMWProject Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
