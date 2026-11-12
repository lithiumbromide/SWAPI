---
title: "Table Property (IDatumOrigin)"
project: "SOLIDWORKS API Help"
interface: "IDatumOrigin"
member: "Table"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~Table.html"
---

# Table Property (IDatumOrigin)

Gets the hole table associated with this datum origin.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Table As HoleTable
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumOrigin
Dim value As HoleTable

value = instance.Table
```

### C#

```csharp
HoleTable Table {get;}
```

### C++/CLI

```cpp
property HoleTable^ Table {
   HoleTable^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to the [IHoleTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleTable.html) object associated with datum origin

## VBA Syntax

See [DatumOrigin::Table](ms-its:sldworksapivb6.chm::/sldworks~DatumOrigin~Table.html).

## See Also

[IDatumOrigin Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.html)
[IDatumOrigin Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
