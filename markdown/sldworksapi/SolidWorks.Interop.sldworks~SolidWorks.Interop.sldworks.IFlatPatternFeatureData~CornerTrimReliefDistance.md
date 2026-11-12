---
title: "CornerTrimReliefDistance Property (IFlatPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData"
member: "CornerTrimReliefDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimReliefDistance.html"
---

# CornerTrimReliefDistance Property (IFlatPatternFeatureData)

Gets or sets the distance of the relief for the corner trim for the Flat-Pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CornerTrimReliefDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFeatureData
Dim value As System.Double

instance.CornerTrimReliefDistance = value

value = instance.CornerTrimReliefDistance
```

### C#

```csharp
System.double CornerTrimReliefDistance {get; set;}
```

### C++/CLI

```cpp
property System.double CornerTrimReliefDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance of the relief for the corner trim

## VBA Syntax

See [FlatPatternFeatureData::CornerTrimReliefDistance](ms-its:sldworksapivb6.chm::/sldworks~FlatPatternFeatureData~CornerTrimReliefDistance.html).

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html)
[IFlatPatternFeatureData::GetAddCornerTrim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~GetAddCornerTrim.html)
[IFlatPatternFeatureData::SetAddCornerTrim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~SetAddCornerTrim.html)
[IFlatPatternFeatureData::CornerTrimRatioToThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimRatioToThickness.html)
[IFlatPatternFeatureData::CornerTrimReliefType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimReliefType.html)
[IFlatPatternFeatureData::UseRatioToThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~UseRatioToThickness.html)
[IFlatPatternFeatureData::ShowSlitInCornerRelief Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ShowSlitInCornerRelief.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
