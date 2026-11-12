---
title: "Item Property (IPDMWConfigurations)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConfigurations"
member: "Item"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfigurations~Item.html"
---

# Item Property (IPDMWConfigurations)

Gets a configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Default Property Item( _
   ByVal Index As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConfigurations
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

- `Index`: Number or name indicating which configuration to get

### Property Value

An [IPDMWConfiguration](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration.html)

## VBA Syntax

See [PDMWConfigurations::Item](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConfigurations~Item.html).

## See Also

[IPDMWConfigurations Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfigurations.html)
[IPDMWConfigurations Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfigurations_members.html)
[PDMWConfigurations::Count](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfigurations~Count.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
