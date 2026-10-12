---
title: "Document Property (IPDMWSearchResult)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchResult"
member: "Document"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult~Document.html"
---

# Document Property (IPDMWSearchResult)

Gets the document in the search results.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Document As PDMWDocument
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchResult
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

[IPDMWDocument](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)

## VBA Syntax

See [PDMWSearchResult::Document](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchResult~Document.html).

## See Also

[IPDMWSearchResult Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult.html)
[IPDMWSearchResult Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
