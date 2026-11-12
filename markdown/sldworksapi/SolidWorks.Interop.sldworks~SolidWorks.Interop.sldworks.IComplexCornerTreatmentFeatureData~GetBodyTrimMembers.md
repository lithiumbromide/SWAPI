---
title: "GetBodyTrimMembers Method (IComplexCornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IComplexCornerTreatmentFeatureData"
member: "GetBodyTrimMembers"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~GetBodyTrimMembers.html"
---

# GetBodyTrimMembers Method (IComplexCornerTreatmentFeatureData)

Gets the body trim members of this complex corner treatment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodyTrimMembers() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComplexCornerTreatmentFeatureData
Dim value As System.Object

value = instance.GetBodyTrimMembers()
```

### C#

```csharp
System.object GetBodyTrimMembers()
```

### C++/CLI

```cpp
System.Object^ GetBodyTrimMembers();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of body trim [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.html)s

## VBA Syntax

See [ComplexCornerTreatmentFeatureData::GetBodyTrimMembers](ms-its:sldworksapivb6.chm::/sldworks~ComplexCornerTreatmentFeatureData~GetBodyTrimMembers.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## See Also

[IComplexCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData.html)
[IComplexCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
