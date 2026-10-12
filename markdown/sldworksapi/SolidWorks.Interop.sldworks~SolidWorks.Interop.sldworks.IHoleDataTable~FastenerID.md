---
title: "FastenerID Property (IHoleDataTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleDataTable"
member: "FastenerID"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~FastenerID.html"
---

# FastenerID Property (IHoleDataTable)

Gets the ID of the fastener associated with this Hole Wizard fastener table.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FastenerID As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleDataTable
Dim value As System.Integer

value = instance.FastenerID
```

### C#

```csharp
System.int FastenerID {get;}
```

### C++/CLI

```cpp
property System.int FastenerID {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fastener ID

## VBA Syntax

See [HoleDataTable::FastenerID](ms-its:sldworksapivb6.chm::/sldworks~HoleDataTable~FastenerID.html).

## Examples

See the [IHoleDataTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.html) example.

## See Also

[IHoleDataTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.html)
[IHoleDataTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
