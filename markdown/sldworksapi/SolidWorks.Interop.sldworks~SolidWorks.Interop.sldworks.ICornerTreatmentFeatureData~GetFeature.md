---
title: "GetFeature Method (ICornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICornerTreatmentFeatureData"
member: "GetFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData~GetFeature.html"
---

# GetFeature Method (ICornerTreatmentFeatureData)

Gets the feature for this corner treatment.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeature() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerTreatmentFeatureData
Dim value As Feature

value = instance.GetFeature()
```

### C#

```csharp
Feature GetFeature()
```

### C++/CLI

```cpp
Feature^ GetFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [CornerTreatmentFeatureData::GetFeature](ms-its:sldworksapivb6.chm::/sldworks~CornerTreatmentFeatureData~GetFeature.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## See Also

[ICornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData.html)
[ICornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
