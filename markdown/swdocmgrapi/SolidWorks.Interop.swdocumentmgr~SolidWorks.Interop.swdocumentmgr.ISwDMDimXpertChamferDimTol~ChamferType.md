---
title: "ChamferType Property (ISwDMDimXpertChamferDimTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertChamferDimTol"
member: "ChamferType"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferDimTol~ChamferType.html"
---

# ChamferType Property (ISwDMDimXpertChamferDimTol)

Gets the type of chamfer dimension for this DimXpert chamfer dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ChamferType As swDmDimXpertChamferDimensionType_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertChamferDimTol
Dim value As swDmDimXpertChamferDimensionType_e

value = instance.ChamferType
```

### C#

```csharp
swDmDimXpertChamferDimensionType_e ChamferType {get;}
```

### C++/CLI

```cpp
property swDmDimXpertChamferDimensionType_e ChamferType {
   swDmDimXpertChamferDimensionType_e get();
}
```

### Property Value

Type of chamfer dimension as defined in [swDmDimXpertChamferDimensionType_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertChamferDimensionType_e.html)

## VBA Syntax

See [SwDMDimXpertChamferDimTol::ChamferType](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertChamferDimTol~ChamferType.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertChamferDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferDimTol.html)
[ISwDMDimXpertChamferDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
