---
title: "GetSketch Method (IStructureSystemMemberProfile)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberProfile"
member: "GetSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~GetSketch.html"
---

# GetSketch Method (IStructureSystemMemberProfile)

Gets the sketch that contains all of the pierce points used to define this structure system member profile.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketch() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberProfile
Dim value As System.Object

value = instance.GetSketch()
```

### C#

```csharp
System.object GetSketch()
```

### C++/CLI

```cpp
System.Object^ GetSketch();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[ISketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)

## VBA Syntax

See [StructureSystemMemberProfile::GetSketch](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberProfile~GetSketch.html).

## See Also

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.html)
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
