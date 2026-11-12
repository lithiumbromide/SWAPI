---
title: "WeldTrimGap Property (ISimpleCornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimpleCornerTreatmentFeatureData"
member: "WeldTrimGap"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData~WeldTrimGap.html"
---

# WeldTrimGap Property (ISimpleCornerTreatmentFeatureData)

Gets and sets the weld trim gap of this simple corner treatment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property WeldTrimGap As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleCornerTreatmentFeatureData
Dim value As System.Double

instance.WeldTrimGap = value

value = instance.WeldTrimGap
```

### C#

```csharp
System.double WeldTrimGap {get; set;}
```

### C++/CLI

```cpp
property System.double WeldTrimGap {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Weld trim gap between members

## VBA Syntax

See [SimpleCornerTreatmentFeatureData::WeldTrimGap](ms-its:sldworksapivb6.chm::/sldworks~SimpleCornerTreatmentFeatureData~WeldTrimGap.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## See Also

[ISimpleCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData.html)
[ISimpleCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
