---
title: "Decurve Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "Decurve"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Decurve.html"
---

# Decurve Method (IPolyLine)

Reverts the 2D PolyLine curve, created by [IPolyLine::Fit](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Fit.html) or [IPolyLine::Spline](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Spline.html), to its original vertices.

## Syntax

### Visual Basic

```vb
Function Decurve() As System.Boolean
```

### C#

```csharp
System.bool Decurve()
```

### JScript

```
function Decurve() : System.boolean;
```

### Managed Extensions for C++

```
System.bool Decurve();
```

### C++/CLI

```cpp
System.bool Decurve();
```

### Return Value

True if the 2D PolyLine curve reverts to its original vertices, false if not

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::Type Property](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Type.html)

## Availability

DraftSight V1R1.1
