---
title: "ReferenceFeature Property (IDimXpertCounterBoreDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCounterBoreDimTol"
member: "ReferenceFeature"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCounterBoreDimTol~ReferenceFeature.html"
---

# ReferenceFeature Property (IDimXpertCounterBoreDimTol)

Gets the reference feature for this DimXpert counterbore dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferenceFeature As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCounterBoreDimTol
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

See [DimXpertCounterBoreDimTol::ReferenceFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCounterBoreDimTol~ReferenceFeature.html).

## Examples

[Get DimXpert Tolerance Example (VBA)](Get_DimXpert_Tolerance_Example_VB.htm)
[Get DimXpert Tolerance Example (VB.NET)](Get_DimXpert_Tolerance_Example_VBNET.htm)

## See Also

[IDimXpertCounterBoreDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCounterBoreDimTol.html)
[IDimXpertCounterBoreDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCounterBoreDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
