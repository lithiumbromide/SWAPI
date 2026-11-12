---
title: "GetPerUnitArea Method (IDimXpertFlatnessTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertFlatnessTolerance"
member: "GetPerUnitArea"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFlatnessTolerance~GetPerUnitArea.html"
---

# GetPerUnitArea Method (IDimXpertFlatnessTolerance)

Gets the per unit area for this flatness tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPerUnitArea( _
   ByRef Enabled As System.Boolean, _
   ByRef Length As System.Double, _
   ByRef Width As System.Double, _
   ByRef I As System.Double, _
   ByRef J As System.Double, _
   ByRef K As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertFlatnessTolerance
Dim Enabled As System.Boolean
Dim Length As System.Double
Dim Width As System.Double
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetPerUnitArea(Enabled, Length, Width, I, J, K)
```

### C#

```csharp
System.bool GetPerUnitArea(
   out System.bool Enabled,
   out System.double Length,
   out System.double Width,
   out System.double I,
   out System.double J,
   out System.double K
)
```

### C++/CLI

```cpp
System.bool GetPerUnitArea(
   [Out] System.bool Enabled,
   [Out] System.double Length,
   [Out] System.double Width,
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `Enabled`: True if enabled; false otherwise
- `Length`: Length of the area
- `Width`: Width of the area
- `I`: I component of the unit vector
- `J`: J component of the unit vector
- `K`: K component of the unit vector

### Return Value

True if the method call was successful; false otherwise

## VBA Syntax

See [DimXpertFlatnessTolerance::GetPerUnitArea](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertFlatnessTolerance~GetPerUnitArea.html).

## Examples

[Get DimXpert Tolerance Example (VBA)](Get_DimXpert_Tolerance_Example_VB.htm)
[Get DimXpert Tolerance Example (VB.NET)](Get_DimXpert_Tolerance_Example_VBNET.htm)

## See Also

[IDimXpertFlatnessTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFlatnessTolerance.html)
[IDimXpertFlatnessTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFlatnessTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
