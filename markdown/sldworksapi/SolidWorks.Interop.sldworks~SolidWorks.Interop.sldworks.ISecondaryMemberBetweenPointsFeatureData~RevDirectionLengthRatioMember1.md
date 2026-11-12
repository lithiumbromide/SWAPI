---
title: "RevDirectionLengthRatioMember1 Property (ISecondaryMemberBetweenPointsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberBetweenPointsFeatureData"
member: "RevDirectionLengthRatioMember1"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData~RevDirectionLengthRatioMember1.html"
---

# RevDirectionLengthRatioMember1 Property (ISecondaryMemberBetweenPointsFeatureData)

Gets and sets whether to reverse the direction of the length ratio offset for the first member of the primary structure system member pair.

## Syntax

### Visual Basic (Declaration)

```vb
Property RevDirectionLengthRatioMember1 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberBetweenPointsFeatureData
Dim value As System.Boolean

instance.RevDirectionLengthRatioMember1 = value

value = instance.RevDirectionLengthRatioMember1
```

### C#

```csharp
System.bool RevDirectionLengthRatioMember1 {get; set;}
```

### C++/CLI

```cpp
property System.bool RevDirectionLengthRatioMember1 {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction of the length ratio offset from the end of the first member, false to not

## VBA Syntax

See [SecondaryMemberBetweenPointsFeatureData::RevDirectionLengthRatioMember1](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberBetweenPointsFeatureData~RevDirectionLengthRatioMember1.html).

## Remarks

This property is valid only if [ISecondaryMemberBetweenPointsFeatureData::SecondaryMemberOffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData~SecondaryMemberOffsetType.html) is set to [swSecondaryMemberBetweenPointsDistanceFromEndType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberBetweenPointsDistanceFromEndType_e.html).swSecondaryMemberBetweenPointsDistanceFromEndType_LengthRatio.

## See Also

[ISecondaryMemberBetweenPointsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html)
[ISecondaryMemberBetweenPointsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
