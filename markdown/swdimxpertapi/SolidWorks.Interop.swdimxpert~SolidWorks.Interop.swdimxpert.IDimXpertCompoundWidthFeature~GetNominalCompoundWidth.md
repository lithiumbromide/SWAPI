---
title: "GetNominalCompoundWidth Method (IDimXpertCompoundWidthFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompoundWidthFeature"
member: "GetNominalCompoundWidth"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundWidthFeature~GetNominalCompoundWidth.html"
---

# GetNominalCompoundWidth Method (IDimXpertCompoundWidthFeature)

Gets various attributes for this DimXpert compound width.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalCompoundWidth( _
   ByRef Width As System.Double, _
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
Dim instance As IDimXpertCompoundWidthFeature
Dim Width As System.Double
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetNominalCompoundWidth(Width, X, Y, Z, I, J, K)
```

### C#

```csharp
System.bool GetNominalCompoundWidth(
   out System.double Width,
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
System.bool GetNominalCompoundWidth(
   [Out] System.double Width,
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z,
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `Width`: Width of the feature
- `X`: X-coordinate of the width
- `Y`: Y-coordinate of the width
- `Z`: Z-coordinate of the width
- `I`: I component of the direction vector of the width
- `J`: J component of the direction vector of the width
- `K`: K component of the direction vector of the width

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertCompoundWidthFeature::GetNominalCompoundWidth](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompoundWidthFeature~GetNominalCompoundWidth.html).

## Examples

[Get and Set Size Dimension Example (C#)](Get_and_Set_Size_Dimension_Example_CSharp.htm)
[Get and Set Size Dimension Example (VB.NET)](Get_and_Set_Size_Dimension_Example_VBNET.htm)
[Get and Set Size Dimension Example (VBA)](Get_and_Set_Size_Dimension_Example_VB.htm)
[Get DimXpert Width And Best Fit Plane Features Example (VBA)](Get_DimXpert_Width_And_BestFitPlane_Features_Example_VB.htm)
[Get DimXpert Width And Best Fit Plane Features Example (VB.NET)](Get_DimXpert_Width_And_BestFitPlane_Features_Example_VBNET.htm)

## See Also

[IDimXpertCompoundWidthFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundWidthFeature.html)
[IDimXpertCompoundWidthFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundWidthFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
