---
title: "GetStructureSystemMembers Method (IProfileGroupFolder)"
project: "SOLIDWORKS API Help"
interface: "IProfileGroupFolder"
member: "GetStructureSystemMembers"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~GetStructureSystemMembers.html"
---

# GetStructureSystemMembers Method (IProfileGroupFolder)

Gets the structure system members in this profile group folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStructureSystemMembers() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IProfileGroupFolder
Dim value As System.Object

value = instance.GetStructureSystemMembers()
```

### C#

```csharp
System.object GetStructureSystemMembers()
```

### C++/CLI

```cpp
System.Object^ GetStructureSystemMembers();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.html)s

## VBA Syntax

See [ProfileGroupFolder::GetStructureSystemMembers](ms-its:sldworksapivb6.chm::/sldworks~ProfileGroupFolder~GetStructureSystemMembers.html).

## Examples

See the [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.html) examples.

See the [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html) examples.

## See Also

[IProfileGroupFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder.html)
[IProfileGroupFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
