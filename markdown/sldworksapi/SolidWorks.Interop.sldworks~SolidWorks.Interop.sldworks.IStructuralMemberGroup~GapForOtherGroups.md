---
title: "GapForOtherGroups Property (IStructuralMemberGroup)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberGroup"
member: "GapForOtherGroups"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~GapForOtherGroups.html"
---

# GapForOtherGroups Property (IStructuralMemberGroup)

Gets and sets the gap between segments in different structural-member groups.

## Syntax

### Visual Basic (Declaration)

```vb
Property GapForOtherGroups As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberGroup
Dim value As System.Double

instance.GapForOtherGroups = value

value = instance.GapForOtherGroups
```

### C#

```csharp
System.double GapForOtherGroups {get; set;}
```

### C++/CLI

```cpp
property System.double GapForOtherGroups {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Gap in meters between segments in different groups

## VBA Syntax

See [StructuralMemberGroup::GapForOtherGroups](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberGroup~GapForOtherGroups.html).

## Examples

[Merge Arc Segment Bodies With Adjacent Bodies (C#)](Merge_Arc_Segment_Bodies_With_Adjacent_Bodies_Example_CSharp.htm)
[Merge Arc Segment Bodies With Adjacent Bodies (VB.NET)](Merge_Arc_Segment_Bodies_With_Adjacent_Bodies_Example_VBNET.htm)
[Merge Arc Segment Bodies With Adjacent Bodies (VBA)](Merge_Arc_Segment_Bodies_With_Adjacent_Bodies_Example_VB.htm)

## See Also

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.html)
[IStructuralMemberGroup::GapWithinGroup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~GapWithinGroup.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
