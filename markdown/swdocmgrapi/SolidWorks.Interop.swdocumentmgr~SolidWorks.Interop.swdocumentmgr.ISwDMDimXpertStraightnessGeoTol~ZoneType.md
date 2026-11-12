---
title: "ZoneType Property (ISwDMDimXpertStraightnessGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertStraightnessGeoTol"
member: "ZoneType"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertStraightnessGeoTol~ZoneType.html"
---

# ZoneType Property (ISwDMDimXpertStraightnessGeoTol)

Gets the zone type of this DimXpert straightness geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ZoneType As swDmDimXpertStraightnessZoneType_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertStraightnessGeoTol
Dim value As swDmDimXpertStraightnessZoneType_e

value = instance.ZoneType
```

### C#

```csharp
swDmDimXpertStraightnessZoneType_e ZoneType {get;}
```

### C++/CLI

```cpp
property swDmDimXpertStraightnessZoneType_e ZoneType {
   swDmDimXpertStraightnessZoneType_e get();
}
```

### Property Value

Zone type for the straightness geometric tolerance as defined in [swDmDimXpertStraightnessZoneType_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertStraightnessZoneType_e.html)

## VBA Syntax

See [SwDMDimXpertStraightnessGeoTol::ZoneType](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertStraightnessGeoTol~ZoneType.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertStraightnessGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertStraightnessGeoTol.html)
[ISwDMDimXpertStraightnessGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertStraightnessGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
