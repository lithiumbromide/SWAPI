---
title: "ZoneType Property (ISwDMDimXpertCompositePositionGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompositePositionGeoTol"
member: "ZoneType"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol~ZoneType.html"
---

# ZoneType Property (ISwDMDimXpertCompositePositionGeoTol)

Gets the zone type of this DimXpert composite position geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ZoneType As swDmDimXpertPositionZoneType_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompositePositionGeoTol
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

Type of zone for the position as defined in [swDmDimXpertPositionZoneType_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertPositionZoneType_e.html)

## VBA Syntax

See [SwDMDimXpertCompositePositionGeoTol::ZoneType](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompositePositionGeoTol~ZoneType.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompositePositionGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol.html)
[ISwDMDimXpertCompositePositionGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositePositionGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
