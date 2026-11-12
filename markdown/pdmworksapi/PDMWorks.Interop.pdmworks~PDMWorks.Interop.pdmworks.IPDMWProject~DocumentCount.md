---
title: "DocumentCount Property (IPDMWProject)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWProject"
member: "DocumentCount"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~DocumentCount.html"
---

# DocumentCount Property (IPDMWProject)

Gets the number of documents in this project.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DocumentCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWProject
Dim value As System.Integer

value = instance.DocumentCount
```

### C#

```csharp
System.int DocumentCount {get;}
```

### C++/CLI

```cpp
property System.int DocumentCount {
   System.int get();
}
```

### Property Value

Number of documents in this project

## VBA Syntax

See [PDMWProject::DocumentCount](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWProject~DocumentCount.html).

## See Also

[IPDMWProject Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject.html)
[IPDMWProject Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject_members.html)
[IPDMWProject::DocumentList Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~DocumentList.html)
[IDPMWProject::Documents Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~Documents.html)

## Availability

SOLIDWORKS Workgroup PDM 2007 FCS
