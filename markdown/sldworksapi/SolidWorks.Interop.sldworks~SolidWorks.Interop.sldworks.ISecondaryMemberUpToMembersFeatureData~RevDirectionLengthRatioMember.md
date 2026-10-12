---
title: "RevDirectionLengthRatioMember Property (ISecondaryMemberUpToMembersFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberUpToMembersFeatureData"
member: "RevDirectionLengthRatioMember"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~RevDirectionLengthRatioMember.html"
---

# RevDirectionLengthRatioMember Property (ISecondaryMemberUpToMembersFeatureData)

Gets or sets whether to flip the direction of the length ratio offset of this secondary structure system up-to member.

## Syntax

### Visual Basic (Declaration)

```vb
Property RevDirectionLengthRatioMember As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberUpToMembersFeatureData
Dim value As System.Boolean

instance.RevDirectionLengthRatioMember = value

value = instance.RevDirectionLengthRatioMember
```

### C#

```csharp
System.bool RevDirectionLengthRatioMember {get; set;}
```

### C++/CLI

```cpp
property System.bool RevDirectionLengthRatioMember {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the direction of the offset, false to not

## VBA Syntax

See [SecondaryMemberUpToMembersFeatureData::RevDirectionLengthRatioMember](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberUpToMembersFeatureData~RevDirectionLengthRatioMember.html).

## Remarks

This property is valid only if [ISecondaryMemberUpToMembersFeatureData::SecondaryMemberOffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~SecondaryMemberOffsetType.html) is set to [swSecondaryMemberUpToMembersDistanceFromEndType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberUpToMembersDistanceFromEndType_e.html).swSecondaryMemberUpToMembersDistanceFromEndType_LengthRatio.

## See Also

[ISecondaryMemberUpToMembersFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.html)
[ISecondaryMemberUpToMembersFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
