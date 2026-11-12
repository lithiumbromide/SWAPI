---
title: "LengthRatioMember Property (ISecondaryMemberUpToMembersFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberUpToMembersFeatureData"
member: "LengthRatioMember"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~LengthRatioMember.html"
---

# LengthRatioMember Property (ISecondaryMemberUpToMembersFeatureData)

Gets or sets the length ratio with which to offset this secondary structure system up-to member.

## Syntax

### Visual Basic (Declaration)

```vb
Property LengthRatioMember As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberUpToMembersFeatureData
Dim value As System.Double

instance.LengthRatioMember = value

value = instance.LengthRatioMember
```

### C#

```csharp
System.double LengthRatioMember {get; set;}
```

### C++/CLI

```cpp
property System.double LengthRatioMember {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 <= Length ratio <= 1.0

## VBA Syntax

See [SecondaryMemberUpToMembersFeatureData::LengthRatioMember](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberUpToMembersFeatureData~LengthRatioMember.html).

## Remarks

This property is valid only if [ISecondaryMemberUpToMembersFeatureData::SecondaryMemberOffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~SecondaryMemberOffsetType.html) is set to [swSecondaryMemberUpToMembersDistanceFromEndType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberUpToMembersDistanceFromEndType_e.html).swSecondaryMemberUpToMembersDistanceFromEndType_LengthRatio.

## See Also

[ISecondaryMemberUpToMembersFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.html)
[ISecondaryMemberUpToMembersFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
