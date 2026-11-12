---
title: "ScalePoint Method (IMathPoint)"
project: ""
interface: "IMathPoint"
member: "ScalePoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathPoint~ScalePoint.html"
---

# ScalePoint Method (IMathPoint)

Scales this mathematical point by the specified scale factor about the specified mathematical center point.

## Syntax

### Visual Basic

```vb
Sub ScalePoint( _
   ByVal CenterPoint As MathPoint, _
   ByVal ScaleFactor As System.Double _
)
```

### C#

```csharp
void ScalePoint(
   MathPoint CenterPoint,
   System.double ScaleFactor
)
```

### JScript

```
function ScalePoint(
   CenterPoint : MathPoint,
   ScaleFactor : System.double
);
```

### Managed Extensions for C++

```
void ScalePoint(
   MathPoint* CenterPoint,
   System.double ScaleFactor
)
```

### C++/CLI

```cpp
void ScalePoint(
   MathPoint^ CenterPoint,
   System.double ScaleFactor
)
```

### Parameters

- `CenterPoint`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `ScaleFactor`: Factor by which to scale this mathematical point

## See Also

[IMathPoint Interface](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
[IMathPoint Members](Interop.dsAutomation~Interop.dsAutomation.IMathPoint_members.html)

## Availability

DraftSight V1R1.4
