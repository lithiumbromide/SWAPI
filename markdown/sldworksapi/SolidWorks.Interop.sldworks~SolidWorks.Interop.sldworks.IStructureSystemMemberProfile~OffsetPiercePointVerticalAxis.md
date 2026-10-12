---
title: "OffsetPiercePointVerticalAxis Property (IStructureSystemMemberProfile)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberProfile"
member: "OffsetPiercePointVerticalAxis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~OffsetPiercePointVerticalAxis.html"
---

# OffsetPiercePointVerticalAxis Property (IStructureSystemMemberProfile)

Gets and sets the offset value of the pierce point in the vertical direction.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetPiercePointVerticalAxis As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberProfile
Dim value As System.Double

instance.OffsetPiercePointVerticalAxis = value

value = instance.OffsetPiercePointVerticalAxis
```

### C#

```csharp
System.double OffsetPiercePointVerticalAxis {get; set;}
```

### C++/CLI

```cpp
property System.double OffsetPiercePointVerticalAxis {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Vertical offset of the pierce point

## VBA Syntax

See [StructureSystemMemberProfile::OffsetPiercePointVerticalAxis](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberProfile~OffsetPiercePointVerticalAxis.html).

## Remarks

This property is valid only if [IStructureSystemMemberProfile::OffsetPiercePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~OffsetPiercePoint.html) is set to true.

## See Also

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.html)
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
