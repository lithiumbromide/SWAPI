---
title: "GetPerUnitLength Method (IDimXpertStraightnessTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertStraightnessTolerance"
member: "GetPerUnitLength"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertStraightnessTolerance~GetPerUnitLength.html"
---

# GetPerUnitLength Method (IDimXpertStraightnessTolerance)

Gets the per unit length for this DimXpert straightness tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPerUnitLength( _
   ByRef Enabled As System.Boolean, _
   ByRef Distance As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertStraightnessTolerance
Dim Enabled As System.Boolean
Dim Distance As System.Double
Dim value As System.Boolean

value = instance.GetPerUnitLength(Enabled, Distance)
```

### C#

```csharp
System.bool GetPerUnitLength(
   out System.bool Enabled,
   out System.double Distance
)
```

### C++/CLI

```cpp
System.bool GetPerUnitLength(
   [Out] System.bool Enabled,
   [Out] System.double Distance
)
```

### Parameters

- `Enabled`: True if per unit length is in effect; false otherwise
- `Distance`: Length distance per unit length

### Return Value

True if the method call is successful; false otherwise

## VBA Syntax

See [DimXpertStraightnessTolerance::GetPerUnitLength](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertStraightnessTolerance~GetPerUnitLength.html).

## Examples

[Get DimXpert Tolerance4 Example (VBA)](Get_DimXpert_Tolerance4_Example_VB.htm)
[Get DimXpert Tolerance4 Example (VB.NET)](Get_DimXpert_Tolerance4_Example_VBNET.htm)

## See Also

[IDimXpertStraightnessTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertStraightnessTolerance.html)
[IDimXpertStraightnessTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertStraightnessTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
