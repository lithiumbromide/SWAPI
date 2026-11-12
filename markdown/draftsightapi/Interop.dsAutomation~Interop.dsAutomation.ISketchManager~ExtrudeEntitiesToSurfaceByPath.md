---
title: "ExtrudeEntitiesToSurfaceByPath Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "ExtrudeEntitiesToSurfaceByPath"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtrudeEntitiesToSurfaceByPath.html"
---

# ExtrudeEntitiesToSurfaceByPath Method (ISketchManager)

Extrudes the specified entities into a surface using the specified path entity, the specified height, and the specified angle of taper.

## Syntax

### Visual Basic

```vb
Sub ExtrudeEntitiesToSurfaceByPath( _
   ByVal EntitiesArray As System.Object, _
   ByVal ExtrudePathArray As System.Object, _
   ByVal TaperAngle As System.Double, _
   ByRef SweptSurfaceArray As System.Object _
)
```

### C#

```csharp
void ExtrudeEntitiesToSurfaceByPath(
   System.object EntitiesArray,
   System.object ExtrudePathArray,
   System.double TaperAngle,
   out System.object SweptSurfaceArray
)
```

### JScript

```
function ExtrudeEntitiesToSurfaceByPath(
   EntitiesArray : System.Object,
   ExtrudePathArray : System.Object,
   TaperAngle : System.double,
   SweptSurfaceArray : System.Object
);
```

### Managed Extensions for C++

```
void ExtrudeEntitiesToSurfaceByPath(
   System.Object* EntitiesArray,
   System.Object* ExtrudePathArray,
   System.double TaperAngle,
   [PARAMFLAG::Out] System.Object* SweptSurfaceArray
)
```

### C++/CLI

```cpp
void ExtrudeEntitiesToSurfaceByPath(
   System.Object^ EntitiesArray,
   System.Object^ ExtrudePathArray,
   System.double TaperAngle,
   [Out] System.Object^ SweptSurfaceArray
)
```

### Parameters

- `EntitiesArray`: Array of entities to extrude
- `ExtrudePathArray`: Array of one path entity
- `TaperAngle`: -1.5708 <= Angle of taper in radians <= 1.5708
- `SweptSurfaceArray`: Array of [ISweptSurface](Interop.dsAutomation~Interop.dsAutomation.ISweptSurface.html)s

## Examples

[Extruding Entities (C#)](Extruding_Entities_Example_CSharp.htm)
[Extruding Entities (VB.NET)](Extruding_Entities_Example_VBNET.htm)
[Extruding Entities (VBA)](Extruding_Entities_Example_VBA.htm)
[Extruding Entities (JS)](Extruding_Entities_Example_JS.htm)

## Remarks

See the **3D Modeling > Creating Solids > Creating 3D Solids by Sweeping 2D Entities Along a Path** topic in the DraftSight (Premium & Enterprise Plus) user-interface help.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::ExtrudeEntitiesToSolidByHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtrudeEntitiesToSolidByHeight.html)
[ISketchManager::ExtrudeEntitiesToSolidByPath Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtrudeEntitiesToSolidByPath.html)
[ISketchManager::ExtrudeEntitiesToSurfaceByHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtrudeEntitiesToSurfaceByHeight.html)

## Availability

DraftSight 2020 SP0
