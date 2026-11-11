---
title: "Fit Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "Fit"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Fit.html"
---

# Fit Method (IPolyLine)

Turns the 2D PolyLine into a smooth curve consisting of Arcs joining each pair of vertices.

## Syntax

### Visual Basic

```vb
Function Fit() As System.Boolean
```

### C#

```csharp
System.bool Fit()
```

### JScript

```
function Fit() : System.boolean;
```

### Managed Extensions for C++

```
System.bool Fit();
```

### C++/CLI

```cpp
System.bool Fit();
```

### Return Value

True if the 2D PolyLine is turned into a smooth curve, false if not

## Remarks

Using this method ensures that the curve passes through all vertices of the 2D PolyLine. Using the [IPolyLine::Spline](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Spline.html) method also turns the 2D PolyLine into a curve, but it usually does not cause the curve to pass through the vertices.

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::Decurve Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Decurve.html)
[IPolyLine::Type Property](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Type.html)
[IPolyLine::Split Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Split.html)
[IPolyLine::Straighten Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Straighten.html)

## Availability

DraftSight V1R1.1
