---
title: "SetBulkTemperatureTimeCurve Method (ICWConvection)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWConvection"
member: "SetBulkTemperatureTimeCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~SetBulkTemperatureTimeCurve.html"
---

# SetBulkTemperatureTimeCurve Method (ICWConvection)

Obsolete. Superseded by [ICWConvection::SetBulkTemperatureTimeCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~SetBulkTemperatureTimeCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBulkTemperatureTimeCurve( _
   ByVal VarCurveData As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWConvection
Dim VarCurveData As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Integer

value = instance.SetBulkTemperatureTimeCurve(VarCurveData, ErrorCode)
```

### C#

```csharp
System.int SetBulkTemperatureTimeCurve(
   System.object VarCurveData,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.int SetBulkTemperatureTimeCurve(
   System.Object^ VarCurveData,
   [Out] System.int ErrorCode
)
```

### Parameters

- `VarCurveData`: Array of bulk temperature-time curve data (see **Remarks**)
- `ErrorCode`: Error as defined in [swsTimeCurveError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTimeCurveError_e.html)

### Return Value

1 to use curve, 0 to not

## VBA Syntax

See [CWConvection::SetBulkTemperatureTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWConvection~SetBulkTemperatureTimeCurve.html).

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
[ICWConvection::GetBulkTemperatureTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~GetBulkTemperatureTimeCurve.html)
[ICWConvection::UseBulkTemperatureTimeCurve Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~UseBulkTemperatureTimeCurve.html)
[ICWConvection::BulkAmbientTemperature Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~BulkAmbientTemperature.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
