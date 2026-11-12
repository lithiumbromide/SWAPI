---
title: "GapWithinGroup Property (IStructuralMemberGroup)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberGroup"
member: "GapWithinGroup"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~GapWithinGroup.html"
---

# GapWithinGroup Property (IStructuralMemberGroup)

Gets and sets the gap between connected segments within this structural-member group.

## Syntax

### Visual Basic (Declaration)

```vb
Property GapWithinGroup As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberGroup
Dim value As System.Double

instance.GapWithinGroup = value

value = instance.GapWithinGroup
```

### C#

```csharp
System.double GapWithinGroup {get; set;}
```

### C++/CLI

```cpp
property System.double GapWithinGroup {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Gap in meters between connected segments within group

## VBA Syntax

See [StructuralMemberGroup::GapWithinGroup](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberGroup~GapWithinGroup.html).

## Examples

[Insert Structural Weldment (C#)](Insert_Structural_Weldment_Example_CSharp.htm)
[Insert Structural Weldment (VB.NET)](Insert_Structural_Weldment_Example_VBNET.htm)
[Insert Structural Weldment (VBA)](Insert_Structural_Weldment_Example_VB.htm)

## See Also

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.html)
[IStructuralMemberGroup::GapForOtherGroups Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~GapForOtherGroups.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
