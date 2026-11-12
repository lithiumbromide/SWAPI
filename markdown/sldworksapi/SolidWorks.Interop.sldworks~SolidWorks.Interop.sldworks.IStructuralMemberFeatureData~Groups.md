---
title: "Groups Property (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "Groups"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~Groups.html"
---

# Groups Property (IStructuralMemberFeatureData)

Gets or sets the groups to use in this structural member.

## Syntax

### Visual Basic (Declaration)

```vb
Property Groups As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim value As System.Object

instance.Groups = value

value = instance.Groups
```

### C#

```csharp
System.object Groups {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Groups {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [IStructuralMemberGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberGroup.html) objects

## VBA Syntax

See [StructuralMemberFeatureData::Groups](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberFeatureData~Groups.html).

## Examples

[Insert Structural Weldment (C#)](Insert_Structural_Weldment_Example_CSharp.htm)
[Insert Structural Weldment (VB.NET)](Insert_Structural_Weldment_Example_VBNET.htm)
[Insert Structural Weldment (VBA)](Insert_Structural_Weldment_Example_VB.htm)
[Create Structural-Member Group (VBA)](Create_Structural_Member_Group_Example_VB.htm)
[Create Structural-Member Group (VB.NET)](Create_Structural_Member_Group_Example_VBNET.htm)
[Create Structural-Member Group (C#)](Create_Structural_Member_Group_Example_CSharp.htm)

## Remarks

This method works only for features that support groups. A feature supports groups only if [IStructuralMemberFeatureData::GetGroupsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~GetGroupsCount.html) > 0.

Call [IFeatureManager::CreateStructuralMemberGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~CreateStructuralMemberGroup.html) to create groups.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)
[IStructuralMemberFeatureData::IGetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetGroups.html)
[IStructuralMemberFeatureData::ISetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ISetGroups.html)
[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)

## Availability

SOLIDWORKS 2009 SP5, Revision Number 17.5
