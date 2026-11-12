---
title: "GetUpperAndLowerLimit Method (IDimXpertDimensionTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertDimensionTolerance"
member: "GetUpperAndLowerLimit"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionTolerance~GetUpperAndLowerLimit.html"
---

# GetUpperAndLowerLimit Method (IDimXpertDimensionTolerance)

Gets the upper and lower tolerance limits for this DimXpert dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUpperAndLowerLimit( _
   ByRef Upper As System.Double, _
   ByRef Lower As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertDimensionTolerance
Dim Upper As System.Double
Dim Lower As System.Double
Dim value As System.Boolean

value = instance.GetUpperAndLowerLimit(Upper, Lower)
```

### C#

```csharp
System.bool GetUpperAndLowerLimit(
   out System.double Upper,
   out System.double Lower
)
```

### C++/CLI

```cpp
System.bool GetUpperAndLowerLimit(
   [Out] System.double Upper,
   [Out] System.double Lower
)
```

### Parameters

- `Upper`: Upper limit
- `Lower`: Lower limit

### Return Value

True if the method call is successful; false otherwise

## VBA Syntax

See [DimXpertDimensionTolerance::GetUpperAndLowerLimit](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertDimensionTolerance~GetUpperAndLowerLimit.html).

## Examples

[Get DimXpert Tolerance Example (VBA)](Get_DimXpert_Tolerance_Example_VB.htm)
[Get DimXpert Tolerance Example (VB.NET)](Get_DimXpert_Tolerance_Example_VBNET.htm)

## See Also

[IDimXpertDimensionTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionTolerance.html)
[IDimXpertDimensionTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
