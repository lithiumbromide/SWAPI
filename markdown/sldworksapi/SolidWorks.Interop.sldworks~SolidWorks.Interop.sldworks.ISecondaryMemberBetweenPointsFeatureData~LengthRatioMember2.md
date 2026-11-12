---
title: "LengthRatioMember2 Property (ISecondaryMemberBetweenPointsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberBetweenPointsFeatureData"
member: "LengthRatioMember2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData~LengthRatioMember2.html"
---

# LengthRatioMember2 Property (ISecondaryMemberBetweenPointsFeatureData)

Gets and sets the length ratio offset from the end of the second member of the primary structure system member pair.

## Syntax

### Visual Basic (Declaration)

```vb
Property LengthRatioMember2 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberBetweenPointsFeatureData
Dim value As System.Double

instance.LengthRatioMember2 = value

value = instance.LengthRatioMember2
```

### C#

```csharp
System.double LengthRatioMember2 {get; set;}
```

### C++/CLI

```cpp
property System.double LengthRatioMember2 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 <= Length ratio offset from the end of the second member <= 1.0

## VBA Syntax

See [SecondaryMemberBetweenPointsFeatureData::LengthRatioMember2](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberBetweenPointsFeatureData~LengthRatioMember2.html).

## Examples

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html) examples.

## Remarks

This property is valid only if [ISecondaryMemberBetweenPointsFeatureData::SecondaryMemberOffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData~SecondaryMemberOffsetType.html) is set to [swSecondaryMemberBetweenPointsDistanceFromEndType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberBetweenPointsDistanceFromEndType_e.html).swSecondaryMemberBetweenPointsDistanceFromEndType_LengthRatio.

## See Also

[ISecondaryMemberBetweenPointsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html)
[ISecondaryMemberBetweenPointsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
