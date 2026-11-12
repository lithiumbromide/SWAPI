---
title: "GetFromPointMembers Method (ISecondaryMemberUpToMembersFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberUpToMembersFeatureData"
member: "GetFromPointMembers"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~GetFromPointMembers.html"
---

# GetFromPointMembers Method (ISecondaryMemberUpToMembersFeatureData)

Gets the structure system member(s) connected to a from point to create one or more secondary structure system up-to members.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFromPointMembers() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberUpToMembersFeatureData
Dim value As System.Object

value = instance.GetFromPointMembers()
```

### C#

```csharp
System.object GetFromPointMembers()
```

### C++/CLI

```cpp
System.Object^ GetFromPointMembers();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.html)s

## VBA Syntax

See [SecondaryMemberUpToMembersFeatureData::GetFromPointMembers](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberUpToMembersFeatureData~GetFromPointMembers.html).

## Remarks

This method is valid only if [ISecondaryMemberUpToMembersFeatureData::MemberPointParametersType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~MemberPointParametersType.html) is set to [swSecondaryMemberUpToMembersMemberPointParameters_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberUpToMembersMemberPointParameters_e.html).swSecondaryMemberUpToMembersMemberPointParameters_FromPoint.

## See Also

[ISecondaryMemberUpToMembersFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.html)
[ISecondaryMemberUpToMembersFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
