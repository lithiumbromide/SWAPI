---
title: "GetZoneDirection Method (ISwDMDimXpertSymmetryGeoTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertSymmetryGeoTol"
member: "GetZoneDirection"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSymmetryGeoTol~GetZoneDirection.html"
---

# GetZoneDirection Method (ISwDMDimXpertSymmetryGeoTol)

Gets the zone direction of this DimXpert symmetry geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetZoneDirection( _
   ByRef I As System.Double, _
   ByRef J As System.Double, _
   ByRef K As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertSymmetryGeoTol
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetZoneDirection(I, J, K)
```

### C#

```csharp
System.bool GetZoneDirection(
   out System.double I,
   out System.double J,
   out System.double K
)
```

### C++/CLI

```cpp
System.bool GetZoneDirection(
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `I`: i component of zone direction vector
- `J`: j component of zone direction vector
- `K`: k component of zone direction vector

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertSymmetryGeoTol::GetZoneDirection](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertSymmetryGeoTol~GetZoneDirection.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertSymmetryGeoTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSymmetryGeoTol.html)
[ISwDMDimXpertSymmetryGeoTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSymmetryGeoTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
