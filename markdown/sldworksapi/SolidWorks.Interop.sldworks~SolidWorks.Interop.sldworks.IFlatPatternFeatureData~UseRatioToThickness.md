---
title: "UseRatioToThickness Property (IFlatPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData"
member: "UseRatioToThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~UseRatioToThickness.html"
---

# UseRatioToThickness Property (IFlatPatternFeatureData)

Gets or sets whether to use the ratio to thickness setting for the corner trim for the Flat-Pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseRatioToThickness As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFeatureData
Dim value As System.Boolean

instance.UseRatioToThickness = value

value = instance.UseRatioToThickness
```

### C#

```csharp
System.bool UseRatioToThickness {get; set;}
```

### C++/CLI

```cpp
property System.bool UseRatioToThickness {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the ratio to thickness setting, false to not

## VBA Syntax

See [FlatPatternFeatureData::UseRatioToThickness](ms-its:sldworksapivb6.chm::/sldworks~FlatPatternFeatureData~UseRatioToThickness.html).

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html)
[IFlatPatternFeatureData::GetAddCornerTrim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~GetAddCornerTrim.html)
[IFlatPatternFeatureData::SetAddCornerTrim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~SetAddCornerTrim.html)
[IFlatPatternFeatureData::CornerTrimRatioToThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimRatioToThickness.html)
[IFlatPatternFeatureData::CornerTrimReliefDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimReliefDistance.html)
[IFlatPatternFeatureData::CornerTrimReliefType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimReliefType.html)
[IFlatPatternFeatureData::ShowSlitInCornerRelief Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ShowSlitInCornerRelief.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
