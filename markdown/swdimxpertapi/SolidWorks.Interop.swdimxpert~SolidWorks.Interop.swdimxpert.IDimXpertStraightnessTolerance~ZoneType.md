---
title: "ZoneType Property (IDimXpertStraightnessTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertStraightnessTolerance"
member: "ZoneType"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertStraightnessTolerance~ZoneType.html"
---

# ZoneType Property (IDimXpertStraightnessTolerance)

Gets the zone type of this DimXpert straightness tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ZoneType As swDimXpertStraightnessZoneType_e
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertStraightnessTolerance
Dim value As swDimXpertStraightnessZoneType_e

value = instance.ZoneType
```

### C#

```csharp
swDimXpertStraightnessZoneType_e ZoneType {get;}
```

### C++/CLI

```cpp
property swDimXpertStraightnessZoneType_e ZoneType {
   swDimXpertStraightnessZoneType_e get();
}
```

### Property Value

Position zone type as defined in [swDimXpertStraightnessZoneType_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertStraightnessZoneType_e.html)

## VBA Syntax

See [DimXpertStraightnessTolerance::ZoneType](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertStraightnessTolerance~ZoneType.html).

## See Also

[IDimXpertStraightnessTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertStraightnessTolerance.html)
[IDimXpertStraightnessTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertStraightnessTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
