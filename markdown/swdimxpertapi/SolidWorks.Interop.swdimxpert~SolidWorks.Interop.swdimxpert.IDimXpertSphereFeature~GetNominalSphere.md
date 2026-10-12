---
title: "GetNominalSphere Method (IDimXpertSphereFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertSphereFeature"
member: "GetNominalSphere"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertSphereFeature~GetNominalSphere.html"
---

# GetNominalSphere Method (IDimXpertSphereFeature)

Gets the coordinates and vector for this DimXpert sphere.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalSphere( _
   ByRef R As System.Double, _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertSphereFeature
Dim R As System.Double
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.GetNominalSphere(R, X, Y, Z)
```

### C#

```csharp
System.bool GetNominalSphere(
   out System.double R,
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### C++/CLI

```cpp
System.bool GetNominalSphere(
   [Out] System.double R,
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `R`: Radius of the sphere
- `X`: X-coordinate of the origin of the sphere
- `Y`: Y-coordinate of the origin of the sphere
- `Z`: Z-coordinate of the origin of the sphere

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertSphereFeature::GetNominalSphere](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertSphereFeature~GetNominalSphere.html).

## Examples

[Get DimXpert Sphere Feature Example (VBA)](Get_DimXpert_Sphere_Feature_Example_VB.htm)
[Get DimXpert Sphere Feature Example (VB.NET)](Get_DimXpert_Sphere_Feature_Example_VBNET.htm)

## See Also

[IDimXpertSphereFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertSphereFeature.html)
[IDimXpertSphereFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertSphereFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
