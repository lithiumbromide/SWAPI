---
title: "GetTemperatureCurve Method (ICWConvection)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWConvection"
member: "GetTemperatureCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~GetTemperatureCurve.html"
---

# GetTemperatureCurve Method (ICWConvection)

Gets the temperature curve data for convection.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTemperatureCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWConvection
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

Array of temperature curve data for convection (see Remarks)

## VBA Syntax

See [CWConvection::GetTemperatureCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWConvection~GetTemperatureCurve.html).

## Remarks

Temperature curve array:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- xi = temperature value at the `ith` data point
- yi = property value associated with temperature xi

## See Also

[ICWConvection Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection.html)
[ICWConvection Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection_members.html)
[ICWConvection::UseTemperatureCurve Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~UseTemperatureCurve.html)
[ICWConvection::SetTemperatureCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~SetTemperatureCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
