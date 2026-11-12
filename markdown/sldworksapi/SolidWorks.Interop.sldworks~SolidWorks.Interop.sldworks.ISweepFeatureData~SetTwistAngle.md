---
title: "SetTwistAngle Method (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "SetTwistAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetTwistAngle.html"
---

# SetTwistAngle Method (ISweepFeatureData)

Sets the angle at which to twist this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetTwistAngle( _
   ByVal Angle As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim Angle As System.Double

instance.SetTwistAngle(Angle)
```

### C#

```csharp
void SetTwistAngle(
   System.double Angle
)
```

### C++/CLI

```cpp
void SetTwistAngle(
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`: Angle of twist in radians

## VBA Syntax

See [SweepFeatureData::SetTwistAngle](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~SetTwistAngle.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

This method is valid only if [ISweepFeatureData::TwistControlType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~TwistControlType.html) is set to [swTwistControlType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTwistControlType_e.html).swTwistControlConstantTwistAlongPath.

In the Sweep PropertyManager, you can specify revolutions, degrees, or radians. To specify Angle, you must convert revolutions and degrees to radians:

1 revolution = 360 degrees = 2*pi = 6.28319 radians

This method sets the angle of twist in radians in Direction 1 of a bidirectional sweep.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::GetTwistAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetTwistAngle.html)
[ISweepFeatureData::D1ReverseTwistDir Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~D1ReverseTwistDir.html)
[ISweepFeatureData::SetD2TwistAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetD2TwistAngle.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
