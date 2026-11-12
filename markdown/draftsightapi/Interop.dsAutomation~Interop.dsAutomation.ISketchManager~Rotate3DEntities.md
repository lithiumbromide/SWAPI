---
title: "Rotate3DEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "Rotate3DEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~Rotate3DEntities.html"
---

# Rotate3DEntities Method (ISketchManager)

Rotates the specified entities in 3D space.

## Syntax

### Visual Basic

```vb
Sub Rotate3DEntities( _
   ByVal FirstAxisThroughPoint As MathPoint, _
   ByVal SecondAxisThroughPoint As MathPoint, _
   ByVal Angle As System.Double, _
   ByVal EntitiesArray As System.Object _
)
```

### C#

```csharp
void Rotate3DEntities(
   MathPoint FirstAxisThroughPoint,
   MathPoint SecondAxisThroughPoint,
   System.double Angle,
   System.object EntitiesArray
)
```

### JScript

```
function Rotate3DEntities(
   FirstAxisThroughPoint : MathPoint,
   SecondAxisThroughPoint : MathPoint,
   Angle : System.double,
   EntitiesArray : System.Object
);
```

### Managed Extensions for C++

```
void Rotate3DEntities(
   MathPoint* FirstAxisThroughPoint,
   MathPoint* SecondAxisThroughPoint,
   System.double Angle,
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
void Rotate3DEntities(
   MathPoint^ FirstAxisThroughPoint,
   MathPoint^ SecondAxisThroughPoint,
   System.double Angle,
   System.Object^ EntitiesArray
)
```

### Parameters

- `FirstAxisThroughPoint`: First [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) that defines the axis of rotation
- `SecondAxisThroughPoint`: Second [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) that defines the axis of rotation
- `Angle`: Angle of rotation in radians
- `EntitiesArray`: Array of entities to rotate in 3D space

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::RotateEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RotateEntities.html)

## Availability

DraftSight V1R4.0
