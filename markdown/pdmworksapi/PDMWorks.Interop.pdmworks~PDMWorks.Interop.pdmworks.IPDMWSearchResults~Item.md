---
title: "Item Property (IPDMWSearchResults)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchResults"
member: "Item"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResults~Item.html"
---

# Item Property (IPDMWSearchResults)

Gets the specified search result.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Default Property Item( _
   ByVal Index As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchResults
Dim Index As System.Object
Dim value As System.Object

value = instance.Item(Index)
```

### C#

```csharp
System.object this[
   System.object Index
]; {get;}
```

### C++/CLI

```cpp
property System.Object^ default [System.Object^] {
   System.Object^ get(System.Object^ Index);
}
```

### Parameters

- `Index`: Number or name indicating which search result to get

### Property Value

[IPDMSearchResult](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult.html)

## VBA Syntax

See [PDMWSearchResults::Item](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchResults~Item.html).

## See Also

[IPDMWSearchResults Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResults.html)
[IPDMWSearchResults Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResults_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
