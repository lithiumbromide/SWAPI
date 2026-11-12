---
title: "OffsetEntityByDistance Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "OffsetEntityByDistance"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~OffsetEntityByDistance.html"
---

# OffsetEntityByDistance Method (ISketchManager)

Copies the specified entity to a location at the specified distance.

## Syntax

### Visual Basic

```vb
Function OffsetEntityByDistance( _
   ByVal Obj As System.Object, _
   ByVal DeleteSourceEntity As System.Boolean, _
   ByVal Distance As System.Double, _
   ByVal Bothsides As System.Boolean, _
   ByVal OneSidePoint As MathPoint, _
   ByVal OffsetType As dsOffsetType_e _
) As System.Object
```

### C#

```csharp
System.object OffsetEntityByDistance(
   System.object Obj,
   System.bool DeleteSourceEntity,
   System.double Distance,
   System.bool Bothsides,
   MathPoint OneSidePoint,
   dsOffsetType_e OffsetType
)
```

### JScript

```
function OffsetEntityByDistance(
   Obj : System.Object,
   DeleteSourceEntity : System.boolean,
   Distance : System.double,
   Bothsides : System.boolean,
   OneSidePoint : MathPoint,
   OffsetType : dsOffsetType_e
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* OffsetEntityByDistance(
   System.Object* Obj,
   System.bool DeleteSourceEntity,
   System.double Distance,
   System.bool Bothsides,
   MathPoint* OneSidePoint,
   dsOffsetType_e OffsetType
)
```

### C++/CLI

```cpp
System.Object^ OffsetEntityByDistance(
   System.Object^ Obj,
   System.bool DeleteSourceEntity,
   System.double Distance,
   System.bool Bothsides,
   MathPoint^ OneSidePoint,
   dsOffsetType_e OffsetType
)
```

### Parameters

- `Obj`: Source entity to offset
- `DeleteSourceEntity`: True to delete the Obj after offset, false to not
- `Distance`: Distance by which to offset Obj
- `Bothsides`: True to offset on both sides of Obj, false to not
- `OneSidePoint`: [MathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on the side of Obj from which to offset; valid only if Bothsides is false
- `OffsetType`: Type of offset as defined in [dsOffsetType_e](Interop.dsAutomation~Interop.dsAutomation.dsOffsetType_e.html)

### Return Value

Entity

## Remarks

For more information, see the **Creating Offsets of Entities** topic in the DraftSight user-interface help.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::OffsetEntityByThroughPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~OffsetEntityByThroughPoint.html)

## Availability

DraftSight 2021 SP0
