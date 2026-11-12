---
title: "CornerTrimRatioToThickness Property (IFlatPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData"
member: "CornerTrimRatioToThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimRatioToThickness.html"
---

# CornerTrimRatioToThickness Property (IFlatPatternFeatureData)

Gets or sets the ratio of the relief thickness of the corner trim for the Flat-Pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CornerTrimRatioToThickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFeatureData
Dim value As System.Double

instance.CornerTrimRatioToThickness = value

value = instance.CornerTrimRatioToThickness
```

### C#

```csharp
System.double CornerTrimRatioToThickness {get; set;}
```

### C++/CLI

```cpp
property System.double CornerTrimRatioToThickness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Ratio

## VBA Syntax

See [FlatPatternFeatureData::CornerTrimRatioToThickness](ms-its:sldworksapivb6.chm::/sldworks~FlatPatternFeatureData~CornerTrimRatioToThickness.html).

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html)
[IFlatPatternFeatureData::GetAddCornerTrim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~GetAddCornerTrim.html)
[IFlatPatternFeatureData::SetAddCornerTrim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~SetAddCornerTrim.html)
[IFlatPatternFeatureData::CornerTrimReliefDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimReliefDistance.html)
[IFlatPatternFeatureData::CornerTrimReliefType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimReliefType.html)
[IFlatPatternFeatureData::UseRatioToThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~UseRatioToThickness.html)
[IFlatPatternFeatureData::ShowSlitInCornerRelief Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ShowSlitInCornerRelief.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
