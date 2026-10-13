---
title: "ProfileAlignmentAngle Property (IStructureSystemMemberProfile)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberProfile"
member: "ProfileAlignmentAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentAngle.html"
---

# ProfileAlignmentAngle Property (IStructureSystemMemberProfile)

Gets and sets the angle of alignment between this member profile and a specified entity.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileAlignmentAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberProfile
Dim value As System.Double

instance.ProfileAlignmentAngle = value

value = instance.ProfileAlignmentAngle
```

### C#

```csharp
System.double ProfileAlignmentAngle {get; set;}
```

### C++/CLI

```cpp
property System.double ProfileAlignmentAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Alignment angle in radians

## VBA Syntax

See [StructureSystemMemberProfile::ProfileAlignmentAngle](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberProfile~ProfileAlignmentAngle.html).

## Remarks

The angle is measured between an axis of the profile member as defined by [IStructureSystemMemberProfile::ProfileAlignmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentType.html) and an entity specified by [IStructureSystemMemberProfile::ProfileAlignmentObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentObject.html).

## See Also

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.html)
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
