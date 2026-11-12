---
title: "Angle Property (IStructuralMemberGroup)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberGroup"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~Angle.html"
---

# Angle Property (IStructuralMemberGroup)

Gets and sets the rotational angle of this structural-member group.

## Syntax

### Visual Basic (Declaration)

```vb
Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberGroup
Dim value As System.Double

instance.Angle = value

value = instance.Angle
```

### C#

```csharp
System.double Angle {get; set;}
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Rotational angle in radians

## VBA Syntax

See [StructuralMemberGroup::Angle](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberGroup~Angle.html).

## Examples

[Insert Structural Weldment (C#)](Insert_Structural_Weldment_Example_CSharp.htm)
[Insert Structural Weldment (VB.NET)](Insert_Structural_Weldment_Example_VBNET.htm)
[Insert Structural Weldment (VBA)](Insert_Structural_Weldment_Example_VB.htm)
[Create Structural Member Group (VBA)](Create_Structural_Member_Group_Example_VB.htm)
[Create Structural Member Group (VB.NET)](Create_Structural_Member_Group_Example_VBNET.htm)
[Create Structural Member Group (C#)](Create_Structural_Member_Group_Example_CSharp.htm)

## See Also

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.html)

## Availability

SOLIDWORKS 2009 SP5, Revision Number 17.5
