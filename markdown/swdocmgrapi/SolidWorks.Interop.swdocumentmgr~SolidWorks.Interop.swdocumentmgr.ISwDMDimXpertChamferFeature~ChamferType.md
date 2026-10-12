---
title: "ChamferType Property (ISwDMDimXpertChamferFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertChamferFeature"
member: "ChamferType"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature~ChamferType.html"
---

# ChamferType Property (ISwDMDimXpertChamferFeature)

Gets the type of this DimXpert chamfer.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ChamferType As swDmDimXpertChamferType_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertChamferFeature
Dim value As swDmDimXpertChamferType_e

value = instance.ChamferType
```

### C#

```csharp
swDmDimXpertChamferType_e ChamferType {get;}
```

### C++/CLI

```cpp
property swDmDimXpertChamferType_e ChamferType {
   swDmDimXpertChamferType_e get();
}
```

### Property Value

Type of chamfer as defined in [swDmDimXpertChamferType_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertChamferType_e.html)

## VBA Syntax

See [SwDMDimXpertChamferFeature::ChamferType](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertChamferFeature~ChamferType.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertChamferFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature.html)
[ISwDMDimXpertChamferFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
