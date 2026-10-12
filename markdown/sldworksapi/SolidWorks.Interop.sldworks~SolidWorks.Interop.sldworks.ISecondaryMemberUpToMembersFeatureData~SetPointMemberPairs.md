---
title: "SetPointMemberPairs Method (ISecondaryMemberUpToMembersFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberUpToMembersFeatureData"
member: "SetPointMemberPairs"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~SetPointMemberPairs.html"
---

# SetPointMemberPairs Method (ISecondaryMemberUpToMembersFeatureData)

Sets the point-member pair(s) used to create one or more secondary structure system up-to members.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPointMemberPairs( _
   ByVal Points As System.Object, _
   ByVal Members As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberUpToMembersFeatureData
Dim Points As System.Object
Dim Members As System.Object
Dim value As System.Boolean

value = instance.SetPointMemberPairs(Points, Members)
```

### C#

```csharp
System.bool SetPointMemberPairs(
   System.object Points,
   System.object Members
)
```

### C++/CLI

```cpp
System.bool SetPointMemberPairs(
   System.Object^ Points,
   System.Object^ Members
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Points`: Array of [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)es or [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)s
- `Members`: Array of [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.html)s

## VBA Syntax

See [SecondaryMemberUpToMembersFeatureData::SetPointMemberPairs](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberUpToMembersFeatureData~SetPointMemberPairs.html).

## Remarks

Points and Members arrays must be ordered to create point-member pairs.

This method is valid only if [ISecondaryMemberUpToMembersFeatureData::MemberPointParametersType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~MemberPointParametersType.html) is set to [swSecondaryMemberUpToMembersMemberPointParameters_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberUpToMembersMemberPointParameters_e.html).swSecondaryMemberUpToMembersMemberPointParameters_PointMemberPair.

## See Also

[ISecondaryMemberUpToMembersFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.html)
[ISecondaryMemberUpToMembersFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
