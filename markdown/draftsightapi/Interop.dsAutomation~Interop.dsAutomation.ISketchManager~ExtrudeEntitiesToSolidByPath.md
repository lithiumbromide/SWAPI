---
title: "ExtrudeEntitiesToSolidByPath Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "ExtrudeEntitiesToSolidByPath"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtrudeEntitiesToSolidByPath.html"
---

# ExtrudeEntitiesToSolidByPath Method (ISketchManager)

Extrudes the specified entities into a solid using the specified path entity and the specified angle of taper.

## Syntax

### Visual Basic

```vb
Sub ExtrudeEntitiesToSolidByPath( _
   ByVal EntitiesArray As System.Object, _
   ByVal ExtrudePathArray As System.Object, _
   ByVal TaperAngle As System.Double, _
   ByRef SweepArray As System.Object _
)
```

### C#

```csharp
void ExtrudeEntitiesToSolidByPath(
   System.object EntitiesArray,
   System.object ExtrudePathArray,
   System.double TaperAngle,
   out System.object SweepArray
)
```

### JScript

```
function ExtrudeEntitiesToSolidByPath(
   EntitiesArray : System.Object,
   ExtrudePathArray : System.Object,
   TaperAngle : System.double,
   SweepArray : System.Object
);
```

### Managed Extensions for C++

```
void ExtrudeEntitiesToSolidByPath(
   System.Object* EntitiesArray,
   System.Object* ExtrudePathArray,
   System.double TaperAngle,
   [PARAMFLAG::Out] System.Object* SweepArray
)
```

### C++/CLI

```cpp
void ExtrudeEntitiesToSolidByPath(
   System.Object^ EntitiesArray,
   System.Object^ ExtrudePathArray,
   System.double TaperAngle,
   [Out] System.Object^ SweepArray
)
```

### Parameters

- `EntitiesArray`: Array of closed entities to extrude
- `ExtrudePathArray`: Array of one path entity
- `TaperAngle`: -1.5708 <= Angle of taper in radians <= 1.5708
- `SweepArray`: Array of [ISweep](Interop.dsAutomation~Interop.dsAutomation.ISweep.html)s

## Examples

[Extruding Entities (C#)](Extruding_Entities_Example_CSharp.htm)
[Extruding Entities (VBA)](Extruding_Entities_Example_VBA.htm)
[Extruding Entities (VB.NET)](Extruding_Entities_Example_VBNET.htm)
[Extruding Entities (JS)](Extruding_Entities_Example_JS.htm)

## Remarks

See the **3D Modeling > Creating Solids > Creating 3D Solids by Sweeping 2D Entities Along a Path** topic in the DraftSight (Premium & Enterprise Plus) user-interface help.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::ExtrudeEntitiesToSolidByHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtrudeEntitiesToSolidByHeight.html)
[ISketchManager::ExtrudeEntitiesToSurfaceByHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtrudeEntitiesToSurfaceByHeight.html)
[ISketchManager::ExtrudeEntitiesToSurfaceByPath Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtrudeEntitiesToSurfaceByPath.html)

## Availability

DraftSight 2020 SP0
