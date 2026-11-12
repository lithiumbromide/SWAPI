---
title: "Item Property (IPDMWProjects)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWProjects"
member: "Item"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProjects~Item.html"
---

# Item Property (IPDMWProjects)

Gets the project by name.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Default Property Item( _
   ByVal Index As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWProjects
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

- `Index`: Number or name indicating the project to get

### Property Value

[IPDMWProject](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject.html)

## VBA Syntax

See [PDMWProjects::Item](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWProjects~Item.html).

## See Also

[IPDMWProjects Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProjects.html)
[IPDMWProjects Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProjects_members.html)
[IPDMWProjects::Count Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProjects~Count.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
