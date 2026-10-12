---
title: "OffsetPiercePoint Property (IStructureSystemMemberProfile)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberProfile"
member: "OffsetPiercePoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~OffsetPiercePoint.html"
---

# OffsetPiercePoint Property (IStructureSystemMemberProfile)

Gets and sets whether to offset the pierce point of this member profile.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetPiercePoint As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberProfile
Dim value As System.Boolean

instance.OffsetPiercePoint = value

value = instance.OffsetPiercePoint
```

### C#

```csharp
System.bool OffsetPiercePoint {get; set;}
```

### C++/CLI

```cpp
property System.bool OffsetPiercePoint {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to offset the pierce point, false to not

## VBA Syntax

See [StructureSystemMemberProfile::OffsetPiercePoint](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberProfile~OffsetPiercePoint.html).

## Remarks

If this property is true, use [IStructureSystemMemberProfile::OffsetPiercePointHorizontalAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~OffsetPiercePointHorizontalAxis.html) and [IStructureSystemMemberProfile::OffsetPiercePointVerticalAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~OffsetPiercePointVerticalAxis.html) to specify the offsets.

## See Also

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.html)
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
