---
title: "GetGuideCurvesType Method (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "GetGuideCurvesType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetGuideCurvesType.html"
---

# GetGuideCurvesType Method (ISweepFeatureData)

Gets the type of [guide curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GuideCurves.html) in this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGuideCurvesType() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Object

value = instance.GetGuideCurvesType()
```

### C#

```csharp
System.object GetGuideCurvesType()
```

### C++/CLI

```cpp
System.Object^ GetGuideCurvesType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of longs or integers representing the types of guide curves as defined in [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [SweepFeatureData::GetGuideCurvesType](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~GetGuideCurvesType.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

This method is not valid if:

- [ISweepFeatureData::Direction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Direction.html) is set to [swSweepDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSweepDirection_e.html).swSweepBiDirectional.

- or -

- [ISweepFeatureData::TwistControlType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~TwistControlType.html) is set to [swTwistControlType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTwistControlType_e.html).swTwistControlConstantTwistAlongPath.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::GetGuideCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetGuideCurvesCount.html)
[ISweepFeatureData::IGetGuideCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IGetGuideCurves.html)
[ISweepFeatureData::IGetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IGetGuideCurvesType.html)
[ISweepFeatureData::ISetGuideCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~ISetGuideCurves.html)
[ISweepFeatureData::MergeSmoothFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~MergeSmoothFaces.html)

## Availability

SOLIDWORKS 2001Plus SP3, Revision Number 10.3
