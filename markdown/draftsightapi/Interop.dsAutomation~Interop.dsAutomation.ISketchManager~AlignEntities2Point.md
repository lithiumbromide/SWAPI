---
title: "AlignEntities2Point Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "AlignEntities2Point"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~AlignEntities2Point.html"
---

# AlignEntities2Point Method (ISketchManager)

Aligns the specified entities, rotating them based on the current coordinate system, using two pairs of points.

## Syntax

### Visual Basic

```vb
Sub AlignEntities2Point( _
   ByVal FirstSourcePoint As MathPoint, _
   ByVal FirstDestinationPoint As MathPoint, _
   ByVal SecondSourcePoint As MathPoint, _
   ByVal SecondDestinationPoint As MathPoint, _
   ByVal ScaleEntities As System.Boolean, _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void AlignEntities2Point(
   MathPoint FirstSourcePoint,
   MathPoint FirstDestinationPoint,
   MathPoint SecondSourcePoint,
   MathPoint SecondDestinationPoint,
   System.bool ScaleEntities,
   System.object EntitiesArray
)
```

### JScript

```
function AlignEntities2Point(
   FirstSourcePoint : MathPoint,
   FirstDestinationPoint : MathPoint,
   SecondSourcePoint : MathPoint,
   SecondDestinationPoint : MathPoint,
   ScaleEntities : System.boolean,
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void AlignEntities2Point(
   MathPoint* FirstSourcePoint,
   MathPoint* FirstDestinationPoint,
   MathPoint* SecondSourcePoint,
   MathPoint* SecondDestinationPoint,
   System.bool ScaleEntities,
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void AlignEntities2Point(
   MathPoint^ FirstSourcePoint,
   MathPoint^ FirstDestinationPoint,
   MathPoint^ SecondSourcePoint,
   MathPoint^ SecondDestinationPoint,
   System.bool ScaleEntities,
   System.Object^ EntitiesArray
)
```

### Parameters

- `FirstSourcePoint`: [First source point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) for the movement vector
- `FirstDestinationPoint`: [First destination point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) for the movement vector
- `SecondSourcePoint`: [Second source point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) for the rotation angle
- `SecondDestinationPoint`: [Second destination point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) for the rotation angle
- `ScaleEntities`: True to scale the specified entities if the distance between both source points and both destination points is not identical, false to not
- `EntitiesArray`: Array of entities to align and rotate

## Remarks

Specifying two pairs of points moves the entities and rotates them based on the current coordinate system.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::Align3DEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~Align3DEntities.html)
[ISketchManager::AlignEntities1Point Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~AlignEntities1Point.html)
[ISketchManager::AlignEntities3Point Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~AlignEntities3Point.html)

## Availability

DraftSight V1R4.0
