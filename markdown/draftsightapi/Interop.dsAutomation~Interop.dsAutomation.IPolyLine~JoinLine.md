---
title: "JoinLine Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "JoinLine"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~JoinLine.html"
---

# JoinLine Method (IPolyLine)

Joins the specified line with this 2D PolyLine.

## Syntax

### Visual Basic

```vb
Function JoinLine( _
   ByVal Line As Line _
) As System.Boolean
```

### C#

```csharp
System.bool JoinLine(
   Line Line
)
```

### JScript

```
function JoinLine(
   Line : Line
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool JoinLine(
   Line* Line
)
```

### C++/CLI

```cpp
System.bool JoinLine(
   Line^ Line
)
```

### Parameters

- `Line`: [Line](Interop.dsAutomation~Interop.dsAutomation.ILine.html)

### Return Value

True if the Line joins the 2D PolyLine, false if not

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::JoinCircleArc Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~JoinCircleArc.html)
[IPolyLine::JoinPolyLine Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~JoinPolyLine.html)

## Availability

DraftSight V1R1.1
