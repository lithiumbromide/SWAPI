---
title: "StandardName Property (IHoleDataTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleDataTable"
member: "StandardName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~StandardName.html"
---

# StandardName Property (IHoleDataTable)

Gets the name of the Hole Wizard standard associated with this Hole Wizard fastener table.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property StandardName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleDataTable
Dim value As System.String

value = instance.StandardName
```

### C#

```csharp
System.string StandardName {get;}
```

### C++/CLI

```cpp
property System.String^ StandardName {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Hole Wizard standard

## VBA Syntax

See [HoleDataTable::StandardName](ms-its:sldworksapivb6.chm::/sldworks~HoleDataTable~StandardName.html).

## Examples

See the [IHoleDataTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.html) example.

## See Also

[IHoleDataTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.html)
[IHoleDataTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
