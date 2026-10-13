---
title: "GetPlanarTrimMembers Method (IComplexCornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IComplexCornerTreatmentFeatureData"
member: "GetPlanarTrimMembers"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~GetPlanarTrimMembers.html"
---

# GetPlanarTrimMembers Method (IComplexCornerTreatmentFeatureData)

Gets the planar trim member of this complex corner treatment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlanarTrimMembers() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComplexCornerTreatmentFeatureData
Dim value As System.Object

value = instance.GetPlanarTrimMembers()
```

### C#

```csharp
System.object GetPlanarTrimMembers()
```

### C++/CLI

```cpp
System.Object^ GetPlanarTrimMembers();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of planar trim [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.html)s

## VBA Syntax

See [ComplexCornerTreatmentFeatureData::GetPlanarTrimMembers](ms-its:sldworksapivb6.chm::/sldworks~ComplexCornerTreatmentFeatureData~GetPlanarTrimMembers.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## See Also

[IComplexCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData.html)
[IComplexCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
