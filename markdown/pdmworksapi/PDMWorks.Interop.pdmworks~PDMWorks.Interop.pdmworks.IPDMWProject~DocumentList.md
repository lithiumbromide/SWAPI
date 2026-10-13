---
title: "DocumentList Property (IPDMWProject)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWProject"
member: "DocumentList"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~DocumentList.html"
---

# DocumentList Property (IPDMWProject)

Gets a the list of document names for this project.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DocumentList As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWProject
Dim value As System.Object

value = instance.DocumentList
```

### C#

```csharp
System.object DocumentList {get;}
```

### C++/CLI

```cpp
property System.Object^ DocumentList {
   System.Object^ get();
}
```

### Property Value

Array document names

## VBA Syntax

See [PDMWProject::DocumentList](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWProject~DocumentList.html).

## See Also

[IPDMWProject Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject.html)
[IPDMWProject Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject_members.html)
[IPDMWProject::DocumentCount Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~DocumentCount.html)
[IPDMWProject::Documents Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~Documents.html)

## Availability

SOLIDWORKS Workgroup PDM 2007 FCS
