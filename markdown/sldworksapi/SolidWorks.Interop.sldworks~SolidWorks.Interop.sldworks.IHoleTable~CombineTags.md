---
title: "CombineTags Property (IHoleTable)"
project: "SOLIDWORKS API Help"
interface: "IHoleTable"
member: "CombineTags"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~CombineTags.html"
---

# CombineTags Property (IHoleTable)

Gets or sets whether to combine tags for same-size holes.

## Syntax

### Visual Basic (Declaration)

```vb
Property CombineTags As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTable
Dim value As System.Boolean

instance.CombineTags = value

value = instance.CombineTags
```

### C#

```csharp
System.bool CombineTags {get; set;}
```

### C++/CLI

```cpp
property System.bool CombineTags {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to combine tags for same-size holes, false to not

## VBA Syntax

See [HoleTable::CombineTags](ms-its:sldworksapivb6.chm::/sldworks~HoleTable~CombineTags.html).

## Remarks

This property appears in the Scheme section of the Hole Table PropertyManager page in SOLIDWORKS.

## See Also

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.html)
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html)
[IHoleTable::HoleTag Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTag.html)
[IHoleTable::HoleTagsVisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTagsVisible.html)
[IHoleTable::TagStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~TagStyle.html)
[IHoleTable::CombineSameSize Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~CombineSameSize.html)
[IHoleTable::ShowANSIInchLetterNumberDrillSizes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~ShowANSIInchLetterNumberDrillSizes.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
