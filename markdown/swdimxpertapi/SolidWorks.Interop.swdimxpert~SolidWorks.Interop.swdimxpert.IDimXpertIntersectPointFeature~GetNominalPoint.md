---
title: "GetNominalPoint Method (IDimXpertIntersectPointFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertIntersectPointFeature"
member: "GetNominalPoint"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectPointFeature~GetNominalPoint.html"
---

# GetNominalPoint Method (IDimXpertIntersectPointFeature)

Gets the coordinates of this DimXpert intersect point.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertIntersectPointFeature
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.GetNominalPoint(X, Y, Z)
```

### C#

```csharp
System.bool GetNominalPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### C++/CLI

```cpp
System.bool GetNominalPoint(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: X-coordinate of the intersect point
- `Y`: Y-coordinate of the intersect point
- `Z`: Z-coordinate of the intersect point

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertIntersectPointFeature::GetNominalPoint](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertIntersectPointFeature~GetNominalPoint.html).

## Examples

[Get DimXpert Intersect Features Example (VBA)](Get_DimXpert_Intersect_Features_Example_VB.htm)
[Get DimXpert Intersect Features Example (VB.NET)](Get_DimXpert_Intersect_Features_Example_VBNET.htm)

## See Also

[IDimXpertIntersectPointFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectPointFeature.html)
[IDimXpertIntersectPointFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectPointFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
