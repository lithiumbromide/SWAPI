---
title: "MemberPointParametersType Property (ISecondaryMemberUpToMembersFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberUpToMembersFeatureData"
member: "MemberPointParametersType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~MemberPointParametersType.html"
---

# MemberPointParametersType Property (ISecondaryMemberUpToMembersFeatureData)

Gets or sets the point parameter used to create this secondary structure system up-to member.

## Syntax

### Visual Basic (Declaration)

```vb
Property MemberPointParametersType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberUpToMembersFeatureData
Dim value As System.Integer

instance.MemberPointParametersType = value

value = instance.MemberPointParametersType
```

### C#

```csharp
System.int MemberPointParametersType {get; set;}
```

### C++/CLI

```cpp
property System.int MemberPointParametersType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Point parameter as defined by [swSecondaryMemberUpToMembersMemberPointParameters_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberUpToMembersMemberPointParameters_e.html)

## VBA Syntax

See [SecondaryMemberUpToMembersFeatureData::MemberPointParametersType](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberUpToMembersFeatureData~MemberPointParametersType.html).

## Examples

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html) examples.

## Remarks

The setter of this method is valid only during creation. As in the user interface, you cannot change the member point parameters type after the secondary structure system member is created.

## See Also

[ISecondaryMemberUpToMembersFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.html)
[ISecondaryMemberUpToMembersFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
