---
title: "Owner Property (IPDMWSearchResult)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchResult"
member: "Owner"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult~Owner.html"
---

# Owner Property (IPDMWSearchResult)

Gets the owner of the document in the search results.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Owner As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchResult
Dim value As System.String

value = instance.Owner
```

### C#

```csharp
System.string Owner {get;}
```

### C++/CLI

```cpp
property System.String^ Owner {
   System.String^ get();
}
```

### Property Value

Owner of document

## VBA Syntax

See [PDMWSearchResult::Owner](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchResult~Owner.html).

## See Also

[IPDMWSearchResult Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult.html)
[IPDMWSearchResult Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
