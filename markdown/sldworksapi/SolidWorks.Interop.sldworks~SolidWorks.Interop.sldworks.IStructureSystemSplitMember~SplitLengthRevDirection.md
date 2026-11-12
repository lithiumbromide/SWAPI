---
title: "SplitLengthRevDirection Property (IStructureSystemSplitMember)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemSplitMember"
member: "SplitLengthRevDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~SplitLengthRevDirection.html"
---

# SplitLengthRevDirection Property (IStructureSystemSplitMember)

Gets and sets whether to reverse the direction of the length of this dimension split member.

## Syntax

### Visual Basic (Declaration)

```vb
Property SplitLengthRevDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemSplitMember
Dim value As System.Boolean

instance.SplitLengthRevDirection = value

value = instance.SplitLengthRevDirection
```

### C#

```csharp
System.bool SplitLengthRevDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool SplitLengthRevDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction of the length, false to not

## VBA Syntax

See [StructureSystemSplitMember::SplitLengthRevDirection](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemSplitMember~SplitLengthRevDirection.html).

## Remarks

This property is valid only for [IStructureSystemSplitMember::DimensionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~DimensionType.html) set to [swSplitMemberDimensionType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSplitMemberDimensionType_e.html).swSplitMemberDimensionType_SplitLength.

## See Also

[IStructureSystemSplitMember Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember.html)
[IStructureSystemSplitMember Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
