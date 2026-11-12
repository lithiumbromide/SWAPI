---
title: "GetTwistAngle Method (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "GetTwistAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetTwistAngle.html"
---

# GetTwistAngle Method (ISweepFeatureData)

Gets the angle at which to twist this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTwistAngle() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Double

value = instance.GetTwistAngle()
```

### C#

```csharp
System.double GetTwistAngle()
```

### C++/CLI

```cpp
System.double GetTwistAngle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Angle of twist in radians

## VBA Syntax

See [SweepFeatureData::GetTwistAngle](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~GetTwistAngle.html).

## Remarks

This method is valid only if [ISweepFeatureData::TwistControlType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~TwistControlType.html) is set to [swTwistControlType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTwistControlType_e.html).swTwistControlConstantTwistAlongPath.

This method gets the angle of twist in radians in Direction 1 of a bidirectional sweep.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::SetTwistAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetTwistAngle.html)
[ISweepFeatureData::D1ReverseTwistDir Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~D1ReverseTwistDir.html)
[ISweepFeatureData::GetD2TwistAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetD2TwistAngle.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.1
