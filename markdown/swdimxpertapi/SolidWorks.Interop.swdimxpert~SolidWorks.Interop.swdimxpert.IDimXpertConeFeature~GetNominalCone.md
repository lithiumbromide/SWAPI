---
title: "GetNominalCone Method (IDimXpertConeFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertConeFeature"
member: "GetNominalCone"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertConeFeature~GetNominalCone.html"
---

# GetNominalCone Method (IDimXpertConeFeature)

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
Dim instance As IDimXpertConeFeature
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
- `X`: X-coordinate of the cone
- `Y`: Y-coordinate of the cone
- `Z`: Z-coordinate of the cone
- `I`: I component of the direction vector of the cone
- `J`: J component of the direction vector of the cone
- `K`: K component of the direction vector of the cone

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertConeFeature::GetNominalCone](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompoundNotchFeature~GetNominalBottomPlane.html).

## Examples

[Get DimXpert Cone Feature Example (VBA)](Get_DimXpert_Cone_Feature_Example_VB.htm)
[Get DimXpert Cone Feature Example (VB.NET)](Get_DimXpert_Cone_Feature_Example_VBNET.htm)

## See Also

[IDimXpertConeFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertConeFeature.html)
[IDimXpertConeFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertConeFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
