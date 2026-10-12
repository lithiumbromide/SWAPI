---
title: "IGetGroups Method (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "IGetGroups"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetGroups.html"
---

# IGetGroups Method (IStructuralMemberFeatureData)

Gets the structural-member groups in this structural member.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetGroups( _
   ByVal Count As System.Integer _
) As StructuralMemberGroup
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim Count As System.Integer
Dim value As StructuralMemberGroup

value = instance.IGetGroups(Count)
```

### C#

```csharp
StructuralMemberGroup IGetGroups(
   System.int Count
)
```

### C++/CLI

```cpp
StructuralMemberGroup^ IGetGroups(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of structural-member groups

### Return Value

- in-process, unmanaged C++: Pointer to an array of [structural-member groups](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberGroup.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IStructuralMemberFeatureData::GetGroupsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~GetGroupsCount.html) to set the Count parameter.

This method works only for features that support groups. A feature supports groups only if [IStructuralMemberFeatureData::GetGroupsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~GetGroupsCount.html) > 0.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)
[IStructuralMemberFeatureData::ISetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ISetGroups.html)
[IStructuralMemberFeatureData::Groups Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~Groups.html)
[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)

## Availability

SOLIDWORKS 2009 SP5, Revision Number 17.5
