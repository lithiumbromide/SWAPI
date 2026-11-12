---
title: "LengthRatioMember1 Property (ISecondaryMemberBetweenPointsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberBetweenPointsFeatureData"
member: "LengthRatioMember1"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData~LengthRatioMember1.html"
---

# LengthRatioMember1 Property (ISecondaryMemberBetweenPointsFeatureData)

Gets and sets the length ratio offset from the end of the first member of the primary structure system member pair.

## Syntax

### Visual Basic (Declaration)

```vb
Property LengthRatioMember1 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberBetweenPointsFeatureData
Dim value As System.Double

instance.LengthRatioMember1 = value

value = instance.LengthRatioMember1
```

### C#

```csharp
System.double LengthRatioMember1 {get; set;}
```

### C++/CLI

```cpp
property System.double LengthRatioMember1 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 <= Length ratio offset from the end of the first member <= 1.0

## VBA Syntax

See [SecondaryMemberBetweenPointsFeatureData::LengthRatioMember1](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberBetweenPointsFeatureData~LengthRatioMember1.html).

## Examples

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html) examples.

## Remarks

This property is valid only if [ISecondaryMemberBetweenPointsFeatureData::SecondaryMemberOffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData~SecondaryMemberOffsetType.html) is set to [swSecondaryMemberBetweenPointsDistanceFromEndType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberBetweenPointsDistanceFromEndType_e.html).swSecondaryMemberBetweenPointsDistanceFromEndType_LengthRatio.

## See Also

[ISecondaryMemberBetweenPointsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html)
[ISecondaryMemberBetweenPointsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
