---
title: "MemberProfile Property (IStructureSystemMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberFeatureData"
member: "MemberProfile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~MemberProfile.html"
---

# MemberProfile Property (IStructureSystemMemberFeatureData)

Gets the profile of this structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MemberProfile As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberFeatureData
Dim value As System.Object

value = instance.MemberProfile
```

### C#

```csharp
System.object MemberProfile {get;}
```

### C++/CLI

```cpp
property System.Object^ MemberProfile {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IStructureSystemMemberProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.html)

## VBA Syntax

See [StructureSystemMemberFeatureData::MemberProfile](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberFeatureData~MemberProfile.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

See the [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.html) examples.

See the [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html) examples.

See the [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.html) examples.

See the [IPrimaryMemberRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.html) examples.

## See Also

[IStructureSystemMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.html)
[IStructureSystemMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
