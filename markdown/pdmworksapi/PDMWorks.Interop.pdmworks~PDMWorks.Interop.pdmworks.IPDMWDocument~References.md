---
title: "References Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "References"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~References.html"
---

# References Property (IPDMWDocument)

Gets the links to the documents referenced by this document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property References As PDMWLinks
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As PDMWLinks

value = instance.References
```

### C#

```csharp
PDMWLinks References {get;}
```

### C++/CLI

```cpp
property PDMWLinks^ References {
   PDMWLinks^ get();
}
```

### Property Value

Collection of [links](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLinks.html) to documents referenced by this document

## VBA Syntax

See [PDMWDocument::References](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~References.html).

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
