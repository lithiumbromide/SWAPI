---
title: "Document Property (IPDMWLink)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWLink"
member: "Document"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink~Document.html"
---

# Document Property (IPDMWLink)

Gets the document for this link.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Document As PDMWDocument
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWLink
Dim value As PDMWDocument

value = instance.Document
```

### C#

```csharp
PDMWDocument Document {get;}
```

### C++/CLI

```cpp
property PDMWDocument^ Document {
   PDMWDocument^ get();
}
```

### Property Value

[IPDMWDocument](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html) object for this link

## VBA Syntax

See [PDMWLink::Document](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWLink~Document.html).

## See Also

[IPDMWLink Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink.html)
[IPDMWLink Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
