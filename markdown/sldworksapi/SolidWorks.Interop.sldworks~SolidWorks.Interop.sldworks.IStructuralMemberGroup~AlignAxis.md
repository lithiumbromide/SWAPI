---
title: "AlignAxis Property (IStructuralMemberGroup)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberGroup"
member: "AlignAxis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~AlignAxis.html"
---

# AlignAxis Property (IStructuralMemberGroup)

Gets and sets the axis on which to align this structural-member group.

## Syntax

### Visual Basic (Declaration)

```vb
Property AlignAxis As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberGroup
Dim value As System.Integer

instance.AlignAxis = value

value = instance.AlignAxis
```

### C#

```csharp
System.int AlignAxis {get; set;}
```

### C++/CLI

```cpp
property System.int AlignAxis {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Axis as defined in [swMirrorProfileOrAlignmentAxis_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMirrorProfileOrAlignmentAxis_e.html)

## VBA Syntax

See [StructuralMemberGroup::AlignAxis](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberGroup~AlignAxis.html).

## Examples

[Insert Structural Weldment (C#)](Insert_Structural_Weldment_Example_CSharp.htm)
[Insert Structural Weldment (VB.NET)](Insert_Structural_Weldment_Example_VBNET.htm)
[Insert Structural Weldment (VBA)](Insert_Structural_Weldment_Example_VB.htm)

## See Also

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
