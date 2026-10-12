---
title: "ChamferType Property (IDimXpertChamferFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertChamferFeature"
member: "ChamferType"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertChamferFeature~ChamferType.html"
---

# ChamferType Property (IDimXpertChamferFeature)

Gets the type of this DimXpert chamfer.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ChamferType As swDimXpertChamferType_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertChamferFeature
Dim value As swDimXpertChamferType_e

value = instance.ChamferType
```

### C#

```csharp
swDimXpertChamferType_e ChamferType {get;}
```

### C++/CLI

```cpp
property swDimXpertChamferType_e ChamferType {
   swDimXpertChamferType_e get();
}
```

### Property Value

Type of chamfer as defined in [swDimXpertChamferType_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertChamferType_e.html)

## VBA Syntax

See [DimXpertChamferFeature::ChamferType](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertChamferFeature~ChamferType.html).

## Examples

[Get DimXpert Chamfer Feature Example (VBA)](Get_DimXpert_Chamfer_Feature_Example_VB.htm)
[Get DimXpert Chamfer Feature Example (VB.NET)](Get_DimXpert_Chamfer_Feature_Example_VBNET.htm)

## See Also

[IDimXpertChamferFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertChamferFeature.html)
[IDimXpertChamferFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertChamferFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
