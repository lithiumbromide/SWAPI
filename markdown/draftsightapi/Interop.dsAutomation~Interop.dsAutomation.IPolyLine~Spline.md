---
title: "Spline Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "Spline"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Spline.html"
---

# Spline Method (IPolyLine)

Turns the 2D PolyLine into a curve using the vertices as control points.

## Syntax

### Visual Basic

```vb
Function Spline() As System.Boolean
```

### C#

```csharp
System.bool Spline()
```

### JScript

```
function Spline() : System.boolean;
```

### Managed Extensions for C++

```
System.bool Spline();
```

### C++/CLI

```cpp
System.bool Spline();
```

### Return Value

True if the 2D PolyLine is turned into a curve, false if not

## Remarks

Using this method turns the 2D PolyLine into a curve, but it usually does not cause the curve to pass through the vertices. Using [IPolyLine::Fit](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Fit.html) ensures that the curve passes through all vertices of the 2d PolyLine.

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::Decurve Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Decurve.html)
[IPolyLine::Type Property](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Type.html)
[IPolyLine::Split Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Split.html)
[IPolyLine::Straighten Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Straighten.html)

## Availability

DraftSight V1R1.1
