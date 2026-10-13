---
title: "OffsetPiercePointHorizontalAxis Property (IStructureSystemMemberProfile)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberProfile"
member: "OffsetPiercePointHorizontalAxis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~OffsetPiercePointHorizontalAxis.html"
---

# OffsetPiercePointHorizontalAxis Property (IStructureSystemMemberProfile)

Gets and sets the offset value of the pierce point in the horizontal direction.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetPiercePointHorizontalAxis As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberProfile
Dim value As System.Double

instance.OffsetPiercePointHorizontalAxis = value

value = instance.OffsetPiercePointHorizontalAxis
```

### C#

```csharp
System.double OffsetPiercePointHorizontalAxis {get; set;}
```

### C++/CLI

```cpp
property System.double OffsetPiercePointHorizontalAxis {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Horizontal offset of the pierce point

## VBA Syntax

See [StructureSystemMemberProfile::OffsetPiercePointHorizontalAxis](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberProfile~OffsetPiercePointHorizontalAxis.html).

## Remarks

This property is valid only if [IStructureSystemMemberProfile::OffsetPiercePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~OffsetPiercePoint.html) is set to true.

## See Also

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.html)
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
