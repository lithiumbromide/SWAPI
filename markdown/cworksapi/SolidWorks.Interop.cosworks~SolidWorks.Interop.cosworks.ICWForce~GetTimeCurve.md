---
title: "GetTimeCurve Method (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "GetTimeCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetTimeCurve.html"
---

# GetTimeCurve Method (ICWForce)

Gets the time curve data for this time-dependent force in a dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTimeCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
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

See [CWForce::GetTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~GetTimeCurve.html).

## Remarks

Time curve data array:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- xi = time value at the `ith` data point
- yi = property value associated with time xi

Time curves are used to specify feature variation with respect to time in linear and nonlinear dynamic studies.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)
[ICWForce::SetTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetTimeCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
