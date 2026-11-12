---
title: "SetD2TwistAngle Method (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "SetD2TwistAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetD2TwistAngle.html"
---

# SetD2TwistAngle Method (ISweepFeatureData)

Sets the twist angle in Direction 2 of this bidirectional sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetD2TwistAngle( _
   ByVal Angle As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim Angle As System.Double

instance.SetD2TwistAngle(Angle)
```

### C#

```csharp
void SetD2TwistAngle(
   System.double Angle
)
```

### C++/CLI

```cpp
void SetD2TwistAngle(
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`: Angle of twist in radians in Direction 2

## VBA Syntax

See [SweepFeatureData::SetD2TwistAngle](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~SetD2TwistAngle.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

This property is valid only if:

- [ISweepFeatureData::TwistControlType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~TwistControlType.html) is set to [swTwistControlType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTwistControlType_e.html).swTwistControlConstantTwistAlongPath.
- [ISweepFeatureData::Direction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Direction.html) is set to [swSweepDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSweepDirection_e.html).swSweepBidirectional.

In the Sweep PropertyManager, you can specify revolutions, degrees, or radians. To specify Angle, you must convert revolutions and degrees to radians:

1 revolution = 360 degrees = 2*pi = 6.28319 radians

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::GetD2TwistAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetD2TwistAngle.html)
[ISweepFeatureData::SetTwistAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetTwistAngle.html)
[ISweepFeatureData::D2ReverseTwistDir Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~D2ReverseTwistDir.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
