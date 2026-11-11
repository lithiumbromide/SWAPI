---
title: "InsertArcByCenter2Points2 Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertArcByCenter2Points2"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertArcByCenter2Points2.html"
---

# InsertArcByCenter2Points2 Method (ISketchManager)

Constructs an Arc using the specified center, start, and end points.

## Syntax

### Visual Basic

```vb
Function InsertArcByCenter2Points2( _
   ByVal CenterPoint As MathPoint, _
   ByVal FirstPoint As MathPoint, _
   ByVal SecondPoint As MathPoint _
) As CircleArc
```

### C#

```csharp
CircleArc InsertArcByCenter2Points2(
   MathPoint CenterPoint,
   MathPoint FirstPoint,
   MathPoint SecondPoint
)
```

### JScript

```
function InsertArcByCenter2Points2(
   CenterPoint : MathPoint,
   FirstPoint : MathPoint,
   SecondPoint : MathPoint
) : CircleArc;
```

### Managed Extensions for C++

```
CircleArc* InsertArcByCenter2Points2(
   MathPoint* CenterPoint,
   MathPoint* FirstPoint,
   MathPoint* SecondPoint
)
```

### C++/CLI

```cpp
CircleArc^ InsertArcByCenter2Points2(
   MathPoint^ CenterPoint,
   MathPoint^ FirstPoint,
   MathPoint^ SecondPoint
)
```

### Parameters

- `CenterPoint`: Center [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) of the Arc
- `FirstPoint`: Start [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) of the Arc
- `SecondPoint`: End [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) of the Arc (see **Remarks**)

### Return Value

[Arc](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)

## Remarks

SecondPoint specifies the end angle; thus, the end point does not have to be same as SecondPoint.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertArc Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertArc.html)
[ISketchManager::InsertArcBy3Points Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertArcBy3Points.html)

## Availability

DraftSight V1R3.0
