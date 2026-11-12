---
title: "SetBulkTemperatureTimeCurve2 Method (ICWConvection)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWConvection"
member: "SetBulkTemperatureTimeCurve2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~SetBulkTemperatureTimeCurve2.html"
---

# SetBulkTemperatureTimeCurve2 Method (ICWConvection)

Sets the bulk temperature-time curve data.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBulkTemperatureTimeCurve2( _
   ByVal VarCurveData As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWConvection
Dim VarCurveData As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Boolean

value = instance.SetBulkTemperatureTimeCurve2(VarCurveData, ErrorCode)
```

### C#

```csharp
System.bool SetBulkTemperatureTimeCurve2(
   System.object VarCurveData,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.bool SetBulkTemperatureTimeCurve2(
   System.Object^ VarCurveData,
   [Out] System.int ErrorCode
)
```

### Parameters

- `VarCurveData`: Array of bulk temperature-time curve data (see **Remarks**)
- `ErrorCode`: Error as defined in [swsTimeCurveError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTimeCurveError_e.html)

### Return Value

-1 or true to use curve, 0 or false to not

## Remarks

Bulk temperature-time curve array:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- xi = time value at the `ith` data point
- yi = bulk temperature at time xi

## See Also

[ICWConvection Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection.html)
[ICWConvection Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
