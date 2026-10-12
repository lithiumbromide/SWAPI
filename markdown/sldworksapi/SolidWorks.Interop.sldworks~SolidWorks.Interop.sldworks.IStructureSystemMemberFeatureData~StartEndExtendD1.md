---
title: "StartEndExtendD1 Property (IStructureSystemMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberFeatureData"
member: "StartEndExtendD1"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~StartEndExtendD1.html"
---

# StartEndExtendD1 Property (IStructureSystemMemberFeatureData)

Gets and sets the distance in Direction 1 to extend this structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Property StartEndExtendD1 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberFeatureData
Dim value As System.Double

instance.StartEndExtendD1 = value

value = instance.StartEndExtendD1
```

### C#

```csharp
System.double StartEndExtendD1 {get; set;}
```

### C++/CLI

```cpp
property System.double StartEndExtendD1 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Extend distance in Direction 1

## VBA Syntax

See [StructureSystemMemberFeatureData::StartEndExtendD1](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberFeatureData~StartEndExtendD1.html).

## Examples

See the [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.html) examples.

See the [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html) examples.

See the [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.html) examples.

See the [IPrimaryMemberRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.html) examples.

## See Also

[IStructureSystemMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.html)
[IStructureSystemMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
