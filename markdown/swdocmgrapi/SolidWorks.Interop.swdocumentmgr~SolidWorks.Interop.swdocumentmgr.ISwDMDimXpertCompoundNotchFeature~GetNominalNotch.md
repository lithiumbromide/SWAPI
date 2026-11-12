---
title: "GetNominalNotch Method (ISwDMDimXpertCompoundNotchFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompoundNotchFeature"
member: "GetNominalNotch"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature~GetNominalNotch.html"
---

# GetNominalNotch Method (ISwDMDimXpertCompoundNotchFeature)

Gets various attributes for this DimXpert compound notch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalNotch( _
   ByRef width As System.Double, _
   ByRef Length As System.Double, _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double, _
   ByRef I As System.Double, _
   ByRef J As System.Double, _
   ByRef K As System.Double, _
   ByRef LongitudeI As System.Double, _
   ByRef LongitudeJ As System.Double, _
   ByRef LongitudeK As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompoundNotchFeature
Dim width As System.Double
Dim Length As System.Double
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim LongitudeI As System.Double
Dim LongitudeJ As System.Double
Dim LongitudeK As System.Double
Dim value As System.Boolean

value = instance.GetNominalNotch(width, Length, X, Y, Z, I, J, K, LongitudeI, LongitudeJ, LongitudeK)
```

### C#

```csharp
System.bool GetNominalNotch(
   out System.double width,
   out System.double Length,
   out System.double X,
   out System.double Y,
   out System.double Z,
   out System.double I,
   out System.double J,
   out System.double K,
   out System.double LongitudeI,
   out System.double LongitudeJ,
   out System.double LongitudeK
)
```

### C++/CLI

```cpp
System.bool GetNominalNotch(
   [Out] System.double width,
   [Out] System.double Length,
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z,
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K,
   [Out] System.double LongitudeI,
   [Out] System.double LongitudeJ,
   [Out] System.double LongitudeK
)
```

### Parameters

- `width`: Width of the compound notch
- `Length`: Length of the compound notch
- `X`: x coordinate of the compound notch
- `Y`: y coordinate of the compound notch
- `Z`: z coordinate of the compound notch
- `I`: i component of the direction vector of the compound notch
- `J`: j component of the direction vector of the compound notch
- `K`: k component of the direction vector of the compound notch
- `LongitudeI`: i component of the longitudinal unit vector of the closed slot
- `LongitudeJ`: j component of the longitudinal unit vector of the closed slot
- `LongitudeK`: k component of the longitudinal unit vector of the closed slot

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertCompoundNotchFeature::GetNominalNotch](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompoundNotchFeature~GetNominalNotch.html).

## Examples

See the examples on the interface page.

## Remarks

The i, j, and k components of the longitudinal vector indicate the direction of a feature's length with respect to its part axes. For example, if the length of a feature goes along the y-axis of the part, its longitudinal vector is (0, 1, 0).

## See Also

[ISwDMDimXpertCompoundNotchFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature.html)
[ISwDMDimXpertCompoundNotchFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
