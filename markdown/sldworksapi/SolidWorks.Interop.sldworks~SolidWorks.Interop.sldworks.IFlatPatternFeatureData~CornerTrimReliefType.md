---
title: "CornerTrimReliefType Property (IFlatPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData"
member: "CornerTrimReliefType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimReliefType.html"
---

# CornerTrimReliefType Property (IFlatPatternFeatureData)

Gets or sets the type of relief for the corner trim for the Flat-Pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CornerTrimReliefType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFeatureData
Dim value As System.Integer

instance.CornerTrimReliefType = value

value = instance.CornerTrimReliefType
```

### C#

```csharp
System.int CornerTrimReliefType {get; set;}
```

### C++/CLI

```cpp
property System.int CornerTrimReliefType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of relief as defined in [swCornerReliefType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCornerReliefType_e.html)

## VBA Syntax

See [FlatPatternFeatureData::CornerTrimReliefType](ms-its:sldworksapivb6.chm::/sldworks~FlatPatternFeatureData~CornerTrimReliefType.html).

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html)
[IFlatPatternFeatureData::GetAddCornerTrim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~GetAddCornerTrim.html)
[IFlatPatternFeatureData::SetAddCornerTrim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~SetAddCornerTrim.html)
[IFlatPatternFeatureData::CornerTrimRatioToThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimRatioToThickness.html)
[IFlatPatternFeatureData::CornerTrimReliefDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimReliefDistance.html)
[IFlatPatternFeatureData::UseRatioToThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~UseRatioToThickness.html)
[IFlatPatternFeatureData::ShowSlitInCornerRelief Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ShowSlitInCornerRelief.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
