---
title: "GuideCurves Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "GuideCurves"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GuideCurves.html"
---

# GuideCurves Property (ISweepFeatureData)

Gets or sets the guide curves for this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property GuideCurves As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Object

instance.GuideCurves = value

value = instance.GuideCurves
```

### C#

```csharp
System.object GuideCurves {get; set;}
```

### C++/CLI

```cpp
property System.Object^ GuideCurves {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of guide [curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html), [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [lines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html), or [arcs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.html)

## VBA Syntax

See [SweepFeatureData::GuideCurves](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~GuideCurves.html).

## Remarks

This property is not valid if:

- [ISweepFeatureData::Direction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Direction.html) is set to [swSweepDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSweepDirection_e.html).swSweepBiDirectional.

- or -

- [ISweepFeatureData::TwistControlType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~TwistControlType.html) is set to [swTwistControlType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTwistControlType_e.html).swTwistControlConstantTwistAlongPath.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::GetGuideCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetGuideCurvesCount.html)
[ISweepFeatureData::GetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetGuideCurvesType.html)
[ISweepFeatureData::IGetGuideCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IGetGuideCurves.html)
[ISweepFeatureData::IGetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IGetGuideCurvesType.html)
[ISweepFeatureData::ISetGuideCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~ISetGuideCurves.html)
[ISweepFeatureData::MergeSmoothFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~MergeSmoothFaces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
