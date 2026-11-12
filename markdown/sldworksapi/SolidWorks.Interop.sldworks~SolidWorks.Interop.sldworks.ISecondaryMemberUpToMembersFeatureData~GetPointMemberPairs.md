---
title: "GetPointMemberPairs Method (ISecondaryMemberUpToMembersFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberUpToMembersFeatureData"
member: "GetPointMemberPairs"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~GetPointMemberPairs.html"
---

# GetPointMemberPairs Method (ISecondaryMemberUpToMembersFeatureData)

Gets the point-member pair(s) used to create one or more secondary structure system up-to members.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetPointMemberPairs( _
   ByRef Points As System.Object, _
   ByRef Members As System.Object, _
   ByRef PointTypes As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberUpToMembersFeatureData
Dim Points As System.Object
Dim Members As System.Object
Dim PointTypes As System.Object

instance.GetPointMemberPairs(Points, Members, PointTypes)
```

### C#

```csharp
void GetPointMemberPairs(
   out System.object Points,
   out System.object Members,
   out System.object PointTypes
)
```

### C++/CLI

```cpp
void GetPointMemberPairs(
   [Out] System.Object^ Points,
   [Out] System.Object^ Members,
   [Out] System.Object^ PointTypes
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Points`: Array of [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)es or [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)s
- `Members`: Array of [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.html)s
- `PointTypes`: Array of Points types as defined by [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [SecondaryMemberUpToMembersFeatureData::GetPointMemberPairs](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberUpToMembersFeatureData~GetPointMemberPairs.html).

## Remarks

Points and Members arrays are ordered to create point-member pairs.

This method is valid only if [ISecondaryMemberUpToMembersFeatureData::MemberPointParametersType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~MemberPointParametersType.html) is set to [swSecondaryMemberUpToMembersMemberPointParameters_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberUpToMembersMemberPointParameters_e.html).swSecondaryMemberUpToMembersMemberPointParameters_PointMemberPair.

## See Also

[ISecondaryMemberUpToMembersFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.html)
[ISecondaryMemberUpToMembersFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
