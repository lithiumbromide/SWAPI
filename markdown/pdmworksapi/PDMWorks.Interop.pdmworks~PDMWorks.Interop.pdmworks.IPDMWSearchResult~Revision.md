---
title: "Revision Property (IPDMWSearchResult)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchResult"
member: "Revision"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult~Revision.html"
---

# Revision Property (IPDMWSearchResult)

Gets the revision of the document in the search results.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Revision As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchResult
Dim value As System.String

value = instance.Revision
```

### C#

```csharp
System.string Revision {get;}
```

### C++/CLI

```cpp
property System.String^ Revision {
   System.String^ get();
}
```

### Property Value

Revision of the document

## VBA Syntax

See [PDMWSearchResult::Revision](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchResult~Revision.html).

## See Also

[IPDMWSearchResult Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult.html)
[IPDMWSearchResult Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
