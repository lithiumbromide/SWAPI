---
title: "GetNominalTopPlane Method (ISwDMDimXpertCylinderFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCylinderFeature"
member: "GetNominalTopPlane"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature~GetNominalTopPlane.html"
---

# GetNominalTopPlane Method (ISwDMDimXpertCylinderFeature)

Gets the coordinates and vector for the plane at the top of this DimXpert cylinder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalTopPlane( _
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
Dim instance As ISwDMDimXpertCylinderFeature
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetNominalTopPlane(X, Y, Z, I, J, K)
```

### C#

```csharp
System.bool GetNominalTopPlane(
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
System.bool GetNominalTopPlane(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z,
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `X`: x coordinate of the top plane
- `Y`: y coordinate of the top plane
- `Z`: z coordinate of the top plane
- `I`: i component of the direction vector of the top plane
- `J`: j component of the direction vector of the top plane
- `K`: k component of the direction vector of the top plane

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertCylinderFeature::GetNominalTopPlane](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCylinderFeature~GetNominalTopPlane.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCylinderFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature.html)
[ISwDMDimXpertCylinderFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
