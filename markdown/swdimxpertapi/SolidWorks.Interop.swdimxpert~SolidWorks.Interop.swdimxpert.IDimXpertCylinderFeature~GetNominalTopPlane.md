---
title: "GetNominalTopPlane Method (IDimXpertCylinderFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCylinderFeature"
member: "GetNominalTopPlane"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCylinderFeature~GetNominalTopPlane.html"
---

# GetNominalTopPlane Method (IDimXpertCylinderFeature)

Gets the coordinates and vector for the top plane of this DimXpert cylinder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalTopPlane( _
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
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetNominalTopPlane(X, Y, Z, I, J, K)
```

### C#

```csharp
System.bool GetNominalTopPlane(
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
System.bool GetNominalTopPlane(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z,
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `X`: X-coordinate of the top plane
- `Y`: Y-coordinate of the top plane
- `Z`: Z-coordinate of the top plane
- `I`: I component of the direction vector of the top plane
- `J`: J component of the direction vector of the top plane
- `K`: K component of the direction vector of the top plane

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertCylinderFeature::GetNominalTopPlane](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCylinderFeature~GetNominalTopPlane.html).

## Examples

[Get DimXpert Feature Example (VBA)](Get_DimXpert_Feature_Example_VB.htm)
[Get DimXpert Feature Example (VB.NET)](Get_DimXpert_Feature_Example_VBNET.htm)

## See Also

[IDimXpertCylinderFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCylinderFeature.html)
[IDimXpertCylinderFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCylinderFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
