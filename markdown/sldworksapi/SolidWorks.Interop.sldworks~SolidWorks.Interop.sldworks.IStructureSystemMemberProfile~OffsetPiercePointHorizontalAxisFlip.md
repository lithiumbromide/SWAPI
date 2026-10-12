---
title: "OffsetPiercePointHorizontalAxisFlip Property (IStructureSystemMemberProfile)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberProfile"
member: "OffsetPiercePointHorizontalAxisFlip"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~OffsetPiercePointHorizontalAxisFlip.html"
---

# OffsetPiercePointHorizontalAxisFlip Property (IStructureSystemMemberProfile)

Gets and sets whether to reverse the offset value of the pierce point in the horizontal direction.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetPiercePointHorizontalAxisFlip As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberProfile
Dim value As System.Boolean

instance.OffsetPiercePointHorizontalAxisFlip = value

value = instance.OffsetPiercePointHorizontalAxisFlip
```

### C#

```csharp
System.bool OffsetPiercePointHorizontalAxisFlip {get; set;}
```

### C++/CLI

```cpp
property System.bool OffsetPiercePointHorizontalAxisFlip {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the horizontal offset, false to not

## VBA Syntax

See [StructureSystemMemberProfile::OffsetPiercePointHorizontalAxisFlip](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberProfile~OffsetPiercePointHorizontalAxisFlip.html).

## Remarks

This property is valid only if [IStructureSystemMemberProfile::OffsetPiercePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~OffsetPiercePoint.html) is set to true.

## See Also

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.html)
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
