---
title: "OffsetPiercePointVerticalAxisFlip Property (IStructureSystemMemberProfile)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberProfile"
member: "OffsetPiercePointVerticalAxisFlip"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~OffsetPiercePointVerticalAxisFlip.html"
---

# OffsetPiercePointVerticalAxisFlip Property (IStructureSystemMemberProfile)

Gets and sets whether to reverse the offset value of the pierce point in the vertical direction.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetPiercePointVerticalAxisFlip As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberProfile
Dim value As System.Boolean

instance.OffsetPiercePointVerticalAxisFlip = value

value = instance.OffsetPiercePointVerticalAxisFlip
```

### C#

```csharp
System.bool OffsetPiercePointVerticalAxisFlip {get; set;}
```

### C++/CLI

```cpp
property System.bool OffsetPiercePointVerticalAxisFlip {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the vertical offset, false to not

## VBA Syntax

See [StructureSystemMemberProfile::OffsetPiercePointVerticalAxisFlip](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberProfile~OffsetPiercePointVerticalAxisFlip.html).

## See Also

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.html)
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
