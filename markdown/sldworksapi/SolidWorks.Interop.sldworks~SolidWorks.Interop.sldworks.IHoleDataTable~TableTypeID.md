---
title: "TableTypeID Property (IHoleDataTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleDataTable"
member: "TableTypeID"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~TableTypeID.html"
---

# TableTypeID Property (IHoleDataTable)

Gets the fastener table type ID associated with this Hole Wizard fastener table.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TableTypeID As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleDataTable
Dim value As System.Integer

value = instance.TableTypeID
```

### C#

```csharp
System.int TableTypeID {get;}
```

### C++/CLI

```cpp
property System.int TableTypeID {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fastener table type ID as defined in [swFastenerTableTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFastenerTableTypes_e.html)

## VBA Syntax

See [HoleDataTable::TableTypeID](ms-its:sldworksapivb6.chm::/sldworks~HoleDataTable~TableTypeID.html).

## Examples

See the [IHoleDataTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.html) example.

## See Also

[IHoleDataTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.html)
[IHoleDataTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
