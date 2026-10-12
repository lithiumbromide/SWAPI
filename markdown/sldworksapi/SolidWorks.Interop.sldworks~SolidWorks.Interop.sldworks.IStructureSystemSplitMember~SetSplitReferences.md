---
title: "SetSplitReferences Method (IStructureSystemSplitMember)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemSplitMember"
member: "SetSplitReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~SetSplitReferences.html"
---

# SetSplitReferences Method (IStructureSystemSplitMember)

Sets the split member references.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSplitReferences( _
   ByVal References As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemSplitMember
Dim References As System.Object
Dim value As System.Boolean

value = instance.SetSplitReferences(References)
```

### C#

```csharp
System.bool SetSplitReferences(
   System.object References
)
```

### C++/CLI

```cpp
System.bool SetSplitReferences(
   System.Object^ References
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `References`: Array of split member references, e.g.:

  - Face2
  - IRefPlane
  - Member

### Return Value

True if split member references successfully set, false if not

## VBA Syntax

See [StructureSystemSplitMember::SetSplitReferences](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemSplitMember~SetSplitReferences.html).

## Examples

See the [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.html) examples.

## Remarks

This method is valid only if [IStructureSystemSplitMember::MemberType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~MemberType.html) is set to [swStructureSplitMemberType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStructureSplitMemberType_e.html).swStructureSplitMember_Reference.

## See Also

[IStructureSystemSplitMember Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember.html)
[IStructureSystemSplitMember Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
