---
title: "GetNominalClosedSlot Method (IDimXpertCompoundClosedSlot3DFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompoundClosedSlot3DFeature"
member: "GetNominalClosedSlot"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundClosedSlot3DFeature~GetNominalClosedSlot.html"
---

# GetNominalClosedSlot Method (IDimXpertCompoundClosedSlot3DFeature)

Gets various attributes for this DimXpert compound closed slot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalClosedSlot( _
   ByRef Width As System.Double, _
   ByRef Length As System.Double, _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double, _
   ByRef I As System.Double, _
   ByRef J As System.Double, _
   ByRef K As System.Double, _
   ByRef LongitudeI As System.Double, _
   ByRef LongitudeJ As System.Double, _
   ByRef LongitudeK As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompoundClosedSlot3DFeature
Dim Width As System.Double
Dim Length As System.Double
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim LongitudeI As System.Double
Dim LongitudeJ As System.Double
Dim LongitudeK As System.Double
Dim value As System.Boolean

value = instance.GetNominalClosedSlot(Width, Length, X, Y, Z, I, J, K, LongitudeI, LongitudeJ, LongitudeK)
```

### C#

```csharp
System.bool GetNominalClosedSlot(
   out System.double Width,
   out System.double Length,
   out System.double X,
   out System.double Y,
   out System.double Z,
   out System.double I,
   out System.double J,
   out System.double K,
   out System.double LongitudeI,
   out System.double LongitudeJ,
   out System.double LongitudeK
)
```

### C++/CLI

```cpp
System.bool GetNominalClosedSlot(
   [Out] System.double Width,
   [Out] System.double Length,
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z,
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K,
   [Out] System.double LongitudeI,
   [Out] System.double LongitudeJ,
   [Out] System.double LongitudeK
)
```

### Parameters

- `Width`: Width of the closed slot
- `Length`: Length of the closed slot
- `X`: X-coordinate of the closed slot origin
- `Y`: Y-coordinate of the closed slot origin
- `Z`: Z-coordinate of the closed slot origin
- `I`: I component of the direction vector of the closed slot
- `J`: J component of the direction vector of the closed slot
- `K`: K component of the direction vector of the closed slot
- `LongitudeI`: I component of the longitudinal unit vector of the closed slot
- `LongitudeJ`: J component of the longitudinal unit vector of the closed slot
- `LongitudeK`: K component of the longitudinal unit vector of the closed slot

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertCompoundClosedSlot3DFeature::GetNominalClosedSlot](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompoundClosedSlot3DFeature~GetNominalClosedSlot.html).

## Examples

[Get DimXpert Feature Example (VBA)](Get_DimXpert_Feature_Example_VB.htm)
[Get DimXpert Feature Example (VB.NET)](Get_DimXpert_Feature_Example_VBNET.htm)

## Remarks

The i, j, and k components of the longitudinal vector indicate the direction of a feature's length with respect to its part axes. For example, if the length of a feature goes along the y-axis of the part, its longitudinal vector is (0, 1, 0).

## See Also

[IDimXpertCompoundClosedSlot3DFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundClosedSlot3DFeature.html)
[IDimXpertCompoundClosedSlot3DFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundClosedSlot3DFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
