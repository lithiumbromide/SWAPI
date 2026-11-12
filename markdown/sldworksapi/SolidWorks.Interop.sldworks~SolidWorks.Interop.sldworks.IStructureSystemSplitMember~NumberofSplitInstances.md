---
title: "NumberofSplitInstances Property (IStructureSystemSplitMember)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemSplitMember"
member: "NumberofSplitInstances"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~NumberofSplitInstances.html"
---

# NumberofSplitInstances Property (IStructureSystemSplitMember)

Gets the number of instances in this dimension split member.

## Syntax

### Visual Basic (Declaration)

```vb
Property NumberofSplitInstances As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemSplitMember
Dim value As System.Integer

instance.NumberofSplitInstances = value

value = instance.NumberofSplitInstances
```

### C#

```csharp
System.int NumberofSplitInstances {get; set;}
```

### C++/CLI

```cpp
property System.int NumberofSplitInstances {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of instances

## VBA Syntax

See [StructureSystemSplitMember::NumberofSplitInstances](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemSplitMember~NumberofSplitInstances.html).

## Remarks

This property is valid only for [IStructureSystemSplitMember::DimensionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~DimensionType.html) set to [swSplitMemberDimensionType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSplitMemberDimensionType_e.html).swSplitMemberDimensionType_Instance.

## See Also

[IStructureSystemSplitMember Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember.html)
[IStructureSystemSplitMember Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
