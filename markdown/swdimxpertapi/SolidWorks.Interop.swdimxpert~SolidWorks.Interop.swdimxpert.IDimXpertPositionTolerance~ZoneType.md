---
title: "ZoneType Property (IDimXpertPositionTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPositionTolerance"
member: "ZoneType"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPositionTolerance~ZoneType.html"
---

# ZoneType Property (IDimXpertPositionTolerance)

Gets the zone type of this DimXpert position tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ZoneType As swDimXpertPositionZoneType_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPositionTolerance
Dim value As swDimXpertPositionZoneType_e

value = instance.ZoneType
```

### C#

```csharp
swDimXpertPositionZoneType_e ZoneType {get;}
```

### C++/CLI

```cpp
property swDimXpertPositionZoneType_e ZoneType {
   swDimXpertPositionZoneType_e get();
}
```

### Property Value

Position zone type as defined in [swDimXpertPositionZoneType_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertPositionZoneType_e.html)

## VBA Syntax

See [DimXpertPositionTolerance::ZoneType](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPositionTolerance~ZoneType.html).

## Examples

[Get DimXpert Tolerance3 Example (VBA)](Get_DimXpert_Tolerance3_Example_VB.htm)
[Get DimXpert Tolerance3 Example (VB.NET)](Get_DimXpert_Tolerance3_Example_VBNET.htm)

## See Also

[IDimXpertPositionTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPositionTolerance.html)
[IDimXpertPositionTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPositionTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
