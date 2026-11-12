---
title: "ProfileMirrorType Property (IStructureSystemMemberProfile)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberProfile"
member: "ProfileMirrorType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileMirrorType.html"
---

# ProfileMirrorType Property (IStructureSystemMemberProfile)

Gets and sets the axis about which to flip this member profile.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileMirrorType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberProfile
Dim value As System.Integer

instance.ProfileMirrorType = value

value = instance.ProfileMirrorType
```

### C#

```csharp
System.int ProfileMirrorType {get; set;}
```

### C++/CLI

```cpp
property System.int ProfileMirrorType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Axis about which to flip this member profile as defined by [swStructureProfileMirrorType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStructureProfileMirrorType_e.html)

## VBA Syntax

See [StructureSystemMemberProfile::ProfileMirrorType](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberProfile~ProfileMirrorType.html).

## Remarks

This property is valid only if [IStructureSystemMemberProfile::MirrorProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~MirrorProfile.html) is true.

## See Also

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.html)
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
