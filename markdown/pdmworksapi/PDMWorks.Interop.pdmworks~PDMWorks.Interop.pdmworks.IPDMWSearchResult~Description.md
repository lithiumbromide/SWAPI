---
title: "Description Property (IPDMWSearchResult)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchResult"
member: "Description"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult~Description.html"
---

# Description Property (IPDMWSearchResult)

Gets the description of the document in the search results.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Description As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchResult
Dim value As System.String

value = instance.Description
```

### C#

```csharp
System.string Description {get;}
```

### C++/CLI

```cpp
property System.String^ Description {
   System.String^ get();
}
```

### Property Value

Description of the document

## VBA Syntax

See [PDMWSearchResult::Description](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchResult~Description.html).

## See Also

[IPDMWSearchResult Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult.html)
[IPDMWSearchResult Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
