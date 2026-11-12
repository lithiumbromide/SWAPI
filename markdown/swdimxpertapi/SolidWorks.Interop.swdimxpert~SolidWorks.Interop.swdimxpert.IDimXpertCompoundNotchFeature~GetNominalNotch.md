---
title: "GetNominalNotch Method (IDimXpertCompoundNotchFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompoundNotchFeature"
member: "GetNominalNotch"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundNotchFeature~GetNominalNotch.html"
---

# GetNominalNotch Method (IDimXpertCompoundNotchFeature)

Gets various attributes for this DimXpert compound notch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalNotch( _
   ByRef Width As System.Double, _
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
Dim instance As IDimXpertCompoundNotchFeature
Dim Width As System.Double
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

value = instance.GetNominalNotch(Width, Length, X, Y, Z, I, J, K, LongitudeI, LongitudeJ, LongitudeK)
```

### C#

```csharp
System.bool GetNominalNotch(
   out System.double Width,
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
   [Out] System.double Width,
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

- `Width`: Width of the notch
- `Length`: Length of the notch
- `X`: X-coordinate of the notch
- `Y`: Y-coordinate of the notch
- `Z`: Z-coordinate of the notch
- `I`: I component of the direction vector of the notch
- `J`: J component of the direction vector of the notch
- `K`: K component of the direction vector of the notch
- `LongitudeI`: I component of the longitudinal unit vector of the notch
- `LongitudeJ`: J component of the longitudinal unit vector of the notch
- `LongitudeK`: K component of the longitudinal unit vector of the notch

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertCompoundNotchFeature::GetNominalNotch](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompoundNotchFeature~GetNominalNotch.html).

## Examples

[Get More DimXpert Feature Examples (VBA)](Get_DimXpert_Feature2_Example_VB.htm)
[Get More DimXpert Feature Examples (VB.NET)](Get_DimXpert_Feature2_Example_VBNET.htm)

## Remarks

The longitudinal i, j, and k component vectors indicate the direction of a notch's length with respect to its part axes. For example, if the length of a notch goes along the y-axis of the part, its longitudinal vector is (0, 1, 0).

## See Also

[IDimXpertCompoundNotchFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundNotchFeature.html)
[IDimXpertCompoundNotchFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundNotchFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
