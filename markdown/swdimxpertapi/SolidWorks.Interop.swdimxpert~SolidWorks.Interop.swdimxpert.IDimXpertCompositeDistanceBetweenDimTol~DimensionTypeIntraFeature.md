---
title: "DimensionTypeIntraFeature Property (IDimXpertCompositeDistanceBetweenDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositeDistanceBetweenDimTol"
member: "DimensionTypeIntraFeature"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol~DimensionTypeIntraFeature.html"
---

# DimensionTypeIntraFeature Property (IDimXpertCompositeDistanceBetweenDimTol)

Gets the dimension type of the feature-locating portion of this DimXpert composite distance-between dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DimensionTypeIntraFeature As swDimXpertDimensionToleranceType_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompositeDistanceBetweenDimTol
Dim value As swDimXpertDimensionToleranceType_e

value = instance.DimensionTypeIntraFeature
```

### C#

```csharp
swDimXpertDimensionToleranceType_e DimensionTypeIntraFeature {get;}
```

### C++/CLI

```cpp
property swDimXpertDimensionToleranceType_e DimensionTypeIntraFeature {
   swDimXpertDimensionToleranceType_e get();
}
```

### Property Value

Dimension type as defined in [swDimXpertDimensionToleranceType_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertDimensionToleranceType_e.html)

## VBA Syntax

See [DimXpertCompositeDistanceBetweenDimTol::DimensionTypeIntraFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositeDistanceBetweenDimTol~DimensionTypeIntraFeature.html).

## Examples

[Get DimXpert Tolerance2 Example (VBA)](Get_DimXpert_Tolerance2_Example_VB.htm)
[Get DimXpert Tolerance2 Example (VB.NET)](Get_DimXpert_Tolerance2_Example_VBNET.htm)

## See Also

[IDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol.html)
[IDimXpertCompositeDistanceBetweenDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
