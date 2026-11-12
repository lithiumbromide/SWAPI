---
title: "CornerType Property (ICornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICornerTreatmentFeatureData"
member: "CornerType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData~CornerType.html"
---

# CornerType Property (ICornerTreatmentFeatureData)

Gets the type of this corner treatment.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CornerType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerTreatmentFeatureData
Dim value As System.Integer

value = instance.CornerType
```

### C#

```csharp
System.int CornerType {get;}
```

### C++/CLI

```cpp
property System.int CornerType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of corner treatment as defined by [swCornerType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerType_e.html)

## VBA Syntax

See [CornerTreatmentFeatureData::CornerType](ms-its:sldworksapivb6.chm::/sldworks~CornerTreatmentFeatureData~CornerType.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## See Also

[ICornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData.html)
[ICornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
