---
title: "ReferenceFeature Property (IDimXpertCounterSinkAngleDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCounterSinkAngleDimTol"
member: "ReferenceFeature"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCounterSinkAngleDimTol~ReferenceFeature.html"
---

# ReferenceFeature Property (IDimXpertCounterSinkAngleDimTol)

Gets the reference feature for this DimXpert countersink angle dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferenceFeature As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCounterSinkAngleDimTol
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

See [DimXpertCounterSinkAngleDimTol::ReferenceFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCounterSinkAngleDimTol~ReferenceFeature.html).

## Examples

[Get DimXpert Tolerance Example (VBA)](Get_DimXpert_Tolerance_Example_VB.htm)
[Get DimXpert Tolerance Example (VB.NET)](Get_DimXpert_Tolerance_Example_VBNET.htm)

## See Also

[IDimXpertCounterSinkAngleDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCounterSinkAngleDimTol.html)
[IDimXpertCounterSinkAngleDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCounterSinkAngleDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
