---
title: "ChamferType Property (IDimXpertChamferDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertChamferDimTol"
member: "ChamferType"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertChamferDimTol~ChamferType.html"
---

# ChamferType Property (IDimXpertChamferDimTol)

Gets the type of this DimXpert chamfer dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ChamferType As swDimXpertChamferDimensionType_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertChamferDimTol
Dim value As swDimXpertChamferDimensionType_e

value = instance.ChamferType
```

### C#

```csharp
swDimXpertChamferDimensionType_e ChamferType {get;}
```

### C++/CLI

```cpp
property swDimXpertChamferDimensionType_e ChamferType {
   swDimXpertChamferDimensionType_e get();
}
```

### Property Value

Type of chamfer as defined in [swDimXpertChamferDimensionType_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertChamferDimensionType_e.html)

## VBA Syntax

See [DimXpertChamferDimTol::ChamferType](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertChamferDimTol~ChamferType.html).

## Examples

[Get DimXpert Tolerance4 Example (VBA)](Get_DimXpert_Tolerance4_Example_VB.htm)
[Get DimXpert Tolerance4 Example (VB.NET)](Get_DimXpert_Tolerance4_Example_VBNET.htm)

## See Also

[IDimXpertChamferDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertChamferDimTol.html)
[IDimXpertChamferDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertChamferDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
