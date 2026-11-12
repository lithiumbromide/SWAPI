---
title: "InsertCircleBy3Points Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertCircleBy3Points"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertCircleBy3Points.html"
---

# InsertCircleBy3Points Method (ISketchManager)

Constructs a Circle using the specified three points.

## Syntax

### Visual Basic

```vb
Function InsertCircleBy3Points( _
   ByVal FirstPoint As MathPoint, _
   ByVal SecondPoint As MathPoint, _
   ByVal ThirdPoint As MathPoint _
) As Circle
```

### C#

```csharp
Circle InsertCircleBy3Points(
   MathPoint FirstPoint,
   MathPoint SecondPoint,
   MathPoint ThirdPoint
)
```

### JScript

```
function InsertCircleBy3Points(
   FirstPoint : MathPoint,
   SecondPoint : MathPoint,
   ThirdPoint : MathPoint
) : Circle;
```

### Managed Extensions for C++

```
Circle* InsertCircleBy3Points(
   MathPoint* FirstPoint,
   MathPoint* SecondPoint,
   MathPoint* ThirdPoint
)
```

### C++/CLI

```cpp
Circle^ InsertCircleBy3Points(
   MathPoint^ FirstPoint,
   MathPoint^ SecondPoint,
   MathPoint^ ThirdPoint
)
```

### Parameters

- `FirstPoint`: First [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `SecondPoint`: Second [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `ThirdPoint`: Third [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)

### Return Value

[Circle](Interop.dsAutomation~Interop.dsAutomation.ICircle.html)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertCircle Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertCircle.html)
[ISketchManager::InsertCircleByDiameter Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertCircleByDiameter.html)

## Availability

DraftSight V1R3.0
