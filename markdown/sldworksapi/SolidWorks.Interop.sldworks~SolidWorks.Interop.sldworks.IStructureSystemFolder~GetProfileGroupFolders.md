---
title: "GetProfileGroupFolders Method (IStructureSystemFolder)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemFolder"
member: "GetProfileGroupFolders"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder~GetProfileGroupFolders.html"
---

# GetProfileGroupFolders Method (IStructureSystemFolder)

Gets the profile group folders in this structure system folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProfileGroupFolders() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemFolder
Dim value As System.Object

value = instance.GetProfileGroupFolders()
```

### C#

```csharp
System.object GetProfileGroupFolders()
```

### C++/CLI

```cpp
System.Object^ GetProfileGroupFolders();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IProfileGroupFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder.html)s

## VBA Syntax

See [StructureSystemFolder::GetProfileGroupFolders](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemFolder~GetProfileGroupFolders.html).

## Examples

See the [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.html) examples.

See the [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html) examples.

See the [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.html) examples.

See the [IPrimaryMemberRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.html) examples.

## See Also

[IStructureSystemFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder.html)
[IStructureSystemFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
