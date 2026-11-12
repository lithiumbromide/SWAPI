---
title: "SecondaryMemberOffsetType Property (ISecondaryMemberUpToMembersFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberUpToMembersFeatureData"
member: "SecondaryMemberOffsetType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~SecondaryMemberOffsetType.html"
---

# SecondaryMemberOffsetType Property (ISecondaryMemberUpToMembersFeatureData)

Gets or sets the distance from end type for this secondary structure system up-to member.

## Syntax

### Visual Basic (Declaration)

```vb
Property SecondaryMemberOffsetType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberUpToMembersFeatureData
Dim value As System.Integer

instance.SecondaryMemberOffsetType = value

value = instance.SecondaryMemberOffsetType
```

### C#

```csharp
System.int SecondaryMemberOffsetType {get; set;}
```

### C++/CLI

```cpp
property System.int SecondaryMemberOffsetType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance from end type as defined by [swSecondaryMemberUpToMembersDistanceFromEndType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberUpToMembersDistanceFromEndType_e.html)

## VBA Syntax

See [SecondaryMemberUpToMembersFeatureData::SecondaryMemberOffsetType](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberUpToMembersFeatureData~SecondaryMemberOffsetType.html).

## Examples

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html) examples.

## See Also

[ISecondaryMemberUpToMembersFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.html)
[ISecondaryMemberUpToMembersFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
