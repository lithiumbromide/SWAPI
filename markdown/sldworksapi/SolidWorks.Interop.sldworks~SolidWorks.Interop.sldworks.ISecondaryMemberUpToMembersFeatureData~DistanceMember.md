---
title: "DistanceMember Property (ISecondaryMemberUpToMembersFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberUpToMembersFeatureData"
member: "DistanceMember"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~DistanceMember.html"
---

# DistanceMember Property (ISecondaryMemberUpToMembersFeatureData)

Gets or sets the distance with which to offset this secondary structure system up-to member.

## Syntax

### Visual Basic (Declaration)

```vb
Property DistanceMember As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberUpToMembersFeatureData
Dim value As System.Double

instance.DistanceMember = value

value = instance.DistanceMember
```

### C#

```csharp
System.double DistanceMember {get; set;}
```

### C++/CLI

```cpp
property System.double DistanceMember {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance in meters

## VBA Syntax

See [SecondaryMemberUpToMembersFeatureData::DistanceMember](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberUpToMembersFeatureData~DistanceMember.html).

## Examples

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html) examples.

## Remarks

This property is valid only if [ISecondaryMemberUpToMembersFeatureData::SecondaryMemberOffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~SecondaryMemberOffsetType.html) is set to [swSecondaryMemberUpToMembersDistanceFromEndType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberUpToMembersDistanceFromEndType_e.html).swSecondaryMemberUpToMembersDistanceFromEndType_Distance.

## See Also

[ISecondaryMemberUpToMembersFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.html)
[ISecondaryMemberUpToMembersFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
