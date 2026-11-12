---
title: "GetTimeCurve Method (ICWTemperature)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTemperature"
member: "GetTimeCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature~GetTimeCurve.html"
---

# GetTimeCurve Method (ICWTemperature)

Gets the time curve data for the temperature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTimeCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTemperature
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

Array of time curve data (see **Remarks**)

## VBA Syntax

See [CWTemperature::GetTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTemperature~GetTimeCurve.html).

## Remarks

Time curve data array:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi
- xi = time value at the `ith` data point
- yi = property value associated with time xi

## See Also

[ICWTemperature Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature.html)
[ICWTemperature Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature_members.html)
[ICWTemperature::SetTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature~SetTimeCurve.html)
[ICWTemperature::UseTimeCurve Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature~UseTimeCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
