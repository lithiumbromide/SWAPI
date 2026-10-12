---
title: "GetD2TwistAngle Method (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "GetD2TwistAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetD2TwistAngle.html"
---

# GetD2TwistAngle Method (ISweepFeatureData)

Gets the twist angle in Direction 2 of this bidirectional sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetD2TwistAngle() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Double

value = instance.GetD2TwistAngle()
```

### C#

```csharp
System.double GetD2TwistAngle()
```

### C++/CLI

```cpp
System.double GetD2TwistAngle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Angle of twist in radians in Direction 2

## VBA Syntax

See [SweepFeatureData::GetD2TwistAngle](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~GetD2TwistAngle.html).

## Remarks

This property is valid only if:

- [ISweepFeatureData::TwistControlType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~TwistControlType.html) is set to [swTwistControlType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTwistControlType_e.html).swTwistControlConstantTwistAlongPath.
- [ISweepFeatureData::Direction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Direction.html) is set to [swSweepDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSweepDirection_e.html).swSweepBidirectional.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::SetD2TwistAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetD2TwistAngle.html)
[ISweepFeatureData::GetTwistAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetTwistAngle.html)
[ISweepFeatureData::D2ReverseTwistDir Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~D2ReverseTwistDir.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
