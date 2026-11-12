---
title: "GetPlanarZoneVector Method (ISwDMDimXpertOrientationGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertOrientationGeoTol"
member: "GetPlanarZoneVector"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol~GetPlanarZoneVector.html"
---

# GetPlanarZoneVector Method (ISwDMDimXpertOrientationGeoTol)

Gets the planar zone vector that is used to compute this DimXpert orientation geometric tolerance.

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
Dim instance As ISwDMDimXpertOrientationGeoTol
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

See [SwDMDimXpertOrientationGeoTol::GetPlanarZoneVector](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertOrientationGeoTol~GetPlanarZoneVector.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertOrientationGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol.html)
[ISwDMDimXpertOrientationGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertOrientationGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
