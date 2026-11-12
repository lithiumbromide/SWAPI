---
title: "ReferenceFeature Property (IDimXpertCounterSinkDiameterDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCounterSinkDiameterDimTol"
member: "ReferenceFeature"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCounterSinkDiameterDimTol~ReferenceFeature.html"
---

# ReferenceFeature Property (IDimXpertCounterSinkDiameterDimTol)

Gets the reference feature for this DimXpert countersink diameter dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferenceFeature As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCounterSinkDiameterDimTol
Dim value As DimXpertFeature

value = instance.ReferenceFeature
```

### C#

```csharp
DimXpertFeature ReferenceFeature {get;}
```

### C++/CLI

```cpp
property DimXpertFeature^ ReferenceFeature {
   DimXpertFeature^ get();
}
```

### Property Value

[IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)

## VBA Syntax

See [DimXpertCounterSinkDiameterDimTol::ReferenceFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCounterSinkDiameterDimTol~ReferenceFeature.html).

## Examples

[Get DimXpert Tolerance Example (VBA)](Get_DimXpert_Tolerance_Example_VB.htm)
[Get DimXpert Tolerance Example (VB.NET)](Get_DimXpert_Tolerance_Example_VBNET.htm)

## See Also

[IDimXpertCounterSinkDiameterDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCounterSinkDiameterDimTol.html)
[IDimXpertCounterSinkDiameterDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCounterSinkDiameterDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
