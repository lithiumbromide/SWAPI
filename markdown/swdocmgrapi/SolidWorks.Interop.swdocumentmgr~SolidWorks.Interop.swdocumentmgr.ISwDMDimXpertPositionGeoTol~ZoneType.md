---
title: "ZoneType Property (ISwDMDimXpertPositionGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertPositionGeoTol"
member: "ZoneType"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol~ZoneType.html"
---

# ZoneType Property (ISwDMDimXpertPositionGeoTol)

Gets the zone type of this DimXpert position geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ZoneType As swDmDimXpertPositionZoneType_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertPositionGeoTol
Dim value As swDmDimXpertPositionZoneType_e

value = instance.ZoneType
```

### C#

```csharp
swDmDimXpertPositionZoneType_e ZoneType {get;}
```

### C++/CLI

```cpp
property swDmDimXpertPositionZoneType_e ZoneType {
   swDmDimXpertPositionZoneType_e get();
}
```

### Property Value

Zone type for the position geometric tolerance as defined in [swDmDimXpertPositionZoneType_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertPositionZoneType_e.html)

## VBA Syntax

See [SwDMDimXpertPositionGeoTol::ZoneType](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertPositionGeoTol~ZoneType.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertPositionGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol.html)
[ISwDMDimXpertPositionGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
