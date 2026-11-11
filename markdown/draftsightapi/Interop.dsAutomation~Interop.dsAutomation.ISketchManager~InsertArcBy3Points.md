---
title: "InsertArcBy3Points Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertArcBy3Points"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertArcBy3Points.html"
---

# InsertArcBy3Points Method (ISketchManager)

Constructs an Arc using the specified three points.

## Syntax

### Visual Basic

```vb
Function InsertArcBy3Points( _
   ByVal FirstPoint As MathPoint, _
   ByVal SecondPoint As MathPoint, _
   ByVal ThirdPoint As MathPoint _
) As CircleArc
```

### C#

```csharp
CircleArc InsertArcBy3Points(
   MathPoint FirstPoint,
   MathPoint SecondPoint,
   MathPoint ThirdPoint
)
```

### JScript

```
function InsertArcBy3Points(
   FirstPoint : MathPoint,
   SecondPoint : MathPoint,
   ThirdPoint : MathPoint
) : CircleArc;
```

### Managed Extensions for C++

```
CircleArc* InsertArcBy3Points(
   MathPoint* FirstPoint,
   MathPoint* SecondPoint,
   MathPoint* ThirdPoint
)
```

### C++/CLI

```cpp
CircleArc^ InsertArcBy3Points(
   MathPoint^ FirstPoint,
   MathPoint^ SecondPoint,
   MathPoint^ ThirdPoint
)
```

### Parameters

- `FirstPoint`: First [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) for the Arc
- `SecondPoint`: Second [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) for the Arc
- `ThirdPoint`: Third [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) for the Arc

### Return Value

[Arc](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertArc Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertArc.html)
[ISketchManager::InsertArcByCenter2Points2 Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertArcByCenter2Points2.html)

## Availability

DraftSight V1R3.0
