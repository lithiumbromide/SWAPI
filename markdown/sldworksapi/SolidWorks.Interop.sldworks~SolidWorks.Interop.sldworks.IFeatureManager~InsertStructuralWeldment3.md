---
title: "InsertStructuralWeldment3 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertStructuralWeldment3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment3.html"
---

# InsertStructuralWeldment3 Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertStructuralWeldment4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertStructuralWeldment4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertStructuralWeldment3( _
   ByVal Path As System.String, _
   ByVal EndCond As System.Integer, _
   ByVal Angle As System.Double, _
   ByVal Merge As System.Boolean, _
   ByVal Groups As System.Object _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Path As System.String
Dim EndCond As System.Integer
Dim Angle As System.Double
Dim Merge As System.Boolean
Dim Groups As System.Object
Dim value As Feature

value = instance.InsertStructuralWeldment3(Path, EndCond, Angle, Merge, Groups)
```

### C#

```csharp
Feature InsertStructuralWeldment3(
   System.string Path,
   System.int EndCond,
   System.double Angle,
   System.bool Merge,
   System.object Groups
)
```

### C++/CLI

```cpp
Feature^ InsertStructuralWeldment3(
   System.String^ Path,
   System.int EndCond,
   System.double Angle,
   System.bool Merge,
   System.Object^ Groups
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Path`: Path, filename, and name of the type of structural member to insert
- `EndCond`: End condition as defined in [swSOLIDWORKSWeldmentEndCondOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSOLIDWORKSWeldmentEndCondOptions_e.html)
- `Angle`: Angle of rotation of the sketch about the sketch segment
- `Merge`: True to merge the bodies of the arc segments to the adjacent bodies, false to not
- `Groups`: Array of [IStructuralMemberGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberGroup.html)

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertStructuralWeldment3](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertStructuralWeldment3.html).

## Examples

[Insert Weldment Features (VBA)](Insert_Weldment_Features_Example_VB.htm)
[Insert Weldment Features (VB.NET)](Insert_Weldment_Features_Example_VBNET.htm)
[Create Structural-Member Group (VBA)](Create_Structural_Member_Group_Example_VB.htm)
[Create Structural-Member Group (VB.NET)](Create_Structural_Member_Group_Example_VBNET.htm)
[Create Structural-Member Group (C#)](Create_Structural_Member_Group_Example_CSharp.htm)
[Insert Weldment Features (C#)](Insert_Weldment_Features_Example_CSharp.htm)

## Remarks

Use [IFeatureManager::CreateStructuralMemberGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~CreateStructuralMemberGroup.html), [IStructuralMemberFeatureData::Groups](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~Groups.html), or [IStructuralMemberFeatureData::IGetGroups](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~IGetGroups.html) to populate the `Groups` parameter.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)

## Availability

SOLIDWORKS 2009 SP5, Revision Number 17.5
