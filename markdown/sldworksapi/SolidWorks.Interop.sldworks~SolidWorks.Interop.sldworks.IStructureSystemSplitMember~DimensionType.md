---
title: "DimensionType Property (IStructureSystemSplitMember)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemSplitMember"
member: "DimensionType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~DimensionType.html"
---

# DimensionType Property (IStructureSystemSplitMember)

Gets the type of dimension split for this structure system split member.

## Syntax

### Visual Basic (Declaration)

```vb
Property DimensionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemSplitMember
Dim value As System.Integer

instance.DimensionType = value

value = instance.DimensionType
```

### C#

```csharp
System.int DimensionType {get; set;}
```

### C++/CLI

```cpp
property System.int DimensionType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of dimension split member as defined by [swSplitMemberDimensionType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSplitMemberDimensionType_e.html)

## VBA Syntax

See [StructureSystemSplitMember::DimensionType](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemSplitMember~DimensionType.html).

## See Also

[IStructureSystemSplitMember Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember.html)
[IStructureSystemSplitMember Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
