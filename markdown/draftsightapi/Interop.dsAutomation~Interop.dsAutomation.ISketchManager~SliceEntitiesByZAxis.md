---
title: "SliceEntitiesByZAxis Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "SliceEntitiesByZAxis"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SliceEntitiesByZAxis.html"
---

# SliceEntitiesByZAxis Method (ISketchManager)

Slices the specified 3D entities using the section plane that contains the specified point and whose normal contain the specified point on the Z-axis.

## Syntax

### Visual Basic

```vb
Function SliceEntitiesByZAxis( _
   ByVal EntitiesArray As System.Object, _
   ByVal PointOnSectionPlane As MathPoint, _
   ByVal PointOnZAxis As MathPoint, _
   ByVal KeepBothSides As System.Boolean, _
   ByVal PointOnDesiredSide As MathPoint, _
   ByRef ObjectsArray As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool SliceEntitiesByZAxis(
   System.object EntitiesArray,
   MathPoint PointOnSectionPlane,
   MathPoint PointOnZAxis,
   System.bool KeepBothSides,
   MathPoint PointOnDesiredSide,
   out System.object ObjectsArray
)
```

### JScript

```
function SliceEntitiesByZAxis(
   EntitiesArray : System.Object,
   PointOnSectionPlane : MathPoint,
   PointOnZAxis : MathPoint,
   KeepBothSides : System.boolean,
   PointOnDesiredSide : MathPoint,
   ObjectsArray : System.Object
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool SliceEntitiesByZAxis(
   System.Object* EntitiesArray,
   MathPoint* PointOnSectionPlane,
   MathPoint* PointOnZAxis,
   System.bool KeepBothSides,
   MathPoint* PointOnDesiredSide,
   [PARAMFLAG::Out] System.Object* ObjectsArray
)
```

### C++/CLI

```cpp
System.bool SliceEntitiesByZAxis(
   System.Object^ EntitiesArray,
   MathPoint^ PointOnSectionPlane,
   MathPoint^ PointOnZAxis,
   System.bool KeepBothSides,
   MathPoint^ PointOnDesiredSide,
   [Out] System.Object^ ObjectsArray
)
```

### Parameters

- `EntitiesArray`: Array of 3D entities
- `PointOnSectionPlane`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `PointOnZAxis`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `KeepBothSides`: True to keep both sides, false to discard the undesired part
- `PointOnDesiredSide`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html); valid only if KeepBothSides is false
- `ObjectsArray`: Array of [ISolid3D](Interop.dsAutomation~Interop.dsAutomation.ISolid3D.html) sliced objects

### Return Value

True if successful, false if not

## Examples

[Slicing Entities (C#)](Slicing_Entities_Example_CSharp.htm)
[Slicing Entities (VBA)](Slicing_Entities_Example_VBA.htm)
[Slicing Entities (VB.NET)](Slicing_Entities_Example_VBNET.htm)
[Slicing Entities (JS)](Slicing_Entities_Example_JS.htm)

## Remarks

See the **3D Modeling > Modifying Solids > Slicing 3D Solids** topic in the DraftSight (Premium & Enterprise Plus) user-interface help.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::SliceEntitiesBy3Points Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SliceEntitiesBy3Points.html)
[ISketchManager::SliceEntitiesByPlanarEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SliceEntitiesByPlanarEntity.html)
[ISketchManager::SliceEntitiesBySurface Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SliceEntitiesBySurface.html)
[ISketchManager::SliceEntitiesByView Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SliceEntitiesByView.html)
[ISketchManager::SliceEntitiesByXY Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SliceEntitiesByXY.html)
[ISketchManager::SliceEntitiesByYZ Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SliceEntitiesByYZ.html)
[ISketchManager::SliceEntitiesByZX Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SliceEntitiesByZX.html)

## Availability

DraftSight 2020 SP0
