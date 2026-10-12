---
title: "GetMaxValue2 Method (IDimensionTolerance)"
project: "SOLIDWORKS API Help"
interface: "IDimensionTolerance"
member: "GetMaxValue2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMaxValue2.html"
---

# GetMaxValue2 Method (IDimensionTolerance)

Gets the tolerance maximum value.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaxValue2( _
   ByRef ToleranceValue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimensionTolerance
Dim ToleranceValue As System.Double
Dim value As System.Integer

value = instance.GetMaxValue2(ToleranceValue)
```

### C#

```csharp
System.int GetMaxValue2(
   out System.double ToleranceValue
)
```

### C++/CLI

```cpp
System.int GetMaxValue2(
   [Out] System.double ToleranceValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ToleranceValue`: Tolerance maximum value

### Return Value

Status of tolerance maximum value as defined in [swDimensionToleranceWarning_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDimensionToleranceWarning_e.html)

## VBA Syntax

See [DimensionTolerance::GetMaxValue2](ms-its:sldworksapivb6.chm::/sldworks~DimensionTolerance~GetMaxValue2.html).

## Examples

[Get Dimension Tolerance (C#)](Get_Dimension_Tolerance_Example_CSharp.htm)
[Get Dimension Tolerance (VB.NET)](Get_Dimension_Tolerance_Example_VBNET.htm)
[Get Dimension Tolerance (VBA)](Get_Dimension_Tolerance_Example_VB.htm)

## Remarks

Depending on the [tolerance type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~Type.html), the tolerance minimum and maximum values might not be visible.

To:

- get the tolerance minimum value, use [IDimensionTolerance::GetMinValue2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetMinValue2.html).
- set the tolerance values, use [IDimensionTolerance::SetValues2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~SetValues2.html).

## See Also

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.html)

## Availability

SOLIDWORKS 2015 SP3, Revision Number 23.3
