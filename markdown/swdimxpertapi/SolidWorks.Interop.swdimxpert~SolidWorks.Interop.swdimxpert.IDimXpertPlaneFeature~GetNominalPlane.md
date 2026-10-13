---
title: "GetNominalPlane Method (IDimXpertPlaneFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPlaneFeature"
member: "GetNominalPlane"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPlaneFeature~GetNominalPlane.html"
---

# GetNominalPlane Method (IDimXpertPlaneFeature)

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
Dim instance As IDimXpertPlaneFeature
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

- `X`: X-coordinate of the plane
- `Y`: Y-coordinate of the plane
- `Z`: Z-coordinate of the plane
- `I`: I component of the direction vector of the plane
- `J`: J component of the direction vector of the plane
- `K`: K component of the direction vector of the plane

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertPlaneFeature::GetNominalPlane](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPlaneFeature~GetNominalPlane.html).

## Examples

[Get DimXpert Feature Example (VBA)](Get_DimXpert_Feature_Example_VB.htm)
[Get DimXpert Feature Example (VB.NET)](Get_DimXpert_Feature_Example_VBNET.htm)

## See Also

[IDimXpertPlaneFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPlaneFeature.html)
[IDimXpertPlaneFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPlaneFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
