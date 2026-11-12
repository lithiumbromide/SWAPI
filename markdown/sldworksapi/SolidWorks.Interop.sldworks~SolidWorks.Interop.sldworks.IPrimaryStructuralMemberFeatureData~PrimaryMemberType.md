---
title: "PrimaryMemberType Property (IPrimaryStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryStructuralMemberFeatureData"
member: "PrimaryMemberType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryStructuralMemberFeatureData~PrimaryMemberType.html"
---

# PrimaryMemberType Property (IPrimaryStructuralMemberFeatureData)

Gets the type of this primary structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PrimaryMemberType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryStructuralMemberFeatureData
Dim value As System.Integer

value = instance.PrimaryMemberType
```

### C#

```csharp
System.int PrimaryMemberType {get;}
```

### C++/CLI

```cpp
property System.int PrimaryMemberType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Primary structure system member type as defined by [swStructureSystemMemberCreationType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStructureSystemMemberCreationType_e.html)

## VBA Syntax

See [PrimaryStructuralMemberFeatureData::PrimaryMemberType](ms-its:sldworksapivb6.chm::/sldworks~PrimaryStructuralMemberFeatureData~PrimaryMemberType.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

See the [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.html) examples.

See the [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html) examples.

## See Also

[IPrimaryStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryStructuralMemberFeatureData.html)
[IPrimaryStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryStructuralMemberFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
