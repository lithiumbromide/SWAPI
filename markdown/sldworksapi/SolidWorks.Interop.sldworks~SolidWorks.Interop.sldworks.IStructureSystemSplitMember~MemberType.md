---
title: "MemberType Property (IStructureSystemSplitMember)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemSplitMember"
member: "MemberType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~MemberType.html"
---

# MemberType Property (IStructureSystemSplitMember)

Gets the type of split for this structure system split member.

## Syntax

### Visual Basic (Declaration)

```vb
Property MemberType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemSplitMember
Dim value As System.Integer

instance.MemberType = value

value = instance.MemberType
```

### C#

```csharp
System.int MemberType {get; set;}
```

### C++/CLI

```cpp
property System.int MemberType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of split as defined by [swStructureSplitMemberType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStructureSplitMemberType_e.html)

## VBA Syntax

See [StructureSystemSplitMember::MemberType](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemSplitMember~MemberType.html).

## Examples

See the [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.html) examples.

## See Also

[IStructureSystemSplitMember Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember.html)
[IStructureSystemSplitMember Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
