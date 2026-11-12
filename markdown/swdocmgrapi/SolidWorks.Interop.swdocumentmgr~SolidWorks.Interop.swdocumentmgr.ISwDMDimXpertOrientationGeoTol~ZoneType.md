---
title: "ZoneType Property (ISwDMDimXpertOrientationGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertOrientationGeoTol"
member: "ZoneType"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol~ZoneType.html"
---

# ZoneType Property (ISwDMDimXpertOrientationGeoTol)

Gets the zone type of this DimXpert orientation geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ZoneType As swDmDimXpertOrientationZoneType_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertOrientationGeoTol
Dim value As swDmDimXpertOrientationZoneType_e

value = instance.ZoneType
```

### C#

```csharp
swDmDimXpertOrientationZoneType_e ZoneType {get;}
```

### C++/CLI

```cpp
property swDmDimXpertOrientationZoneType_e ZoneType {
   swDmDimXpertOrientationZoneType_e get();
}
```

### Property Value

Zone type for the orientation tolerance as defined in [swDmDimXpertOrientationZoneType_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertOrientationZoneType_e.html)

## VBA Syntax

See [SwDMDimXpertOrientationGeoTol::ZoneType](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertOrientationGeoTol~ZoneType.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertOrientationGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol.html)
[ISwDMDimXpertOrientationGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
