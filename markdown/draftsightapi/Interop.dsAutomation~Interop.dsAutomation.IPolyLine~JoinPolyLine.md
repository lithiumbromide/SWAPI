---
title: "JoinPolyLine Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "JoinPolyLine"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~JoinPolyLine.html"
---

# JoinPolyLine Method (IPolyLine)

Joins the specified 2D PolyLine with this 2D PolyLine.

## Syntax

### Visual Basic

```vb
Function JoinPolyLine( _
   ByVal PolyLine As PolyLine _
) As System.Boolean
```

### C#

```csharp
System.bool JoinPolyLine(
   PolyLine PolyLine
)
```

### JScript

```
function JoinPolyLine(
   PolyLine : PolyLine
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool JoinPolyLine(
   PolyLine* PolyLine
)
```

### C++/CLI

```cpp
System.bool JoinPolyLine(
   PolyLine^ PolyLine
)
```

### Parameters

- `PolyLine`: [2D PolyLine](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)

### Return Value

True if the specified 2D PolyLine is joined to this 2D PolyLine, false if not

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::JoinCircleArc Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~JoinCircleArc.html)
[IPolyLine::JoinLine Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~JoinLine.html)

## Availability

DraftSight V1R1.1
