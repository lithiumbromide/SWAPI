---
title: "SetFromPoint Method (ISecondaryMemberUpToMembersFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberUpToMembersFeatureData"
member: "SetFromPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~SetFromPoint.html"
---

# SetFromPoint Method (ISecondaryMemberUpToMembersFeatureData)

Sets the point from which to extend this secondary structure system up-to member.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFromPoint( _
   ByVal Point As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberUpToMembersFeatureData
Dim Point As System.Object
Dim value As System.Boolean

value = instance.SetFromPoint(Point)
```

### C#

```csharp
System.bool SetFromPoint(
   System.object Point
)
```

### C++/CLI

```cpp
System.bool SetFromPoint(
   System.Object^ Point
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Point`: [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html) or [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)

## VBA Syntax

See [SecondaryMemberUpToMembersFeatureData::SetFromPoint](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberUpToMembersFeatureData~SetFromPoint.html).

## Examples

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html) examples.

## Remarks

This method is valid only if [ISecondaryMemberUpToMembersFeatureData::MemberPointParametersType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~MemberPointParametersType.html) is set to [swSecondaryMemberUpToMembersMemberPointParameters_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberUpToMembersMemberPointParameters_e.html).swSecondaryMemberUpToMembersMemberPointParameters_FromPoint.

## See Also

[ISecondaryMemberUpToMembersFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.html)
[ISecondaryMemberUpToMembersFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
