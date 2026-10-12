---
title: "CornerTreatmentTrimType Property (ISimpleCornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimpleCornerTreatmentFeatureData"
member: "CornerTreatmentTrimType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData~CornerTreatmentTrimType.html"
---

# CornerTreatmentTrimType Property (ISimpleCornerTreatmentFeatureData)

Gets and sets the corner treatment trim type for this simple corner treatment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CornerTreatmentTrimType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleCornerTreatmentFeatureData
Dim value As System.Integer

instance.CornerTreatmentTrimType = value

value = instance.CornerTreatmentTrimType
```

### C#

```csharp
System.int CornerTreatmentTrimType {get; set;}
```

### C++/CLI

```cpp
property System.int CornerTreatmentTrimType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Corner treatment trim type as defined by [swCornerTreatmentTrimType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentTrimType_e.html)

## VBA Syntax

See [SimpleCornerTreatmentFeatureData::CornerTreatmentTrimType](ms-its:sldworksapivb6.chm::/sldworks~SimpleCornerTreatmentFeatureData~CornerTreatmentTrimType.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## Remarks

This property is valid only for swCornerTreatmentTrimType_e.:

- swCornerTreatmentTrim_BodyTrim
- swCornerTreatmentTrim_PlanarTrim

## See Also

[ISimpleCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData.html)
[ISimpleCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
