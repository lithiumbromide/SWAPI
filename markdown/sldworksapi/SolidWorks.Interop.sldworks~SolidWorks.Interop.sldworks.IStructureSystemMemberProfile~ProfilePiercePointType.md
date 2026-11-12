---
title: "ProfilePiercePointType Property (IStructureSystemMemberProfile)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberProfile"
member: "ProfilePiercePointType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfilePiercePointType.html"
---

# ProfilePiercePointType Property (IStructureSystemMemberProfile)

Gets and sets the type of pierce point used to define the sketch of this structure system member profile.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfilePiercePointType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberProfile
Dim value As System.Integer

instance.ProfilePiercePointType = value

value = instance.ProfilePiercePointType
```

### C#

```csharp
System.int ProfilePiercePointType {get; set;}
```

### C++/CLI

```cpp
property System.int ProfilePiercePointType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of pierce point as defined by [swStructureProfilePiercePointType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStructureProfilePiercePointType_e.html)

## VBA Syntax

See [StructureSystemMemberProfile::ProfilePiercePointType](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberProfile~ProfilePiercePointType.html).

## Remarks

Gets and sets the type of pierce point for the sketch of this member profile.

## See Also

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.html)
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
