---
title: "GetBulkTemperatureTimeCurve Method (ICWConvection)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWConvection"
member: "GetBulkTemperatureTimeCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~GetBulkTemperatureTimeCurve.html"
---

# GetBulkTemperatureTimeCurve Method (ICWConvection)

Gets the bulk temperature versus time curve data for convection.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBulkTemperatureTimeCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWConvection
Dim value As System.Object

value = instance.GetBulkTemperatureTimeCurve()
```

### C#

```csharp
System.object GetBulkTemperatureTimeCurve()
```

### C++/CLI

```cpp
System.Object^ GetBulkTemperatureTimeCurve();
```

### Return Value

Array of bulk temperature-time curve (see Remarks)

## VBA Syntax

See [CWConvection::GetBulkTemperatureTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWConvection~GetBulkTemperatureTimeCurve.html).

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
[ICWConvection::SetBulkTemperatureTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~SetBulkTemperatureTimeCurve.html)
[ICWConvection::UseBulkTemperatureTimeCurve Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~UseBulkTemperatureTimeCurve.html)
[ICWConvection::BulkAmbientTemperature Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~BulkAmbientTemperature.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
