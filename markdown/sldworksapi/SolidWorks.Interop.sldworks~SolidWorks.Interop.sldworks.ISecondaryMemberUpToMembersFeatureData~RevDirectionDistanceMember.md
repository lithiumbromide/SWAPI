---
title: "RevDirectionDistanceMember Property (ISecondaryMemberUpToMembersFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberUpToMembersFeatureData"
member: "RevDirectionDistanceMember"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~RevDirectionDistanceMember.html"
---

# RevDirectionDistanceMember Property (ISecondaryMemberUpToMembersFeatureData)

Gets or sets whether to flip the direction of the distance offset for this secondary structure system up-to member.

## Syntax

### Visual Basic (Declaration)

```vb
Property RevDirectionDistanceMember As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberUpToMembersFeatureData
Dim value As System.Boolean

instance.RevDirectionDistanceMember = value

value = instance.RevDirectionDistanceMember
```

### C#

```csharp
System.bool RevDirectionDistanceMember {get; set;}
```

### C++/CLI

```cpp
property System.bool RevDirectionDistanceMember {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the direction of the offset, false to not

## VBA Syntax

See [SecondaryMemberUpToMembersFeatureData::RevDirectionDistanceMember](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberUpToMembersFeatureData~RevDirectionDistanceMember.html).

## Examples

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html) examples.

## Remarks

This property is valid only if [ISecondaryMemberUpToMembersFeatureData::SecondaryMemberOffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~SecondaryMemberOffsetType.html) is set to [swSecondaryMemberUpToMembersDistanceFromEndType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberUpToMembersDistanceFromEndType_e.html).swSecondaryMemberUpToMembersDistanceFromEndType_Distance.

## See Also

[ISecondaryMemberUpToMembersFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.html)
[ISecondaryMemberUpToMembersFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
