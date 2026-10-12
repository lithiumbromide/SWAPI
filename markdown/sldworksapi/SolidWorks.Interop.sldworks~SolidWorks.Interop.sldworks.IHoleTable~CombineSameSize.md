---
title: "CombineSameSize Property (IHoleTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleTable"
member: "CombineSameSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~CombineSameSize.html"
---

# CombineSameSize Property (IHoleTable)

Gets or sets whether to merge cells of the same size in this hole table.

## Syntax

### Visual Basic (Declaration)

```vb
Property CombineSameSize As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTable
Dim value As System.Boolean

instance.CombineSameSize = value

value = instance.CombineSameSize
```

### C#

```csharp
System.bool CombineSameSize {get; set;}
```

### C++/CLI

```cpp
property System.bool CombineSameSize {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to merge cells of the same size, false to not

## VBA Syntax

See [HoleTable::CombineSameSize](ms-its:sldworksapivb6.chm::/sldworks~HoleTable~CombineSameSize.html).

## Remarks

This property appears in the Scheme section of the Hole Table PropertyManager page in SOLIDWORKS.

## See Also

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html)
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html)
[IHoleTable::CombineTags Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~CombineTags.html)
[IHoleTable::ShowANSIInchLetterNumberDrillSizes Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~ShowANSIInchLetterNumberDrillSizes.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
