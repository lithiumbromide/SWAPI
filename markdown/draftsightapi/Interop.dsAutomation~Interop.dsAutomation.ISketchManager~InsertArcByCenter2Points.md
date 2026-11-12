---
title: "InsertArcByCenter2Points Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertArcByCenter2Points"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertArcByCenter2Points.html"
---

# InsertArcByCenter2Points Method (ISketchManager)

Obsolete. Superseded by [ISketchManager::InsertArcByCenter2Points](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertArcByCenter2Points2.html).

## Syntax

### Visual Basic

```vb
Function InsertArcByCenter2Points( _
   ByVal CenterPointsDblArray As System.Object, _
   ByVal FirstPointsDblArray As System.Object, _
   ByVal SecondPointsDblArray As System.Object _
) As CircleArc
```

### C#

```csharp
CircleArc InsertArcByCenter2Points(
   System.object CenterPointsDblArray,
   System.object FirstPointsDblArray,
   System.object SecondPointsDblArray
)
```

### JScript

```
function InsertArcByCenter2Points(
   CenterPointsDblArray : System.Object,
   FirstPointsDblArray : System.Object,
   SecondPointsDblArray : System.Object
) : CircleArc;
```

### Managed Extensions for C++

```
CircleArc* InsertArcByCenter2Points(
   System.Object* CenterPointsDblArray,
   System.Object* FirstPointsDblArray,
   System.Object* SecondPointsDblArray
)
```

### C++/CLI

```cpp
CircleArc^ InsertArcByCenter2Points(
   System.Object^ CenterPointsDblArray,
   System.Object^ FirstPointsDblArray,
   System.Object^ SecondPointsDblArray
)
```

### Parameters

- `CenterPointsDblArray`: Array of doubles for the center point of the Arc
- `FirstPointsDblArray`: Array of doubles for the start point of the Arc
- `SecondPointsDblArray`: Array of doubles for the end point of the Arc

### Return Value

[Arc](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R2.0
