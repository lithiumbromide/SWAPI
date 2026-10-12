---
title: "GetPlusAndMinusTolerance Method (IDimXpertDimensionTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertDimensionTolerance"
member: "GetPlusAndMinusTolerance"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionTolerance~GetPlusAndMinusTolerance.html"
---

# GetPlusAndMinusTolerance Method (IDimXpertDimensionTolerance)

Gets the plus and minus tolerance values for this DimXpert dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlusAndMinusTolerance( _
   ByRef Plus As System.Double, _
   ByRef Minus As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertDimensionTolerance
Dim Plus As System.Double
Dim Minus As System.Double
Dim value As System.Boolean

value = instance.GetPlusAndMinusTolerance(Plus, Minus)
```

### C#

```csharp
System.bool GetPlusAndMinusTolerance(
   out System.double Plus,
   out System.double Minus
)
```

### C++/CLI

```cpp
System.bool GetPlusAndMinusTolerance(
   [Out] System.double Plus,
   [Out] System.double Minus
)
```

### Parameters

- `Plus`: The plus value
- `Minus`: The minus value

### Return Value

True if the method call was successful; false otherwise

## VBA Syntax

See [DimXpertDimensionTolerance::GetPlusAndMinusTolerance](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertDimensionTolerance~GetPlusAndMinusTolerance.html).

## Examples

[Get DimXpert Tolerance Example (VBA)](Get_DimXpert_Tolerance_Example_VB.htm)
[Get DimXpert Tolerance Example (VB.NET)](Get_DimXpert_Tolerance_Example_VBNET.htm)

## See Also

[IDimXpertDimensionTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionTolerance.html)
[IDimXpertDimensionTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
