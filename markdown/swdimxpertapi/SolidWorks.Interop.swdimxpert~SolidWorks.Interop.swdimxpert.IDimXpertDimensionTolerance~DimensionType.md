---
title: "DimensionType Property (IDimXpertDimensionTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertDimensionTolerance"
member: "DimensionType"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionTolerance~DimensionType.html"
---

# DimensionType Property (IDimXpertDimensionTolerance)

Gets the type of this DimXpert dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DimensionType As swDimXpertDimensionToleranceType_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertDimensionTolerance
Dim value As swDimXpertDimensionToleranceType_e

value = instance.DimensionType
```

### C#

```csharp
swDimXpertDimensionToleranceType_e DimensionType {get;}
```

### C++/CLI

```cpp
property swDimXpertDimensionToleranceType_e DimensionType {
   swDimXpertDimensionToleranceType_e get();
}
```

### Property Value

Type of this DimXpert dimension tolerance as defined in [swDimXpertDimensionToleranceType_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertDimensionToleranceType_e.html)

## VBA Syntax

See [DimXpertDimensionTolerance::DimensionType](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertDimensionTolerance~DimensionType.html).

## Examples

[Get DimXpert Tolerance Example (VBA)](Get_DimXpert_Tolerance_Example_VB.htm)
[Get DimXpert Tolerance Example (VB.NET)](Get_DimXpert_Tolerance_Example_VBNET.htm)

## See Also

[IDimXpertDimensionTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionTolerance.html)
[IDimXpertDimensionTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
