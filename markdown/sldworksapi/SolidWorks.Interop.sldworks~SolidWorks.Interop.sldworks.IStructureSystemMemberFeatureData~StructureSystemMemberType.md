---
title: "StructureSystemMemberType Property (IStructureSystemMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberFeatureData"
member: "StructureSystemMemberType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~StructureSystemMemberType.html"
---

# StructureSystemMemberType Property (IStructureSystemMemberFeatureData)

Gets the type of this structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property StructureSystemMemberType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberFeatureData
Dim value As System.Integer

value = instance.StructureSystemMemberType
```

### C#

```csharp
System.int StructureSystemMemberType {get;}
```

### C++/CLI

```cpp
property System.int StructureSystemMemberType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of structure system member as defined by [swStructureSystemMemberType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStructureSystemMemberType_e.html)

## VBA Syntax

See [StructureSystemMemberFeatureData::StructureSystemMemberType](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberFeatureData~StructureSystemMemberType.html).

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
