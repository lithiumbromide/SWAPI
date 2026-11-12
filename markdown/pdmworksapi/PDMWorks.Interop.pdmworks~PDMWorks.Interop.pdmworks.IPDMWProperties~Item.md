---
title: "Item Property (IPDMWProperties)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWProperties"
member: "Item"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties~Item.html"
---

# Item Property (IPDMWProperties)

Gets a property.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Default Property Item( _
   ByVal Index As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWProperties
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

- `Index`: Number or name indicating the property to get

### Property Value

[IPDMWProperty](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperty.html)

## VBA Syntax

See [PDMWProperties::Item](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWProperties~Item.html).

## Remarks

Before calling this method, call [IPDMWProperties::Count](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProjects~Count.html) to get the number of properties in the collection.

## See Also

[IPDMWProperties Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties.html)
[IPDMWProperties Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
