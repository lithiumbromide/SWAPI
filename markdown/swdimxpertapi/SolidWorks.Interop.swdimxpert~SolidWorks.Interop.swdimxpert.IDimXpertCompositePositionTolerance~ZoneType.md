---
title: "ZoneType Property (IDimXpertCompositePositionTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompositePositionTolerance"
member: "ZoneType"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositePositionTolerance~ZoneType.html"
---

# ZoneType Property (IDimXpertCompositePositionTolerance)

Gets the zone type of this DimXpert composite position tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ZoneType As swDimXpertPositionZoneType_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompositePositionTolerance
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

See [DimXpertCompositePositionTolerance::ZoneType](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompositePositionTolerance~ZoneType.html).

## Examples

[Get DimXpert Tolerance3 Example (VBA)](Get_DimXpert_Tolerance3_Example_VB.htm)
[Get DimXpert Tolerance3 Example (VB.NET)](Get_DimXpert_Tolerance3_Example_VBNET.htm)

## See Also

[IDimXpertCompositePositionTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositePositionTolerance.html)
[IDimXpertCompositePositionTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompositePositionTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
