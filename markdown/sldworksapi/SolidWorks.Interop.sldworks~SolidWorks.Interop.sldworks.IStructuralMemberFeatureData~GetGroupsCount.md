---
title: "GetGroupsCount Method (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "GetGroupsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetGroupsCount.html"
---

# GetGroupsCount Method (IStructuralMemberFeatureData)

Gets the number of structural-member groups for this structural member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGroupsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim value As System.Integer

value = instance.GetGroupsCount()
```

### C#

```csharp
System.int GetGroupsCount()
```

### C++/CLI

```cpp
System.int GetGroupsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of structural-member groups

## VBA Syntax

See [StructuralMemberFeatureData::GetGroupsCount](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberFeatureData~GetGroupsCount.html).

## Examples

[Insert Structural Weldment (C#)](Insert_Structural_Weldment_Example_CSharp.htm)
[Insert Structural Weldment (VB.NET)](Insert_Structural_Weldment_Example_VBNET.htm)
[Insert Structural Weldment (VBA)](Insert_Structural_Weldment_Example_VB.htm)
[Create Structural-Member Group (VBA)](Create_Structural_Member_Group_Example_VB.htm)
[Create Structural-Member Group (VB.NET)](Create_Structural_Member_Group_Example_VBNET.htm)
[Create Structural-Member Group (C#)](Create_Structural_Member_Group_Example_CSharp.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)
[IStructuralMemberFeatureData::Groups Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~Groups.html)
[IStructuralMemberFeatureData::IGetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetGroups.html)
[IStructuralMemberFeatureData::ISetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ISetGroups.html)

## Availability

SOLIDWORKS 2009 SP5, Revision Number 17.5
