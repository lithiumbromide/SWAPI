---
title: "D1EndRefOffset Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "D1EndRefOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndRefOffset.html"
---

# D1EndRefOffset Property (ILinearPatternFeatureData)

Gets or sets the distance of the last pattern instance from the up-to reference geometry in Direction 1 of this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1EndRefOffset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
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

Offset of last pattern instance from [ILinearPatternFeatureData::D1EndReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndReference.html)

## VBA Syntax

See [LinearPatternFeatureData::D1EndRefOffset](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~D1EndRefOffset.html).

## Remarks

This property is valid only if [ILinearPatternFeatureData::D1EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndCondition.html) is set to [swPatternEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition_UpToReference.

Whether to offset instance geometry or a centroid is governed by [ILinearPatternFeatureData::D1EndUseSeedReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndUseSeedReference.html).

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
