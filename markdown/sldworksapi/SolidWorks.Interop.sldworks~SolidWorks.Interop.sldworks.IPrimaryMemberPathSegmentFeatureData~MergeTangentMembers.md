---
title: "MergeTangentMembers Property (IPrimaryMemberPathSegmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberPathSegmentFeatureData"
member: "MergeTangentMembers"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData~MergeTangentMembers.html"
---

# MergeTangentMembers Property (IPrimaryMemberPathSegmentFeatureData)

Gets and sets whether to merge tangential members.

## Syntax

### Visual Basic (Declaration)

```vb
Property MergeTangentMembers As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberPathSegmentFeatureData
Dim value As System.Boolean

instance.MergeTangentMembers = value

value = instance.MergeTangentMembers
```

### C#

```csharp
System.bool MergeTangentMembers {get; set;}
```

### C++/CLI

```cpp
property System.bool MergeTangentMembers {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to merge tangential members, false to not

## VBA Syntax

See [PrimaryMemberPathSegmentFeatureData::MergeTangentMembers](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberPathSegmentFeatureData~MergeTangentMembers.html).

## Examples

See the [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.html) examples.

## Remarks

This property is valid only when creating the structure system path segment member.

## See Also

[IPrimaryMemberPathSegmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.html)
[IPrimaryMemberPathSegmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
