---
title: "GetTimeCurve Method (ICWHeatFlux)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: "GetTimeCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~GetTimeCurve.html"
---

# GetTimeCurve Method (ICWHeatFlux)

Gets the time curve data for heat flux.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTimeCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatFlux
Dim value As System.Object

value = instance.GetTimeCurve()
```

### C#

```csharp
System.object GetTimeCurve()
```

### C++/CLI

```cpp
System.Object^ GetTimeCurve();
```

### Return Value

Array of time curve data (see Remarks)

## VBA Syntax

See [CWHeatFlux::GetTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatFlux~GetTimeCurve.html).

## Remarks

Time curve data:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- xi = time value at the `ith` data point
- yi = property value associated with time xi

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)
[ICWHeatFlux::SetTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~SetTimeCurve.html)
[ICWHeatFlux::UseTimeCurve Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~UseTimeCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
