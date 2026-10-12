---
title: "GetNominalCylinder Method (ISwDMDimXpertCylinderFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCylinderFeature"
member: "GetNominalCylinder"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature~GetNominalCylinder.html"
---

# GetNominalCylinder Method (ISwDMDimXpertCylinderFeature)

Gets various attributes for this DimXpert cylinder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalCylinder( _
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
Dim instance As ISwDMDimXpertCylinderFeature
Dim R As System.Double
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetNominalCylinder(R, X, Y, Z, I, J, K)
```

### C#

```csharp
System.bool GetNominalCylinder(
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
System.bool GetNominalCylinder(
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

- `R`: Radius of cylinder
- `X`: x coordinate of the cylinder
- `Y`: y coordinate of the cylinder
- `Z`: z coordinate of the cylinder
- `I`: i component of the direction vector of the cylinder
- `J`: j component of the direction vector of the cylinder
- `K`: k component of the direction vector of the cylinder

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertCylinderFeature::GetNominalCylinder](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCylinderFeature~GetNominalCylinder.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCylinderFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature.html)
[ISwDMDimXpertCylinderFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
