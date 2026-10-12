---
title: "Item Property (IPDMWUsers)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWUsers"
member: "Item"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUsers~Item.html"
---

# Item Property (IPDMWUsers)

Gets the user by name.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Default Property Item( _
   ByVal Index As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWUsers
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

- `Index`: Number indicating which user to get

### Property Value

[IPDMWUser](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser.html)

## VBA Syntax

See [PDMWUsers::Item](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWUsers~Item.html).

## See Also

[IPDMWUsers Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUsers.html)
[IPDMWUsers Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUsers_members.html)
[IPDMWUsers::Count Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUsers~Count.html)

## Availability

SOLIDWORKS Workgroup PDM 2004 FCS
