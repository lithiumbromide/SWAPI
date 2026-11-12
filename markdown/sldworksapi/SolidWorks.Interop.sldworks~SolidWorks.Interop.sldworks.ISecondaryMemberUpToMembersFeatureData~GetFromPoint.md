---
title: "GetFromPoint Method (ISecondaryMemberUpToMembersFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberUpToMembersFeatureData"
member: "GetFromPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~GetFromPoint.html"
---

# GetFromPoint Method (ISecondaryMemberUpToMembersFeatureData)

Gets the point from which to extend this secondary structure system up-to member.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetFromPoint( _
   ByRef Point As System.Object, _
   ByRef PointType As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberUpToMembersFeatureData
Dim Point As System.Object
Dim PointType As System.Integer

instance.GetFromPoint(Point, PointType)
```

### C#

```csharp
void GetFromPoint(
   out System.object Point,
   out System.int PointType
)
```

### C++/CLI

```cpp
void GetFromPoint(
   [Out] System.Object^ Point,
   [Out] System.int PointType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Point`: [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html) or [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
- `PointType`: Type of Point as defined by [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [SecondaryMemberUpToMembersFeatureData::GetFromPoint](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberUpToMembersFeatureData~GetFromPoint.html).

## Remarks

This method is valid only if [ISecondaryMemberUpToMembersFeatureData::MemberPointParametersType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~MemberPointParametersType.html) is set to [swSecondaryMemberUpToMembersMemberPointParameters_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberUpToMembersMemberPointParameters_e.html).swSecondaryMemberUpToMembersMemberPointParameters_FromPoint.

## See Also

[ISecondaryMemberUpToMembersFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.html)
[ISecondaryMemberUpToMembersFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
