---
title: "IsSplit Property (IStructureSystemMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberFeatureData"
member: "IsSplit"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~IsSplit.html"
---

# IsSplit Property (IStructureSystemMemberFeatureData)

Gets and sets whether this structure system member is split.

## Syntax

### Visual Basic (Declaration)

```vb
Property IsSplit As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberFeatureData
Dim value As System.Boolean

instance.IsSplit = value

value = instance.IsSplit
```

### C#

```csharp
System.bool IsSplit {get; set;}
```

### C++/CLI

```cpp
property System.bool IsSplit {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this structure system member is split, false if not

## VBA Syntax

See [StructureSystemMemberFeatureData::IsSplit](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberFeatureData~IsSplit.html).

## Examples

See the [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.html) examples.

## Remarks

If this property is true, then use [IStructureSystemMemberFeatureData::GetSplitMember](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~GetSplitMember.html) to access the split member.

## See Also

[IStructureSystemMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.html)
[IStructureSystemMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
