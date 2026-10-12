---
title: "GetNominalPlane Method (IDimXpertIntersectPlaneFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertIntersectPlaneFeature"
member: "GetNominalPlane"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectPlaneFeature~GetNominalPlane.html"
---

# GetNominalPlane Method (IDimXpertIntersectPlaneFeature)

Gets the coordinates and vector for this DimXpert intersect plane.

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
Dim instance As IDimXpertIntersectPlaneFeature
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

- `X`: X-coordinate of the intersect plane
- `Y`: Y-coordinate of the intersect plane
- `Z`: Z-coordinate of the intersect plane
- `I`: I component of the direction vector of the intersect plane
- `J`: J component of the direction vector of the intersect plane
- `K`: K component of the direction vector of the intersect plane

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertIntersectPlaneFeature::GetNominalPlane](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertIntersectPlaneFeature~GetNominalPlane.html).

## See Also

[IDimXpertIntersectPlaneFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectPlaneFeature.html)
[IDimXpertIntersectPlaneFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectPlaneFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
