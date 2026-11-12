---
title: "RevDirectionDistanceMember2 Property (ISecondaryMemberBetweenPointsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberBetweenPointsFeatureData"
member: "RevDirectionDistanceMember2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData~RevDirectionDistanceMember2.html"
---

# RevDirectionDistanceMember2 Property (ISecondaryMemberBetweenPointsFeatureData)

Gets and sets whether to reverse the direction of the offset for the second member of the primary structure system member pair.

## Syntax

### Visual Basic (Declaration)

```vb
Property RevDirectionDistanceMember2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberBetweenPointsFeatureData
Dim value As System.Boolean

instance.RevDirectionDistanceMember2 = value

value = instance.RevDirectionDistanceMember2
```

### C#

```csharp
System.bool RevDirectionDistanceMember2 {get; set;}
```

### C++/CLI

```cpp
property System.bool RevDirectionDistanceMember2 {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction of the offset from the end of the second member, false to not

## VBA Syntax

See [SecondaryMemberBetweenPointsFeatureData::RevDirectionDistanceMember2](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberBetweenPointsFeatureData~RevDirectionDistanceMember2.html).

## Examples

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html) examples.

## Remarks

This property is valid only if [ISecondaryMemberBetweenPointsFeatureData::SecondaryMemberOffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData~SecondaryMemberOffsetType.html) is set to [swSecondaryMemberBetweenPointsDistanceFromEndType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberBetweenPointsDistanceFromEndType_e.html).swSecondaryMemberBetweenPointsDistanceFromEndType_Distance.

## See Also

[ISecondaryMemberBetweenPointsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html)
[ISecondaryMemberBetweenPointsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
