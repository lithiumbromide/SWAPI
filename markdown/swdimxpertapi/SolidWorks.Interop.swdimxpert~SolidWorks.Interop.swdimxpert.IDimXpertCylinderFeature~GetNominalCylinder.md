---
title: "GetNominalCylinder Method (IDimXpertCylinderFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCylinderFeature"
member: "GetNominalCylinder"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCylinderFeature~GetNominalCylinder.html"
---

# GetNominalCylinder Method (IDimXpertCylinderFeature)

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
Dim instance As IDimXpertCylinderFeature
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

- `R`: Radius of the cylinder
- `X`: X-coordinate of the cylinder
- `Y`: Y-coordinate of the cylinder
- `Z`: Z-coordinate of the cylinder
- `I`: I component of the direction vector of the cylinder
- `J`: J component of the direction vector of the cylinder
- `K`: K component of the direction vector of the cylinder

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertCylinderFeature::GetNominalCylinder](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCylinderFeature~GetNominalCylinder.html).

## See Also

[IDimXpertCylinderFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCylinderFeature.html)
[IDimXpertCylinderFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCylinderFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
