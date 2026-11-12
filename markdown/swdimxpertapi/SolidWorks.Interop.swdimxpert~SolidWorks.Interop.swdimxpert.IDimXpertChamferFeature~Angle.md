---
title: "Angle Property (IDimXpertChamferFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertChamferFeature"
member: "Angle"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertChamferFeature~Angle.html"
---

# Angle Property (IDimXpertChamferFeature)

Gets the angle of this DimXpert chamfer.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertChamferFeature
Dim value As System.Double

value = instance.Angle
```

### C#

```csharp
System.double Angle {get;}
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
}
```

### Property Value

Angle in radians of this chamfer

## VBA Syntax

See [DimXpertChamferFeature::Angle](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertChamferFeature~Angle.html).

## Examples

[Get DimXpert Chamfer Feature Example (VBA)](Get_DimXpert_Chamfer_Feature_Example_VB.htm)
[Get DimXpert Chamfer Feature Example (VB.NET)](Get_DimXpert_Chamfer_Feature_Example_VBNET.htm)

## See Also

[IDimXpertChamferFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertChamferFeature.html)
[IDimXpertChamferFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertChamferFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
