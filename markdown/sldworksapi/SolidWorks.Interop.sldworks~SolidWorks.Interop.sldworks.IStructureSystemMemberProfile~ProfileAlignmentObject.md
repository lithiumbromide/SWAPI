---
title: "ProfileAlignmentObject Property (IStructureSystemMemberProfile)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberProfile"
member: "ProfileAlignmentObject"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentObject.html"
---

# ProfileAlignmentObject Property (IStructureSystemMemberProfile)

Gets and sets the entity with which to align an axis of this member profile.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileAlignmentObject As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberProfile
Dim value As System.Object

instance.ProfileAlignmentObject = value

value = instance.ProfileAlignmentObject
```

### C#

```csharp
System.object ProfileAlignmentObject {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ProfileAlignmentObject {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Direction entity with which to align an axis of the member profile, e.g.:

- [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
- [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
- [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
- [IRefAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html)
- [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)
- [ISketchLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html)
- [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
- [ISurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)

## VBA Syntax

See [StructureSystemMemberProfile::ProfileAlignmentObject](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberProfile~ProfileAlignmentObject.html).

## Remarks

Use:

- [IStructureSystemMemberProfile::ProfileAlignmentObjectType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentObjectType.html) to specify the type of this entity.
- [IStructureSystemMemberProfile::ProfileAlignmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentType.html) to specify to which axis of the member profile to align the entity specified by this property.
- [IStructureSystemMemberProfile::ProfileAlignmentAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentAngle.html) to specify the angle of alignment with the specified entity and member axis.

## See Also

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.html)
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
