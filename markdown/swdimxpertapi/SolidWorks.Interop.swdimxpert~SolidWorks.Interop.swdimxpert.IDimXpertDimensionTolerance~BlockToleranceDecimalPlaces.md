---
title: "BlockToleranceDecimalPlaces Property (IDimXpertDimensionTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertDimensionTolerance"
member: "BlockToleranceDecimalPlaces"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionTolerance~BlockToleranceDecimalPlaces.html"
---

# BlockToleranceDecimalPlaces Property (IDimXpertDimensionTolerance)

Gets the precision of the block tolerance of this DimXpert dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BlockToleranceDecimalPlaces As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertDimensionTolerance
Dim value As System.Integer

value = instance.BlockToleranceDecimalPlaces
```

### C#

```csharp
System.int BlockToleranceDecimalPlaces {get;}
```

### C++/CLI

```cpp
property System.int BlockToleranceDecimalPlaces {
   System.int get();
}
```

### Property Value

Number of decimal places.

## VBA Syntax

See [DimXpertDimensionTolerance::BlockToleranceDecimalPlaces](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertDimensionTolerance~BlockToleranceDecimalPlaces.html).

## Examples

[Get DimXpert Tolerance Example (VBA)](Get_DimXpert_Tolerance_Example_VB.htm)
[Get DimXpert Tolerance Example (VB.NET)](Get_DimXpert_Tolerance_Example_VBNET.htm)

## See Also

[IDimXpertDimensionTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionTolerance.html)
[IDimXpertDimensionTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
