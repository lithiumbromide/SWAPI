---
title: "SplitLength Property (IStructureSystemSplitMember)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemSplitMember"
member: "SplitLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~SplitLength.html"
---

# SplitLength Property (IStructureSystemSplitMember)

Gets the length of this dimension split member.

## Syntax

### Visual Basic (Declaration)

```vb
Property SplitLength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemSplitMember
Dim value As System.Double

instance.SplitLength = value

value = instance.SplitLength
```

### C#

```csharp
System.double SplitLength {get; set;}
```

### C++/CLI

```cpp
property System.double SplitLength {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Length

## VBA Syntax

See [StructureSystemSplitMember::SplitLength](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemSplitMember~SplitLength.html).

## Remarks

This property is valid only for [IStructureSystemSplitMember::DimensionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~DimensionType.html) set to [swSplitMemberDimensionType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSplitMemberDimensionType_e.html).swSplitMemberDimensionType_SplitLength.

## See Also

[IStructureSystemSplitMember Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember.html)
[IStructureSystemSplitMember Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
