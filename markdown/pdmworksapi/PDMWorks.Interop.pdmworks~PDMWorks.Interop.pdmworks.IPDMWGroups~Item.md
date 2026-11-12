---
title: "Item Property (IPDMWGroups)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWGroups"
member: "Item"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroups~Item.html"
---

# Item Property (IPDMWGroups)

Gets the specified group.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Default Property Item( _
   ByVal Index As System.Object _
) As PDMWGroup
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWGroups
Dim Index As System.Object
Dim value As PDMWGroup

value = instance.Item(Index)
```

### C#

```csharp
PDMWGroup this[
   System.object Index
]; {get;}
```

### C++/CLI

```cpp
property PDMWGroup^ default [System.Object^] {
   PDMWGroup^ get(System.Object^ Index);
}
```

### Parameters

- `Index`: Number indicating which group to get

### Property Value

[IPDMWGroup](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup.html)

## VBA Syntax

See [PDMWGroups::Item](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWGroups~Item.html).

## See Also

[IPDMWGroups Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroups.html)
[IPDMWGroups Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroups_members.html)
[IPDMWGroups::Count Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroups~Count.html)

## Availability

SOLIDWORKS Workgroup PDM 2004 FCS
