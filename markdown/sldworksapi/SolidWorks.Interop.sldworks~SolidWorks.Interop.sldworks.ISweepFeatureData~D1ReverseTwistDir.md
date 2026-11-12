---
title: "D1ReverseTwistDir Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "D1ReverseTwistDir"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~D1ReverseTwistDir.html"
---

# D1ReverseTwistDir Property (ISweepFeatureData)

Gets or sets whether to reverse the twist of this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1ReverseTwistDir As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Boolean

instance.D1ReverseTwistDir = value

value = instance.D1ReverseTwistDir
```

### C#

```csharp
System.bool D1ReverseTwistDir {get; set;}
```

### C++/CLI

```cpp
property System.bool D1ReverseTwistDir {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the twist, false to not

## VBA Syntax

See [SweepFeatureData::D1ReverseTwistDir](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~D1ReverseTwistDir.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

This property is valid only if [ISweepFeatureData::TwistControlType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~TwistControlType.html) is set to [swTwistControlType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTwistControlType_e.html).swTwistControlConstantTwistAlongPath.

This property reverses the twist in Direction 1 of a bidirectional sweep.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::D2ReverseTwistDir Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~D2ReverseTwistDir.html)
[ISweepFeatureData::GetTwistAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetTwistAngle.html)
[ISweepFeatureData::SetTwistAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetTwistAngle.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
