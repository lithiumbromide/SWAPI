---
title: "GetTemperatureCurve Method (ICWRadiation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRadiation"
member: "GetTemperatureCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~GetTemperatureCurve.html"
---

# GetTemperatureCurve Method (ICWRadiation)

Gets the temperature curve data for this radiation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTemperatureCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRadiation
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

See [CWRadiation::GetTemperatureCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRadiation~GetTemperatureCurve.html).

## Remarks

Temperature curve data array:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- xi = temperature value at the `ith` data point
- yi = property value associated with temperature xi

## See Also

[ICWRadiation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html)
[ICWRadiation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation_members.html)
[ICWRadiation::SetTemperatureCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~SetTemperatureCurve.html)
[ICWRadiation::UseTemperatureCurve Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~UseTemperatureCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
