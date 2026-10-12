---
title: "HoleCentersVisible Property (IHoleTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleTable"
member: "HoleCentersVisible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleCentersVisible.html"
---

# HoleCentersVisible Property (IHoleTable)

Gets or sets whether to show the hole center marks for this hole table.

## Syntax

### Visual Basic (Declaration)

```vb
Property HoleCentersVisible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTable
Dim value As System.Boolean

instance.HoleCentersVisible = value

value = instance.HoleCentersVisible
```

### C#

```csharp
System.bool HoleCentersVisible {get; set;}
```

### C++/CLI

```cpp
property System.bool HoleCentersVisible {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the hole center marks are visible, false if not

## VBA Syntax

See [HoleTable::HoleCentersVisible](ms-its:sldworksapivb6.chm::/sldworks~HoleTable~HoleCentersVisible.html).

## See Also

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html)
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
