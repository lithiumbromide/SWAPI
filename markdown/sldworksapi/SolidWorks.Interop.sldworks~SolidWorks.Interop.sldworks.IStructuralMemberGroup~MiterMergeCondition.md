---
title: "MiterMergeCondition Property (IStructuralMemberGroup)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberGroup"
member: "MiterMergeCondition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~MiterMergeCondition.html"
---

# MiterMergeCondition Property (IStructuralMemberGroup)

Get or set whether to merge miter trimmed bodies in this structural-member group.

## Syntax

### Visual Basic (Declaration)

```vb
Property MiterMergeCondition As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberGroup
Dim value As System.Boolean

instance.MiterMergeCondition = value

value = instance.MiterMergeCondition
```

### C#

```csharp
System.bool MiterMergeCondition {get; set;}
```

### C++/CLI

```cpp
property System.bool MiterMergeCondition {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to merge miter trimmed bodies, false to not

## VBA Syntax

See [StructuralMemberGroup::MiterMergeCondition](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberGroup~MiterMergeCondition.html).

## Examples

[Merge Miter Trimmed Bodies (C#)](Merge_Miter_Trimmed_Bodies_Example_CSharp.htm)
[Merge Miter Trimmed Bodies (VB.NET)](Merge_Miter_Trimmed_Bodies_Example_VBNET.htm)
[Merge Miter Trimmed Bodies (VBA)](Merge_Miter_Trimmed_Bodies_Example_VB.htm)

## Remarks

This property is only available when [IStructuralMemberGroup::CornerTreatmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~CornerTreatmentType.html) is [swSolidworksWeldmentEndCondOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSolidworksWeldmentEndCondOptions_e.html).swEndConditionMiter.

## See Also

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.html)
[IStructuralMemberGroup::ApplyCornerTreatment Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~ApplyCornerTreatment.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
