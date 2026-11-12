---
title: "ISetGroups Method (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "ISetGroups"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ISetGroups.html"
---

# ISetGroups Method (IStructuralMemberFeatureData)

Sets the structural-member groups to use in this structural member.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetGroups( _
   ByVal Count As System.Integer, _
   ByRef SegGroups As StructuralMemberGroup _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim Count As System.Integer
Dim SegGroups As StructuralMemberGroup

instance.ISetGroups(Count, SegGroups)
```

### C#

```csharp
void ISetGroups(
   System.int Count,
   ref StructuralMemberGroup SegGroups
)
```

### C++/CLI

```cpp
void ISetGroups(
   System.int Count,
   StructuralMemberGroup^% SegGroups
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of structural-member groups
- `SegGroups`: - in-process, unmanaged C++: Pointer to an array of [structural-member groups](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberGroup.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This method works only for features that support groups. A feature supports groups only if [IStructuralMemberFeatureData::GetGroupsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~GetGroupsCount.html) > 0.

Call [IFeatureManager::CreateStructuralMemberGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~CreateStructuralMemberGroup.html) to create groups.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)
[IStructuralMemberFeatureData::IGetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetGroups.html)
[IStructuralMemberFeatureData::Groups Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~Groups.html)
[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)

## Availability

SOLIDWORKS 2009 SP5, Revision Number 17.5
