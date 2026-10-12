---
title: "Item Property (IPDMWLinks)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWLinks"
member: "Item"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLinks~Item.html"
---

# Item Property (IPDMWLinks)

Gets the specified link.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Default Property Item( _
   ByVal Index As System.Integer _
) As PDMWLink
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWLinks
Dim Index As System.Integer
Dim value As PDMWLink

value = instance.Item(Index)
```

### C#

```csharp
PDMWLink this[
   System.int Index
]; {get;}
```

### C++/CLI

```cpp
property PDMWLink^ default [System.int] {
   PDMWLink^ get(System.int Index);
}
```

### Parameters

- `Index`: Number indicating which link to get

### Property Value

[IPDMLink](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink.html)

## VBA Syntax

See [PDMWLinks::Item](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWLinks~Item.html).

## See Also

[IPDMWLinks Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLinks.html)
[IPDMWLinks Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLinks_members.html)
[IPDMWLinks::Count Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLinks~Count.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
