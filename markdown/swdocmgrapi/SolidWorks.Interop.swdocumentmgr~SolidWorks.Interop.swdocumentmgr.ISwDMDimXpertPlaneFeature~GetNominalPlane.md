---
title: "GetNominalPlane Method (ISwDMDimXpertPlaneFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertPlaneFeature"
member: "GetNominalPlane"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPlaneFeature~GetNominalPlane.html"
---

# GetNominalPlane Method (ISwDMDimXpertPlaneFeature)

Gets the coordinates and vector for this DimXpert plane.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalPlane( _
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
Dim instance As ISwDMDimXpertPlaneFeature
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetNominalPlane(X, Y, Z, I, J, K)
```

### C#

```csharp
System.bool GetNominalPlane(
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
System.bool GetNominalPlane(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z,
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `X`: x coordinate of the plane
- `Y`: y coordinate of the plane
- `Z`: z coordinate of the plane
- `I`: i component of the direction vector of the plane
- `J`: j component of the direction vector of the plane
- `K`: k component of the direction vector of the plane

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertPlaneFeature::GetNominalPlane](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertPlaneFeature~GetNominalPlane.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertPlaneFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPlaneFeature.html)
[ISwDMDimXpertPlaneFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPlaneFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
