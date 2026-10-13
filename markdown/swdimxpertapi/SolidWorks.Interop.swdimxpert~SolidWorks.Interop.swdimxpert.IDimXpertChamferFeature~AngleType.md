---
title: "AngleType Property (IDimXpertChamferFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertChamferFeature"
member: "AngleType"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertChamferFeature~AngleType.html"
---

# AngleType Property (IDimXpertChamferFeature)

Gets the angle type of this DimXpert chamfer.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AngleType As swDimXpertChamferAngleType_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertChamferFeature
Dim value As swDimXpertChamferAngleType_e

value = instance.AngleType
```

### C#

```csharp
swDimXpertChamferAngleType_e AngleType {get;}
```

### C++/CLI

```cpp
property swDimXpertChamferAngleType_e AngleType {
   swDimXpertChamferAngleType_e get();
}
```

### Property Value

Type of angle as defined in [swDimXpertChamferAngleType_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertChamferAngleType_e.html)

## VBA Syntax

See [DimXpertChamferFeature::AngleType](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertChamferFeature~AngleType.html).

## Examples

[Get DimXpert Chamfer Feature Example (VBA)](Get_DimXpert_Chamfer_Feature_Example_VB.htm)
[Get DimXpert Chamfer Feature Example (VB.NET)](Get_DimXpert_Chamfer_Feature_Example_VBNET.htm)

## See Also

[IDimXpertChamferFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertChamferFeature.html)
[IDimXpertChamferFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertChamferFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
