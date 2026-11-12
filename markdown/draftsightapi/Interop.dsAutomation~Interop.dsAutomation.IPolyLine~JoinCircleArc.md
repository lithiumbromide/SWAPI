---
title: "JoinCircleArc Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "JoinCircleArc"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~JoinCircleArc.html"
---

# JoinCircleArc Method (IPolyLine)

Joins the specified Arc with this 2D PolyLine.

## Syntax

### Visual Basic

```vb
Function JoinCircleArc( _
   ByVal Arc As CircleArc _
) As System.Boolean
```

### C#

```csharp
System.bool JoinCircleArc(
   CircleArc Arc
)
```

### JScript

```
function JoinCircleArc(
   Arc : CircleArc
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool JoinCircleArc(
   CircleArc* Arc
)
```

### C++/CLI

```cpp
System.bool JoinCircleArc(
   CircleArc^ Arc
)
```

### Parameters

- `Arc`: [CircleArc](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)

### Return Value

True if the Arc joins the 2D PolyLine, false if not

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::JoinLine Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~JoinLine.html)
[IPolyLine::JoinPolyLine Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~JoinPolyLine.html)

## Availability

DraftSight V1R1.1
