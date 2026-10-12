---
title: "GetNominalCircle Method (ISwDMDimXpertIntersectCircleFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertIntersectCircleFeature"
member: "GetNominalCircle"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectCircleFeature~GetNominalCircle.html"
---

# GetNominalCircle Method (ISwDMDimXpertIntersectCircleFeature)

Gets the origin coordinates, radius, and vector for this DimXpert intersect circle.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalCircle( _
   ByRef R As System.Double, _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double, _
   ByRef I As System.Double, _
   ByRef J As System.Double, _
   ByRef K As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertIntersectCircleFeature
Dim R As System.Double
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetNominalCircle(R, X, Y, Z, I, J, K)
```

### C#

```csharp
System.bool GetNominalCircle(
   out System.double R,
   out System.double X,
   out System.double Y,
   out System.double Z,
   out System.double I,
   out System.double J,
   out System.double K
)
```

### C++/CLI

```cpp
System.bool GetNominalCircle(
   [Out] System.double R,
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z,
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `R`: Radius of the intersect circle
- `X`: x coordinate of the origin of the intersect circle
- `Y`: y coordinate of the origin of the intersect circle
- `Z`: z coordinate of the origin of the intersect circle
- `I`: i component of the direction vector of the intersect circle
- `J`: j component of the direction vector of the intersect circle
- `K`: k component of the direction vector of the intersect circle

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertIntersectCircleFeature::GetNominalCircle](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertIntersectCircleFeature~GetNominalCircle.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertIntersectCircleFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectCircleFeature.html)
[ISwDMDimXpertIntersectCircleFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectCircleFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
