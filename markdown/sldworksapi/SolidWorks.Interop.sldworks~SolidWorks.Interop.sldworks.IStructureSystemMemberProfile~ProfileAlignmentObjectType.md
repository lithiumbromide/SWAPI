---
title: "ProfileAlignmentObjectType Property (IStructureSystemMemberProfile)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberProfile"
member: "ProfileAlignmentObjectType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentObjectType.html"
---

# ProfileAlignmentObjectType Property (IStructureSystemMemberProfile)

Gets the type of profile alignment entity.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ProfileAlignmentObjectType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberProfile
Dim value As System.Integer

value = instance.ProfileAlignmentObjectType
```

### C#

```csharp
System.int ProfileAlignmentObjectType {get;}
```

### C++/CLI

```cpp
property System.int ProfileAlignmentObjectType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Profile alignment object type as defined by [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html):

- swSelDATUMPLANES
- swSelDATUMAXES
- swSelDATUMLINES
- swSelFACES
- swSelEDGES
- swSelSKETCHSEGS
- swSelSURFACEBODIES

## VBA Syntax

See [StructureSystemMemberProfile::ProfileAlignmentObjectType](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberProfile~ProfileAlignmentObjectType.html).

## See Also

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.html)
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
