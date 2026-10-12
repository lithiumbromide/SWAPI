---
title: "MergeTangentMembers Property (IPrimaryMemberFacePlaneIntersectionFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberFacePlaneIntersectionFeatureData"
member: "MergeTangentMembers"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData~MergeTangentMembers.html"
---

# MergeTangentMembers Property (IPrimaryMemberFacePlaneIntersectionFeatureData)

Gets and sets whether to merge tangent structure system members.

## Syntax

### Visual Basic (Declaration)

```vb
Property MergeTangentMembers As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberFacePlaneIntersectionFeatureData
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

True to merge tangent members, false to not

## VBA Syntax

See [PrimaryMemberFacePlaneIntersectionFeatureData::MergeTangentMembers](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberFacePlaneIntersectionFeatureData~MergeTangentMembers.html).

## Examples

See the [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.html) examples.

## See Also

[IPrimaryMemberFacePlaneIntersectionFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.html)
[IPrimaryMemberFacePlaneIntersectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
