---
title: "OffsetEntityByThroughPoint Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "OffsetEntityByThroughPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~OffsetEntityByThroughPoint.html"
---

# OffsetEntityByThroughPoint Method (ISketchManager)

Copies the specified entity through the specified point.

## Syntax

### Visual Basic

```vb
Function OffsetEntityByThroughPoint( _
   ByVal Obj As System.Object, _
   ByVal DeleteSourceEntity As System.Boolean, _
   ByVal Bothsides As System.Boolean, _
   ByVal ThroughPoint As MathPoint, _
   ByVal OffsetType As dsOffsetType_e _
) As System.Object
```

### C#

```csharp
System.object OffsetEntityByThroughPoint(
   System.object Obj,
   System.bool DeleteSourceEntity,
   System.bool Bothsides,
   MathPoint ThroughPoint,
   dsOffsetType_e OffsetType
)
```

### JScript

```
function OffsetEntityByThroughPoint(
   Obj : System.Object,
   DeleteSourceEntity : System.boolean,
   Bothsides : System.boolean,
   ThroughPoint : MathPoint,
   OffsetType : dsOffsetType_e
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* OffsetEntityByThroughPoint(
   System.Object* Obj,
   System.bool DeleteSourceEntity,
   System.bool Bothsides,
   MathPoint* ThroughPoint,
   dsOffsetType_e OffsetType
)
```

### C++/CLI

```cpp
System.Object^ OffsetEntityByThroughPoint(
   System.Object^ Obj,
   System.bool DeleteSourceEntity,
   System.bool Bothsides,
   MathPoint^ ThroughPoint,
   dsOffsetType_e OffsetType
)
```

### Parameters

- `Obj`: Source entity to offset
- `DeleteSourceEntity`: True to delete Obj after offset, false to not
- `Bothsides`: True to offset on both sides of Obj, false to not
- `ThroughPoint`: [MathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) to which to offset Obj; valid only if Bothsides is false
- `OffsetType`: Type of offset as defined in [dsOffsetType_e](Interop.dsAutomation~Interop.dsAutomation.dsOffsetType_e.html)

### Return Value

Entity

## Remarks

For more information, see the **Creating Offsets of Entities** topic in the DraftSight user-interface help.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::OffsetEntityByDistance Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~OffsetEntityByDistance.html)

## Availability

DraftSight 2021 SP0
