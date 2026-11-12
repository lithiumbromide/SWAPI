---
title: "GetTemperatureCurve Method (ICWHeatPower)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatPower"
member: "GetTemperatureCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~GetTemperatureCurve.html"
---

# GetTemperatureCurve Method (ICWHeatPower)

Gets the temperature curve data for heat power.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTemperatureCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatPower
Dim value As System.Object

value = instance.GetTemperatureCurve()
```

### C#

```csharp
System.object GetTemperatureCurve()
```

### C++/CLI

```cpp
System.Object^ GetTemperatureCurve();
```

### Return Value

Array of temperature curve data (see **Remarks**)

## VBA Syntax

See [CWHeatPower::GetTemperatureCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatPower~GetTemperatureCurve.html).

## Remarks

Temperature curve data:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- xi = temperature value at the `ith` data point
- yi = property value associated with temperature xi

## See Also

[ICWHeatPower Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html)
[ICWHeatPower Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower_members.html)
[ICWHeatPower::SetTemperatureCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~SetTemperatureCurve.html)
[ICWHeatPower::UseTemperatureCurve Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~UseTemperatureCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
