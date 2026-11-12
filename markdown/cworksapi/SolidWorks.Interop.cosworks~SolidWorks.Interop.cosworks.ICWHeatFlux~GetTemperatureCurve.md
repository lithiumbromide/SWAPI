---
title: "GetTemperatureCurve Method (ICWHeatFlux)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: "GetTemperatureCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~GetTemperatureCurve.html"
---

# GetTemperatureCurve Method (ICWHeatFlux)

Gets the temperature curve data for heat flux.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTemperatureCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatFlux
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

See [CWHeatFlux::GetTemperatureCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatFlux~GetTemperatureCurve.html).

## Remarks

Temperature curve data:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- xi = temperature value at the `ith` data point
- yi = property value associated with temperature xi

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)
[ICWHeatFlux::SetTemperatureCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~SetTemperatureCurve.html)
[ICWHeatFlux::UseTemperatureCurve Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~UseTemperatureCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
