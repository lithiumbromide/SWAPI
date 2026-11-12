---
title: "GetNominalTopPlane Method (IDimXpertCompoundClosedSlot3DFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompoundClosedSlot3DFeature"
member: "GetNominalTopPlane"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundClosedSlot3DFeature~GetNominalTopPlane.html"
---

# GetNominalTopPlane Method (IDimXpertCompoundClosedSlot3DFeature)

Gets the coordinates and vector for the top reference plane of this DimXpert compound closed slot.

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
Dim instance As IDimXpertCompoundClosedSlot3DFeature
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

- `X`: X-coordinate of the top reference plane
- `Y`: Y-coordinate of the top reference plane
- `Z`: Z-coordinate of the top reference plane
- `I`: I component of the direction vector of the top reference plane
- `J`: J component of the direction vector of the top reference plane
- `K`: K component of the direction vector of the top reference plane

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertCompoundClosedSlot3DFeature::GetNominalTopPlane](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompoundClosedSlot3DFeature~GetNominalTopPlane.html).

## See Also

[IDimXpertCompoundClosedSlot3DFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundClosedSlot3DFeature.html)
[IDimXpertCompoundClosedSlot3DFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundClosedSlot3DFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
