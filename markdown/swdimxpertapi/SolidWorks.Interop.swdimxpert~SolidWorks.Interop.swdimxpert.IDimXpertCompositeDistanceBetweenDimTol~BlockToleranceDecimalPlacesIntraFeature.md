---
title: "BlockToleranceDecimalPlacesIntraFeature Property (IDimXpertCompositeDistanceBetweenDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositeDistanceBetweenDimTol"
member: "BlockToleranceDecimalPlacesIntraFeature"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol~BlockToleranceDecimalPlacesIntraFeature.html"
---

# BlockToleranceDecimalPlacesIntraFeature Property (IDimXpertCompositeDistanceBetweenDimTol)

Gets the precision of block tolerances for the feature-locating portion of this DimXpert composite distance-between dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BlockToleranceDecimalPlacesIntraFeature As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompositeDistanceBetweenDimTol
Dim value As System.Integer

value = instance.BlockToleranceDecimalPlacesIntraFeature
```

### C#

```csharp
System.int BlockToleranceDecimalPlacesIntraFeature {get;}
```

### C++/CLI

```cpp
property System.int BlockToleranceDecimalPlacesIntraFeature {
   System.int get();
}
```

### Property Value

Number of decimal places

## VBA Syntax

See [DimXpertCompositeDistanceBetweenDimTol::BlockToleranceDecimalPlacesIntraFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositeDistanceBetweenDimTol~BlockToleranceDecimalPlacesIntraFeature.html).

## Examples

[Get DimXpert Tolerance2 Example (VBA)](Get_DimXpert_Tolerance2_Example_VB.htm)
[Get DimXpert Tolerance2 Example (VB.NET)](Get_DimXpert_Tolerance2_Example_VBNET.htm)

## See Also

[IDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol.html)
[IDimXpertCompositeDistanceBetweenDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
