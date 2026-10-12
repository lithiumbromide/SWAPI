---
title: "PathAlignmentType Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "PathAlignmentType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~PathAlignmentType.html"
---

# PathAlignmentType Property (ISweepFeatureData)

Gets or sets the alignment of the sweep path in this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PathAlignmentType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Integer

instance.PathAlignmentType = value

value = instance.PathAlignmentType
```

### C#

```csharp
System.int PathAlignmentType {get; set;}
```

### C++/CLI

```cpp
property System.int PathAlignmentType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Sweep path alignment as defined in [swTangencyType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTangencyType_e.html):

- swTangencyAllFaces
- swTangencyDirectionVector
- swTangencyNone

## VBA Syntax

See [SweepFeatureData::PathAlignmentType](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~PathAlignmentType.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

| For user interface option... | Set... |  |  |
| --- | --- | --- | --- |
| Profile Orientation set to... | And Profile Twist set to... | ISweepFeatureData::TwistControlType as defined in swTwistControlType_e to... | And ISweepFeatureData::PathAlignmentType as defined in swTangencyType_e to... |
| Follow Path | None | swTwistControlFollowPath | swTangencyNone |
| Specify Twist Value | swTwistControlConstantTwistAlongPath | swTangencyNone |  |
| Specify Direction Vector | swTwistControlFollowPath | swTangencyDirectionVector; call ISweepFeatureData::SetPathAlignmentDirectionVector to specify the direction vector |  |
| Follow Path and First Guide Curve (option appears with at least one guide curve) | swTwistControlFollowPathFirstGuideCurve | swTangencyNone |  |
| Follow Path and First and Second Guide Curves (option appears with at least two guide curves) | swTwistControlFollowFirstSecondGuideCurves | swTangencyNone |  |
| Tangent to Adjacent Faces | swTwistControlFollowPath | swTangencyAllFaces |  |
| Minimum Twist (available only with a 3D path) | swTwistControlFollowPath | swMinimumTwist |  |
| Natural | swTwistControlFollowPath | swTangencyNone |  |
| Keep Normal Constant | None | swTwistControlKeepNormalConstant | swTangencyNone |
| Specify Twist Value | swTwistControlConstantTwistAlongPath + swTwistControlKeepNormalConstant | swTangencyNone |  |

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::GetPathAlignmentDirectionVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetPathAlignmentDirectionVector.html)
[ISweepFeatureData::GetPathType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetPathType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
