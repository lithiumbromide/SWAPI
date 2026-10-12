---
title: "CornerTreatmentType Property (IStructuralMemberGroup)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberGroup"
member: "CornerTreatmentType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~CornerTreatmentType.html"
---

# CornerTreatmentType Property (IStructuralMemberGroup)

Gets and sets the type of corner treatment for this structural-member group.

## Syntax

### Visual Basic (Declaration)

```vb
Property CornerTreatmentType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberGroup
Dim value As System.Integer

instance.CornerTreatmentType = value

value = instance.CornerTreatmentType
```

### C#

```csharp
System.int CornerTreatmentType {get; set;}
```

### C++/CLI

```cpp
property System.int CornerTreatmentType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of corner treatment as defined in [swSolidworksWeldmentEndCondOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSolidworksWeldmentEndCondOptions_e.html)

## VBA Syntax

See [StructuralMemberGroup::CornerTreatmentType](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberGroup~CornerTreatmentType.html).

## Examples

[Insert Structural Weldment (C#)](Insert_Structural_Weldment_Example_CSharp.htm)
[Insert Structural Weldment (VB.NET)](Insert_Structural_Weldment_Example_VBNET.htm)
[Insert Structural Weldment (VBA)](Insert_Structural_Weldment_Example_VB.htm)

## Remarks

This property is only available when [IStructuralMemberGroup::ApplyCornerTreatment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~ApplyCornerTreatment.html) is true.

## See Also

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.html)
[IStructuralMemberGroup::MiterMergeCondition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~MiterMergeCondition.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
