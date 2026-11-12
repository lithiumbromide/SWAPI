---
title: "ProfileAlignmentType Property (IStructureSystemMemberProfile)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberProfile"
member: "ProfileAlignmentType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentType.html"
---

# ProfileAlignmentType Property (IStructureSystemMemberProfile)

Gets and sets the axis of alignment for this member profile.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileAlignmentType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberProfile
Dim value As System.Integer

instance.ProfileAlignmentType = value

value = instance.ProfileAlignmentType
```

### C#

```csharp
System.int ProfileAlignmentType {get; set;}
```

### C++/CLI

```cpp
property System.int ProfileAlignmentType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Profile alignment type as defined by [swStructureProfileAlignmentType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStructureProfileAlignmentType_e.html)

## VBA Syntax

See [StructureSystemMemberProfile::ProfileAlignmentType](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberProfile~ProfileAlignmentType.html).

## Remarks

This property is valid only if [IStructureSystemMemberProfile::ProfileAlignmentObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentObject.html) is set.

## See Also

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.html)
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
