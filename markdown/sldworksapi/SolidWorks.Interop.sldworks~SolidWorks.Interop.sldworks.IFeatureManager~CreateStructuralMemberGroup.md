---
title: "CreateStructuralMemberGroup Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "CreateStructuralMemberGroup"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateStructuralMemberGroup.html"
---

# CreateStructuralMemberGroup Method (IFeatureManager)

Creates a weldment structural-member group.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateStructuralMemberGroup() As StructuralMemberGroup
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As StructuralMemberGroup

value = instance.CreateStructuralMemberGroup()
```

### C#

```csharp
StructuralMemberGroup CreateStructuralMemberGroup()
```

### C++/CLI

```cpp
StructuralMemberGroup^ CreateStructuralMemberGroup();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Structural-member group](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberGroup.html)

## VBA Syntax

See [FeatureManager::CreateStructuralMemberGroup](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~CreateStructuralMemberGroup.html).

## Examples

[Insert Structural Weldment (C#)](Insert_Structural_Weldment_Example_CSharp.htm)
[Insert Structural Weldment (VB.NET)](Insert_Structural_Weldment_Example_VBNET.htm)
[Insert Structural Weldment (VBA)](Insert_Structural_Weldment_Example_VB.htm)
[Create Structural-Member Group (VBA)](Create_Structural_Member_Group_Example_VB.htm)
[Create Structural-Member Group (VB.NET)](Create_Structural_Member_Group_Example_VBNET.htm)
[Create Structural-Member Group (C#)](Create_Structural_Member_Group_Example_CSharp.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IStructuralMemberFeatureData::ISetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ISetGroups.html)
[IFeatureManager::InsertStructuralWeldment3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment3.html)

## Availability

SOLIDWORKS 2009 SP5, Revision 17.5
