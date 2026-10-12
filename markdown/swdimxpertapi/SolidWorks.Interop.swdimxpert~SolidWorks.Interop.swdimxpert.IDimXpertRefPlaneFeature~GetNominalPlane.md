---
title: "GetNominalPlane Method (IDimXpertRefPlaneFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertRefPlaneFeature"
member: "GetNominalPlane"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertRefPlaneFeature~GetNominalPlane.html"
---

# GetNominalPlane Method (IDimXpertRefPlaneFeature)

Gets the coordinates and vector for this DimXpert reference plane.

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
Dim instance As IDimXpertRefPlaneFeature
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

- `X`: X-coordinate of the planev
- `Y`: Y-coordinate of the plane
- `Z`: Z-coordinate of the plane
- `I`: I component of the direction vector of the plane
- `J`: J component of the direction vector of the plane
- `K`: K component of the direction vector of the plane

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertRefPlaneFeature::GetNominalPlane](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertRefPlaneFeature~GetNominalPlane.html).

## See Also

[IDimXpertRefPlaneFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertRefPlaneFeature.html)
[IDimXpertRefPlaneFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertRefPlaneFeature_members.html)

## Availability

SOLIDWORKS 2026 SP02, Revision Number 34.2
