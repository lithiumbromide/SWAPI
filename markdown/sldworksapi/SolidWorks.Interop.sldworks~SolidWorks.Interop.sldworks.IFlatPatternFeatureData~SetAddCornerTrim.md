---
title: "SetAddCornerTrim Method (IFlatPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData"
member: "SetAddCornerTrim"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~SetAddCornerTrim.html"
---

# SetAddCornerTrim Method (IFlatPatternFeatureData)

Sets whether to add corner trims to the Flat-Pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetAddCornerTrim( _
   ByVal BCT As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFeatureData
Dim BCT As System.Boolean

instance.SetAddCornerTrim(BCT)
```

### C#

```csharp
void SetAddCornerTrim(
   System.bool BCT
)
```

### C++/CLI

```cpp
void SetAddCornerTrim(
   System.bool BCT
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BCT`: True to add corner trims, false to not

## VBA Syntax

See [FlatPatternFeatureData::SetAddCornerTrim](ms-its:sldworksapivb6.chm::/sldworks~FlatPatternFeatureData~SetAddCornerTrim.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html)
[IFlatPatternFeatureData::GetAddCornerTrim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~GetAddCornerTrim.html)
[IFlatPatternFeatureData::CornerTrimRatioToThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimRatioToThickness.html)
[IFlatPatternFeatureData::CornerTrimReliefDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimReliefDistance.html)
[IFlatPatternFeatureData::CornerTrimReliefType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~CornerTrimReliefType.html)
[IFlatPatternFeatureData::UseRatioToThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~UseRatioToThickness.html)
[IFlatPatternFeatureData::ShowSlitInCornerRelief Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ShowSlitInCornerRelief.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
