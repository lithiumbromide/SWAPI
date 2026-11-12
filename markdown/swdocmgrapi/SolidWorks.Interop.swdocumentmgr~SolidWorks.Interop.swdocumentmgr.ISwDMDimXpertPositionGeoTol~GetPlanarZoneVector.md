---
title: "GetPlanarZoneVector Method (ISwDMDimXpertPositionGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertPositionGeoTol"
member: "GetPlanarZoneVector"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol~GetPlanarZoneVector.html"
---

# GetPlanarZoneVector Method (ISwDMDimXpertPositionGeoTol)

Gets the planar zone vector that is used to compute this DimXpert position geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlanarZoneVector( _
   ByRef I As System.Double, _
   ByRef J As System.Double, _
   ByRef K As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertPositionGeoTol
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetPlanarZoneVector(I, J, K)
```

### C#

```csharp
System.bool GetPlanarZoneVector(
   out System.double I,
   out System.double J,
   out System.double K
)
```

### C++/CLI

```cpp
System.bool GetPlanarZoneVector(
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `I`: i component of the planar zone vector
- `J`: j component of the planar zone vector
- `K`: k component of the planar zone vector

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertPositionGeoTol::GetPlanarZoneVector](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertPositionGeoTol~GetPlanarZoneVector.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertPositionGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol.html)
[ISwDMDimXpertPositionGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPositionGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
