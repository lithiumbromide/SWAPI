---
title: "ShowSlitInCornerRelief Property (IFlatPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData"
member: "ShowSlitInCornerRelief"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ShowSlitInCornerRelief.html"
---

# ShowSlitInCornerRelief Property (IFlatPatternFeatureData)

Get or set whether to show the slit in the corner relief of this Flat-Pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowSlitInCornerRelief As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFeatureData
Dim value As System.Boolean

instance.ShowSlitInCornerRelief = value

value = instance.ShowSlitInCornerRelief
```

### C#

```csharp
System.bool ShowSlitInCornerRelief {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowSlitInCornerRelief {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display the slit in the corner relief of this feature, false to not

## VBA Syntax

See [FlatPatternFeatureData::ShowSlitInCornerRelief](ms-its:sldworksapivb6.chm::/sldworks~FlatPatternFeatureData~ShowSlitInCornerRelief.html).

## Remarks

When you create a rectangular or circular corner relief that is smaller than the bend area, a slit is added so that the part can bend. Setting this property to true makes the slit available in the flat pattern.

This property corresponds to the **Show Slit** option in the Parameters section of the Flat-Pattern PropertyManager.

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html)
[IFlatPatternFeatureData::CornerTrimReliefType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimReliefType.html)
[IFlatPatternFeatureData::GetAddCornerTrim Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~GetAddCornerTrim.html)
[IFlatPatternFeatureData::SetAddCornerTrim Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~SetAddCornerTrim.html)
[IFlatPatternFeatureData::CornerTreatment Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTreatment.html)
[IFlatPatternFeatureData::CornerTrimRatioToThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimRatioToThickness.html)
[IFlatPatternFeatureData::CornerTrimReliefDistance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimReliefDistance.html)
[IFlatPatternFeatureData::UseRatioToThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~UseRatioToThickness.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
