---
title: "GetTimeCurve Method (ICWGravity)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGravity"
member: "GetTimeCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~GetTimeCurve.html"
---

# GetTimeCurve Method (ICWGravity)

Gets the time curve data.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTimeCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGravity
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

See [CWGravity::GetTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGravity~GetTimeCurve.html).

## Remarks

Time curve data array:

**[** `n, x1, y1, x2, y2, x3, y3,...xn, yn` **]**

where:

- n = number of xi,yi pairs
- xi = time value at the `ith` data point
- yi = property value associated with time xi

Time curves are used to specify variation with respect to time in transient studies.

## See Also

[ICWGravity Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity.html)
[ICWGravity Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity_members.html)
[ICWGravity::SetTimeCurve Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~SetTimeCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
