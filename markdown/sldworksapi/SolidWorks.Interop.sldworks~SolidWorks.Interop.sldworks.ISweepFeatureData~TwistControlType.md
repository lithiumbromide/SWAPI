---
title: "TwistControlType Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "TwistControlType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~TwistControlType.html"
---

# TwistControlType Property (ISweepFeatureData)

Gets or sets the type of twist control for this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property TwistControlType As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Short

instance.TwistControlType = value

value = instance.TwistControlType
```

### C#

```csharp
System.short TwistControlType {get; set;}
```

### C++/CLI

```cpp
property System.short TwistControlType {
   System.short get();
   void set (    System.short value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Twist control as defined in [swTwistControlType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTwistControlType_e.html) (see **Remarks**)

## VBA Syntax

See [SweepFeatureData::TwistControlType](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~TwistControlType.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

| For user interface options... | Set... |  |  |
| --- | --- | --- | --- |
| Profile Orientation set to... | And Profile Twist set to... | ISweepFeatureData::TwistControlType as defined in swTwistControlType_e to... | And ISweepFeatureData::PathAlignmentType as defined in swTangencyType_e to... |
| Follow Path | None | swTwistControlFollowPath | swTangencyNone |
| Specify Twist Value | swTwistControlConstantTwistAlongPath | swTangencyNone |  |
| Specify Direction Vector | swTwistControlFollowPath | swTangencyDirectionVector |  |
| Follow Path and First Guide Curve (option appears with at least one guide curve) | swTwistControlFollowPathFirstGuideCurve | swTangencyNone |  |
| Follow Path and First and Second Guide Curves (option appears with at least two guide curves) | swTwistControlFollowFirstSecondGuideCurves | swTangencyNone |  |
| Tangent to Adjacent Faces | swTwistControlFollowPath | swTangencyAllFaces |  |
| Minimum Twist (available only with a 3D path) | swTwistControlFollowPath | swMinimumTwist |  |
| Natural | swTwistControlFollowPath | swTangencyNone |  |
| Keep Normal Constant | None | swTwistControlKeepNormalConstant | swTangencyNone |
| Specify Twist Value | swTwistControlConstantTwistAlongPath + swTwistControlKeepNormalConstant | swTangencyNone |  |

If you specify this property with swTwistControlType_e.swTwistControlConstantTwistAlongPath to specify profile twist values, you must set [ISweepFeatureData::AlignWithEndFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~AlignWithEndFaces.html) to false.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::GetTwistAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetTwistAngle.html)
[ISweepFeatureData::SetTwistAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetTwistAngle.html)
[ISweepFeatureData::D1ReverseTwistDir Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~D1ReverseTwistDir.html)
[ISweepFeatureData::D2ReverseTwistDir Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~D2ReverseTwistDir.html)
[ISweepFeatureData::GetD2TwistAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetD2TwistAngle.html)
[ISweepFeatureData::SetD2TwistAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetD2TwistAngle.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
