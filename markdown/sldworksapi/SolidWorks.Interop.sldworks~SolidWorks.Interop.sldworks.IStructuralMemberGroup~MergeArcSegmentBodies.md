---
title: "MergeArcSegmentBodies Property (IStructuralMemberGroup)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberGroup"
member: "MergeArcSegmentBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~MergeArcSegmentBodies.html"
---

# MergeArcSegmentBodies Property (IStructuralMemberGroup)

Gets or sets whether to merge arc segment bodies with adjacent bodies in this structural-member group.

## Syntax

### Visual Basic (Declaration)

```vb
Property MergeArcSegmentBodies As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberGroup
Dim value As System.Boolean

instance.MergeArcSegmentBodies = value

value = instance.MergeArcSegmentBodies
```

### C#

```csharp
System.bool MergeArcSegmentBodies {get; set;}
```

### C++/CLI

```cpp
property System.bool MergeArcSegmentBodies {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to merge arc segment bodies with adjacent bodies, false to not

## VBA Syntax

See [StructuralMemberGroup::MergeArcSegmentBodies](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberGroup~MergeArcSegmentBodies.html).

## Examples

[Merge Arc Segment Bodies With Adjacent Bodies (C#)](Merge_Arc_Segment_Bodies_With_Adjacent_Bodies_Example_CSharp.htm)
[Merge Arc Segment Bodies With Adjacent Bodies (VB.NET)](Merge_Arc_Segment_Bodies_With_Adjacent_Bodies_Example_VBNET.htm)
[Merge Arc Segment Bodies With Adjacent Bodies (VBA)](Merge_Arc_Segment_Bodies_With_Adjacent_Bodies_Example_VB.htm)

## Remarks

This property is valid for curved entities only. The arc segment and adjacent bodies must be tangent to merge.

## See Also

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
