---
title: "GetTimeCurve Method (ICWCentriFugalForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCentriFugalForce"
member: "GetTimeCurve"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~GetTimeCurve.html"
---

# GetTimeCurve Method (ICWCentriFugalForce)

Gets the time curve data.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTimeCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCentriFugalForce
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

Array of curve data (see Remarks)

## VBA Syntax

See [CWCentriFugalForce::GetTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCentriFugalForce~GetTimeCurve.html).

## Remarks

Array of curve data:

**[** `n, x1, y1, x2, y2, x3, y3,...xn,` `yn`**]**

where:

- n = number of xi,yi pairs
- xi = time value at the `ith` data point
- yi = property value associated with time xi

Time curves are used to specify feature variation with time for transient studies.

## See Also

[ICWCentriFugalForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce.html)
[ICWCentriFugalForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce_members.html)
[ICWCentriFugalForce::SetTimeCurve Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~SetTimeCurve.html)
[ICWCentriFugalForce::UseTimeCurve Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~UseTimeCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
