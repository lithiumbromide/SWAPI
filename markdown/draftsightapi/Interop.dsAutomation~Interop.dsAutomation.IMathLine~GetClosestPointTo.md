---
title: "GetClosestPointTo Method (IMathLine)"
project: ""
interface: "IMathLine"
member: "GetClosestPointTo"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathLine~GetClosestPointTo.html"
---

# GetClosestPointTo Method (IMathLine)

Gets the point on the mathematical line that is closest to the specified point.

## Syntax

### Visual Basic

```vb
Function GetClosestPointTo( _
   ByVal Point As MathPoint _
) As MathPoint
```

### C#

```csharp
MathPoint GetClosestPointTo(
   MathPoint Point
)
```

### JScript

```
function GetClosestPointTo(
   Point : MathPoint
) : MathPoint;
```

### Managed Extensions for C++

```
MathPoint* GetClosestPointTo(
   MathPoint* Point
)
```

### C++/CLI

```cpp
MathPoint^ GetClosestPointTo(
   MathPoint^ Point
)
```

### Parameters

- `Point`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)

### Return Value

[Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on the mathematical line that is closest to the specified Point

## See Also

[IMathLine Interface](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html)
[IMathLine Members](Interop.dsAutomation~Interop.dsAutomation.IMathLine_members.html)
[IMathLine::GetClosestPointToCircArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~GetClosestPointToCircArc.html)
[IMathLine::GetClosestPointToEllipArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~GetClosestPointToEllipArc.html)
[IMathLine::GetClosestPointToLinearObject Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~GetClosestPointToLinearObject.html)
[IMathLine::EndPoint Property ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~EndPoint.html)
[IMathLine::StartPoint Property ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~StartPoint.html)

## Availability

DraftSight V1R5.0
