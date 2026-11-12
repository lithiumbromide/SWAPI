---
title: "GetClosestPointToLinearObject Method (IMathLine)"
project: ""
interface: "IMathLine"
member: "GetClosestPointToLinearObject"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathLine~GetClosestPointToLinearObject.html"
---

# GetClosestPointToLinearObject Method (IMathLine)

Gets the point on the mathematical line that is closest to the specified linear object, and the gets point on the specified linear object that is closest to the mathematical line.

## Syntax

### Visual Basic

```vb
Function GetClosestPointToLinearObject( _
   ByVal LinearObject As MathLine, _
   ByRef PointOnLinearObject As MathPoint _
) As MathPoint
```

### C#

```csharp
MathPoint GetClosestPointToLinearObject(
   MathLine LinearObject,
   out MathPoint PointOnLinearObject
)
```

### JScript

```
function GetClosestPointToLinearObject(
   LinearObject : MathLine,
   PointOnLinearObject : MathPoint
) : MathPoint;
```

### Managed Extensions for C++

```
MathPoint* GetClosestPointToLinearObject(
   MathLine* LinearObject,
   [PARAMFLAG::Out] MathPoint* PointOnLinearObject
)
```

### C++/CLI

```cpp
MathPoint^ GetClosestPointToLinearObject(
   MathLine^ LinearObject,
   [Out] MathPoint^ PointOnLinearObject
)
```

### Parameters

- `LinearObject`: [Linear object](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html)
- `PointOnLinearObject`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on LinearObject that is closest to the mathematical line

### Return Value

[Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on the mathematical line that is closest to LinearObject

## See Also

[IMathLine Interface](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html)
[IMathLine Members](Interop.dsAutomation~Interop.dsAutomation.IMathLine_members.html)
[IMathLine::GetClosestPointTo Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~GetClosestPointTo.html)
[IMathLine::GetClosestPointToCircArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~GetClosestPointToCircArc.html)
[IMathLine::GetClosestPointToEllipArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~GetClosestPointToEllipArc.html)
[IMathLine::EndPoint Property ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~EndPoint.html)
[IMathLine::StartPoint Property ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~StartPoint.html)

## Availability

DraftSight V1R5.0
