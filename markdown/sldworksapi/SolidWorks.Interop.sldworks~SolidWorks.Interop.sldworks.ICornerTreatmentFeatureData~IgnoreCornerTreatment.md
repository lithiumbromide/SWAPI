---
title: "IgnoreCornerTreatment Property (ICornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICornerTreatmentFeatureData"
member: "IgnoreCornerTreatment"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData~IgnoreCornerTreatment.html"
---

# IgnoreCornerTreatment Property (ICornerTreatmentFeatureData)

Gets and sets whether to ignore this corner treatment.

## Syntax

### Visual Basic (Declaration)

```vb
Property IgnoreCornerTreatment As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerTreatmentFeatureData
Dim value As System.Boolean

instance.IgnoreCornerTreatment = value

value = instance.IgnoreCornerTreatment
```

### C#

```csharp
System.bool IgnoreCornerTreatment {get; set;}
```

### C++/CLI

```cpp
property System.bool IgnoreCornerTreatment {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to ignore the corner treatment, false to not

## VBA Syntax

See [CornerTreatmentFeatureData::IgnoreCornerTreatment](ms-its:sldworksapivb6.chm::/sldworks~CornerTreatmentFeatureData~IgnoreCornerTreatment.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## See Also

[ICornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData.html)
[ICornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
