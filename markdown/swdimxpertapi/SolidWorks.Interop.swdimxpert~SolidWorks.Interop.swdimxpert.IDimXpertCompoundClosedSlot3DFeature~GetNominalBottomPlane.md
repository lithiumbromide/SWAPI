---
title: "GetNominalBottomPlane Method (IDimXpertCompoundClosedSlot3DFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompoundClosedSlot3DFeature"
member: "GetNominalBottomPlane"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundClosedSlot3DFeature~GetNominalBottomPlane.html"
---

# GetNominalBottomPlane Method (IDimXpertCompoundClosedSlot3DFeature)

Gets the coordinates and vector for the bottom reference plane of this DimXpert compound closed slot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalBottomPlane( _
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
Dim instance As IDimXpertCompoundClosedSlot3DFeature
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetNominalBottomPlane(X, Y, Z, I, J, K)
```

### C#

```csharp
System.bool GetNominalBottomPlane(
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
System.bool GetNominalBottomPlane(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z,
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `X`: X-coordinate of the bottom plane
- `Y`: Y-coordinate of the bottom plane
- `Z`: Z-coordinate of the bottom plane
- `I`: I component of the direction vector of the bottom plane
- `J`: J component of the direction vector of the bottom plane
- `K`: K component of the direction vector of the bottom plane

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertCompoundClosedSlot3DFeature::GetNominalBottomPlane](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompoundClosedSlot3DFeature~GetNominalBottomPlane.html).

## See Also

[IDimXpertCompoundClosedSlot3DFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundClosedSlot3DFeature.html)
[IDimXpertCompoundClosedSlot3DFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundClosedSlot3DFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
