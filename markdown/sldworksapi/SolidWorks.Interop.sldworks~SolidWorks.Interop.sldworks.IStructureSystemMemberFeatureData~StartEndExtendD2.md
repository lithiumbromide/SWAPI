---
title: "StartEndExtendD2 Property (IStructureSystemMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberFeatureData"
member: "StartEndExtendD2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~StartEndExtendD2.html"
---

# StartEndExtendD2 Property (IStructureSystemMemberFeatureData)

Gets and sets the distance in Direction 2 to extend this structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Property StartEndExtendD2 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberFeatureData
Dim value As System.Double

instance.StartEndExtendD2 = value

value = instance.StartEndExtendD2
```

### C#

```csharp
System.double StartEndExtendD2 {get; set;}
```

### C++/CLI

```cpp
property System.double StartEndExtendD2 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Extend distance in Direction 2

## VBA Syntax

See [StructureSystemMemberFeatureData::StartEndExtendD2](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberFeatureData~StartEndExtendD2.html).

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
