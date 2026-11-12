---
title: "MirrorProfile Property (IStructureSystemMemberProfile)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberProfile"
member: "MirrorProfile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~MirrorProfile.html"
---

# MirrorProfile Property (IStructureSystemMemberProfile)

Gets and sets whether to flip the profile of this member about an axis.

## Syntax

### Visual Basic (Declaration)

```vb
Property MirrorProfile As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberProfile
Dim value As System.Boolean

instance.MirrorProfile = value

value = instance.MirrorProfile
```

### C#

```csharp
System.bool MirrorProfile {get; set;}
```

### C++/CLI

```cpp
property System.bool MirrorProfile {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the profile of the member about an axis, false to not

## VBA Syntax

See [StructureSystemMemberProfile::MirrorProfile](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberProfile~MirrorProfile.html).

## Remarks

Use [IStructureSystemMemberProfile::ProfileMirrorType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileMirrorType.html) to specify either the horizontal or vertical axis about which to flip the member profile.

## See Also

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.html)
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
