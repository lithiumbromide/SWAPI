---
title: "ApplyCornerTreatment Property (IStructuralMemberGroup)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberGroup"
member: "ApplyCornerTreatment"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~ApplyCornerTreatment.html"
---

# ApplyCornerTreatment Property (IStructuralMemberGroup)

Gets and sets whether or not to apply a corner treatment to this structural-member group.

## Syntax

### Visual Basic (Declaration)

```vb
Property ApplyCornerTreatment As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberGroup
Dim value As System.Boolean

instance.ApplyCornerTreatment = value

value = instance.ApplyCornerTreatment
```

### C#

```csharp
System.bool ApplyCornerTreatment {get; set;}
```

### C++/CLI

```cpp
property System.bool ApplyCornerTreatment {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to apply corner treatment, false to not

## VBA Syntax

See [StructuralMemberGroup::ApplyCornerTreatment](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberGroup~ApplyCornerTreatment.html).

## Examples

[Insert Structural Weldment (C#)](Insert_Structural_Weldment_Example_CSharp.htm)
[Insert Structural Weldment (VB.NET)](Insert_Structural_Weldment_Example_VBNET.htm)
[Insert Structural Weldment (VBA)](Insert_Structural_Weldment_Example_VB.htm)

## See Also

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.html)
[IStructuralMemberGroup::CornerTreatmentType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~CornerTreatmentType.html)
[IStructuralMemberGroup::MiterMergeCondition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~MiterMergeCondition.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
