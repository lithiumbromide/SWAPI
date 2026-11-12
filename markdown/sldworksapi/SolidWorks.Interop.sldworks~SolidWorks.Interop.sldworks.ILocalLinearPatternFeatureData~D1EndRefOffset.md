---
title: "D1EndRefOffset Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "D1EndRefOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndRefOffset.html"
---

# D1EndRefOffset Property (ILocalLinearPatternFeatureData)

Gets or sets the offset from a reference entity in Direction 1 of this linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1EndRefOffset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Double

instance.D1EndRefOffset = value

value = instance.D1EndRefOffset
```

### C#

```csharp
System.double D1EndRefOffset {get; set;}
```

### C++/CLI

```cpp
property System.double D1EndRefOffset {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Offset of a pattern instance or centroid from [ILocalLinearPatternFeatureData::D1EndReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndReference.html)

## VBA Syntax

See [LocalLinearPatternFeatureData::D1EndRefOffset](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~D1EndRefOffset.html).

## Remarks

This property is valid only if [ILocalLinearPatternFeatureData::D1EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndCondition.html) is set to [swPatternEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition_UpToReference.

The pattern instance or centroid to offset is:

- Specified by [ILocalLinearPatternFeatureData::D1EndSeedReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndSeedReference.html).
- Governed by [ILocalLinearPatternFeatureData::D1EndUseSeedReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndUseSeedReference.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Component Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
