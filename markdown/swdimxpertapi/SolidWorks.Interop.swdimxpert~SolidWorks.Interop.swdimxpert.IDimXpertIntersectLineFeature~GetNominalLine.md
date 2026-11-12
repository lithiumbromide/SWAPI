---
title: "GetNominalLine Method (IDimXpertIntersectLineFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertIntersectLineFeature"
member: "GetNominalLine"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectLineFeature~GetNominalLine.html"
---

# GetNominalLine Method (IDimXpertIntersectLineFeature)

Gets the coordinates and vector for this DimXpert intersect line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalLine( _
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
Dim instance As IDimXpertIntersectLineFeature
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetNominalLine(X, Y, Z, I, J, K)
```

### C#

```csharp
System.bool GetNominalLine(
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
System.bool GetNominalLine(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z,
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `X`: X-coordinate of the intersect line
- `Y`: Y-coordinate of the intersect line
- `Z`: Z-coordinate of the intersect line
- `I`: I component of the direction vector of the intersect line
- `J`: J component of the direction vector of the intersect line
- `K`: K component of the direction vector of the intersect line

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertIntersectLineFeature::GetNominalLine](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertIntersectLineFeature~GetNominalLine.html).

## Examples

[Get DimXpert Intersect Features Example (VBA)](Get_DimXpert_Intersect_Features_Example_VB.htm)
[Get DimXpert Intersect Features Example (VB.NET)](Get_DimXpert_Intersect_Features_Example_VBNET.htm)

## See Also

[IDimXpertIntersectLineFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectLineFeature.html)
[IDimXpertIntersectLineFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectLineFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
