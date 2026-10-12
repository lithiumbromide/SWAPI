---
title: "ZoneType Property (IDimXpertOrientationTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertOrientationTolerance"
member: "ZoneType"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertOrientationTolerance~ZoneType.html"
---

# ZoneType Property (IDimXpertOrientationTolerance)

Gets the zone type of this DimXpert orientation tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ZoneType As swDimXpertOrientationZoneType_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertOrientationTolerance
Dim value As swDimXpertOrientationZoneType_e

value = instance.ZoneType
```

### C#

```csharp
swDimXpertOrientationZoneType_e ZoneType {get;}
```

### C++/CLI

```cpp
property swDimXpertOrientationZoneType_e ZoneType {
   swDimXpertOrientationZoneType_e get();
}
```

### Property Value

Orientation zone type as defined in [swDimXpertOrientationZoneType_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertOrientationZoneType_e.html)

## VBA Syntax

See [DimXpertOrientationTolerance::ZoneType](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertOrientationTolerance~ZoneType.html).

## Examples

[Get DimXpert Tolerance3 Example (VBA)](Get_DimXpert_Tolerance3_Example_VB.htm)
[Get DimXpert Tolerance3 Example (VB.NET)](Get_DimXpert_Tolerance3_Example_VBNET.htm)

## See Also

[IDimXpertOrientationTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertOrientationTolerance.html)
[IDimXpertOrientationTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertOrientationTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
