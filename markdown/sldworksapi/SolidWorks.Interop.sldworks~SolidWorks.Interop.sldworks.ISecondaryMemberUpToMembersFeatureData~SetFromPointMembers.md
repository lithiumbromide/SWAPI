---
title: "SetFromPointMembers Method (ISecondaryMemberUpToMembersFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberUpToMembersFeatureData"
member: "SetFromPointMembers"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~SetFromPointMembers.html"
---

# SetFromPointMembers Method (ISecondaryMemberUpToMembersFeatureData)

Sets the structure system member(s) connected to a from point to create one or more secondary structure system up-to members.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFromPointMembers( _
   ByVal Members As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberUpToMembersFeatureData
Dim Members As System.Object
Dim value As System.Boolean

value = instance.SetFromPointMembers(Members)
```

### C#

```csharp
System.bool SetFromPointMembers(
   System.object Members
)
```

### C++/CLI

```cpp
System.bool SetFromPointMembers(
   System.Object^ Members
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Members`: Array of [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.html)s

### Return Value

True if From point member successfully set, false if not

## VBA Syntax

See [SecondaryMemberUpToMembersFeatureData::SetFromPointMembers](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberUpToMembersFeatureData~SetFromPointMembers.html).

## Examples

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html) examples.

## Remarks

This property is valid only if [ISecondaryMemberUpToMembersFeatureData::MemberPointParametersType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~MemberPointParametersType.html) is set to [swSecondaryMemberUpToMembersMemberPointParameters_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberUpToMembersMemberPointParameters_e.html).swSecondaryMemberUpToMembersMemberPointParameters_FromPoint.

## See Also

[ISecondaryMemberUpToMembersFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.html)
[ISecondaryMemberUpToMembersFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
