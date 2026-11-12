---
title: "GetSplitReferences Method (IStructureSystemSplitMember)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemSplitMember"
member: "GetSplitReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~GetSplitReferences.html"
---

# GetSplitReferences Method (IStructureSystemSplitMember)

Gets the entities used to split this structure system split member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplitReferences() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemSplitMember
Dim value As System.Object

value = instance.GetSplitReferences()
```

### C#

```csharp
System.object GetSplitReferences()
```

### C++/CLI

```cpp
System.Object^ GetSplitReferences();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of one or more references, e.g.:

- [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
- [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)
- [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html) (i.e., another structure system member)

## VBA Syntax

See [StructureSystemSplitMember::GetSplitReferences](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemSplitMember~GetSplitReferences.html).

## Remarks

This method is valid only if [IStructureSystemSplitMember::MemberType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~MemberType.html) is set to [swStructureSplitMemberType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStructureSplitMemberType_e.html).swStructureSplitMember_Reference.

## See Also

[IStructureSystemSplitMember Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember.html)
[IStructureSystemSplitMember Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
