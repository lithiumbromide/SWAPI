---
title: "Segments Property (IStructuralMemberGroup)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberGroup"
member: "Segments"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~Segments.html"
---

# Segments Property (IStructuralMemberGroup)

Gets and sets the sketch segments to use in this structural-member group.

## Syntax

### Visual Basic (Declaration)

```vb
Property Segments As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberGroup
Dim value As System.Object

instance.Segments = value

value = instance.Segments
```

### C#

```csharp
System.object Segments {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Segments {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)

## VBA Syntax

See [StructuralMemberGroup::Segments](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberGroup~Segments.html).

## Examples

[Insert Structural Weldment (C#)](Insert_Structural_Weldment_Example_CSharp.htm)
[Insert Structural Weldment (VB.NET)](Insert_Structural_Weldment_Example_VBNET.htm)
[Insert Structural Weldment (VBA)](Insert_Structural_Weldment_Example_VB.htm)
[Create Structural-Member Group (VBA)](Create_Structural_Member_Group_Example_VB.htm)
[Create Structural-Member Group (VB.NET)](Create_Structural_Member_Group_Example_VBNET.htm)
[Create Structural-Member Group (C#)](Create_Structural_Member_Group_Example_CSharp.htm)

## See Also

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.html)
[IStructuralMemberGroup::IGetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~IGetSegments.html)
[IStructuralMemberGroup::ISetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~ISetSegments.html)

## Availability

SOLIDWORKS 2009 SP5, Revision Number 17.5
