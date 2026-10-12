---
title: "GetNominalCircle Method (IDimXpertIntersectCircleFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertIntersectCircleFeature"
member: "GetNominalCircle"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectCircleFeature~GetNominalCircle.html"
---

# GetNominalCircle Method (IDimXpertIntersectCircleFeature)

Gets the coordinates and vector for this DimXpert intersect circle.

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
Dim instance As IDimXpertIntersectCircleFeature
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
- `X`: X-coordinate of the origin of the intersect circle
- `Y`: Y-coordinate of the origin of the intersect circle
- `Z`: Z-coordinate of the origin of the intersect circle
- `I`: I component of the direction vector of the intersect circle
- `J`: J component of the direction vector of the intersect circle
- `K`: K component of the direction vector of the intersect circle

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertIntersectCircleFeature::GetNominalCircle](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertIntersectCircleFeature~GetNominalCircle.html).

## Examples

[Get DimXpert Intersect Features Example (VBA)](Get_DimXpert_Intersect_Features_Example_VB.htm)
[Get DimXpert Intersect Features Example (VB.NET)](Get_DimXpert_Intersect_Features_Example_VBNET.htm)

## Remarks

The i, j, and k vector components indicate the pierce direction of a feature. For example, if a feature is sketched on the front x-y plane, its pierce vector is (0, 0, 1).

## See Also

[IDimXpertIntersectCircleFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectCircleFeature.html)
[IDimXpertIntersectCircleFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectCircleFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
