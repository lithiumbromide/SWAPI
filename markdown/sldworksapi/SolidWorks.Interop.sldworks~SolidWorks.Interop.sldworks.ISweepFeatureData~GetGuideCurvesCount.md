---
title: "GetGuideCurvesCount Method (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "GetGuideCurvesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetGuideCurvesCount.html"
---

# GetGuideCurvesCount Method (ISweepFeatureData)

Gets a number of guide curves for this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGuideCurvesCount() As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Short

value = instance.GetGuideCurvesCount()
```

### C#

```csharp
System.short GetGuideCurvesCount()
```

### C++/CLI

```cpp
System.short GetGuideCurvesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of guide curves

## VBA Syntax

See [SweepFeatureData::GetGuideCurvesCount](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~GetGuideCurvesCount.html).

## Remarks

This method is not valid if:

- [ISweepFeatureData::Direction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Direction.html) is set to [swSweepDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSweepDirection_e.html).swSweepBiDirectional.

- or -

- [ISweepFeatureData::TwistControlType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~TwistControlType.html) is set to [swTwistControlType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTwistControlType_e.html).swTwistControlConstantTwistAlongPath.

Call this method before calling [ISweepFeatureData::IGetGuideCurves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISweepFeatureData~IGetGuideCurves.html) to get the size of the array for that method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::GetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetGuideCurvesType.html)
[ISweepFeatureData::IGetGuideCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IGetGuideCurves.html)
[ISweepFeatureData::IGetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IGetGuideCurvesType.html)
[ISweepFeatureData::ISetGuideCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~ISetGuideCurves.html)
[ISweepFeatureData::GuideCurves Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GuideCurves.html)
[ISweepFeatureData::MergeSmoothFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~MergeSmoothFaces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
