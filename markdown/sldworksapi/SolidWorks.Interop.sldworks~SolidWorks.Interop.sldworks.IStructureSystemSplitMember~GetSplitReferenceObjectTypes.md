---
title: "GetSplitReferenceObjectTypes Method (IStructureSystemSplitMember)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemSplitMember"
member: "GetSplitReferenceObjectTypes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~GetSplitReferenceObjectTypes.html"
---

# GetSplitReferenceObjectTypes Method (IStructureSystemSplitMember)

Gets the types of split member references.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplitReferenceObjectTypes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemSplitMember
Dim value As System.Object

value = instance.GetSplitReferenceObjectTypes()
```

### C#

```csharp
System.object GetSplitReferenceObjectTypes()
```

### C++/CLI

```cpp
System.Object^ GetSplitReferenceObjectTypes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of types of split member references as defined by [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html):

- swSelFACES
- swSelDATUMPLANES
- swSelADVSTRUCTMEMBER

## VBA Syntax

See [StructureSystemSplitMember::GetSplitReferenceObjectTypes](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemSplitMember~GetSplitReferenceObjectTypes.html).

## Remarks

This method is valid only if [IStructureSystemSplitMember::MemberType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~MemberType.html) is set to [swStructureSplitMemberType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStructureSplitMemberType_e.html).swStructureSplitMember_Reference.

The array returned by this method maps one-to-one and onto with the array returned by [IStructureSystemSplitMember::GetSplitReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~GetSplitReferences.html).

## See Also

[IStructureSystemSplitMember Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember.html)
[IStructureSystemSplitMember Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
