---
title: "MirrorProfileAxis Property (IStructuralMemberGroup)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberGroup"
member: "MirrorProfileAxis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~MirrorProfileAxis.html"
---

# MirrorProfileAxis Property (IStructuralMemberGroup)

Gets and sets the axis about which to mirror the profile of this structural-member group.

## Syntax

### Visual Basic (Declaration)

```vb
Property MirrorProfileAxis As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberGroup
Dim value As System.Integer

instance.MirrorProfileAxis = value

value = instance.MirrorProfileAxis
```

### C#

```csharp
System.int MirrorProfileAxis {get; set;}
```

### C++/CLI

```cpp
property System.int MirrorProfileAxis {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Axis as defined in [swMirrorProfileOrAlignmentAxis_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMirrorProfileOrAlignmentAxis_e.html)

## VBA Syntax

See [StructuralMemberGroup::MirrorProfileAxis](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberGroup~MirrorProfileAxis.html).

## Examples

[Insert Structural Weldment (C#)](Insert_Structural_Weldment_Example_CSharp.htm)
[Insert Structural Weldment (VB.NET)](Insert_Structural_Weldment_Example_VBNET.htm)
[Insert Structural Weldment (VBA)](Insert_Structural_Weldment_Example_VB.htm)

## See Also

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.html)
[IStructuralMemberGroup::MirrorProfile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~MirrorProfile.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
