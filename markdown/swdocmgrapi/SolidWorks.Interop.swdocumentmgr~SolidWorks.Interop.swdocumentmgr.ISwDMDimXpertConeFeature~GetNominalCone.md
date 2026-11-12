---
title: "GetNominalCone Method (ISwDMDimXpertConeFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertConeFeature"
member: "GetNominalCone"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeFeature~GetNominalCone.html"
---

# GetNominalCone Method (ISwDMDimXpertConeFeature)

Gets various attributes for this DimXpert cone.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalCone( _
   ByRef Angle As System.Double, _
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
Dim instance As ISwDMDimXpertConeFeature
Dim Angle As System.Double
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetNominalCone(Angle, X, Y, Z, I, J, K)
```

### C#

```csharp
System.bool GetNominalCone(
   out System.double Angle,
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
System.bool GetNominalCone(
   [Out] System.double Angle,
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z,
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `Angle`: Angle in radians of the cone
- `X`: x coordinate of the cone
- `Y`: y coordinate of the cone
- `Z`: z coordinate of the cone
- `I`: i component of the direction vector of the cone
- `J`: j component of the direction vector of the cone
- `K`: k component of the direction vector of the cone

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertConeFeature::GetNominalCone](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertConeFeature~GetNominalCone.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertConeFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeFeature.html)
[ISwDMDimXpertConeFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
