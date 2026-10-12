---
title: "D2ReverseTwistDir Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "D2ReverseTwistDir"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~D2ReverseTwistDir.html"
---

# D2ReverseTwistDir Property (ISweepFeatureData)

Gets or sets whether to reverse the twist in Direction 2 of this bidirectional sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2ReverseTwistDir As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Boolean

instance.D2ReverseTwistDir = value

value = instance.D2ReverseTwistDir
```

### C#

```csharp
System.bool D2ReverseTwistDir {get; set;}
```

### C++/CLI

```cpp
property System.bool D2ReverseTwistDir {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the twist in Direction 2, false to not

## VBA Syntax

See [SweepFeatureData::D2ReverseTwistDir](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~D2ReverseTwistDir.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

This property is valid only if:

- [ISweepFeatureData::TwistControlType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~TwistControlType.html) is set to [swTwistControlType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTwistControlType_e.html).swTwistControlConstantTwistAlongPath.
- [ISweepFeatureData::Direction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Direction.html) is set to [swSweepDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSweepDirection_e.html).swSweepBidirectional.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::D1ReverseTwistDir Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~D1ReverseTwistDir.html)
[ISweepFeatureData::GetD2TwistAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetD2TwistAngle.html)
[ISweepFeatureData::SetD2TwistAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetD2TwistAngle.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
