---
title: "IsTopLevel Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "IsTopLevel"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~IsTopLevel.html"
---

# IsTopLevel Property (IPDMWDocument)

Gets whether this document is at the top-level project.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsTopLevel As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As System.Integer

value = instance.IsTopLevel
```

### C#

```csharp
System.int IsTopLevel {get;}
```

### C++/CLI

```cpp
property System.int IsTopLevel {
   System.int get();
}
```

### Property Value

0 if document is at the top-level project, 1 if not

## VBA Syntax

See [PDMWDocument::IsTopLevel](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~IsTopLevel.html).

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2004 FCS
