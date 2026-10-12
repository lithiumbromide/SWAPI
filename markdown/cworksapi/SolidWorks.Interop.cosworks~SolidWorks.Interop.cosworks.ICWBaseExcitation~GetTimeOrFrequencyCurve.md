---
title: "GetTimeOrFrequencyCurve Method (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "GetTimeOrFrequencyCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~GetTimeOrFrequencyCurve.html"
---

# GetTimeOrFrequencyCurve Method (ICWBaseExcitation)

Gets the variation of base excitation with frequency or time.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTimeOrFrequencyCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation
Dim value As System.Object

value = instance.GetTimeOrFrequencyCurve()
```

### C#

```csharp
System.object GetTimeOrFrequencyCurve()
```

### C++/CLI

```cpp
System.Object^ GetTimeOrFrequencyCurve();
```

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [CWBaseExcitation::GetTimeOrFrequencyCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBaseExcitation~GetTimeOrFrequencyCurve.html).

## Examples

[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)

## Remarks

Array of linear or curve data:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where for modal time history and nonlinear dynamic studies:

- n = number of xi,yi pairs
- xi = time value at the `ith` data point
- yi = excitation value associated with time xi

and for harmonic and random vibration dynamic studies:

- n = number of xi,yi pairs
- xi = frequency value at the `ith` data point
- yi = excitation value associated with frequency xi

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[ICWBaseExcitation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html)
[ICWBaseExcitation::SetTimeOrFrequencyCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~SetTimeOrFrequencyCurve.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
