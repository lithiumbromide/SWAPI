---
title: "ExtrudeEntitiesToSurfaceByHeight Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "ExtrudeEntitiesToSurfaceByHeight"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtrudeEntitiesToSurfaceByHeight.html"
---

# ExtrudeEntitiesToSurfaceByHeight Method (ISketchManager)

Extrudes the specified entities into a surface with the specified height and the specified angle of taper.

## Syntax

### Visual Basic

```vb
Sub ExtrudeEntitiesToSurfaceByHeight( _
   ByVal EntitiesArray As System.Object, _
   ByVal Height As System.Double, _
   ByVal TaperAngle As System.Double, _
   ByRef ExtrudedSurfaceArray As System.Object _
)
```

### C#

```csharp
void ExtrudeEntitiesToSurfaceByHeight(
   System.object EntitiesArray,
   System.double Height,
   System.double TaperAngle,
   out System.object ExtrudedSurfaceArray
)
```

### JScript

```
function ExtrudeEntitiesToSurfaceByHeight(
   EntitiesArray : System.Object,
   Height : System.double,
   TaperAngle : System.double,
   ExtrudedSurfaceArray : System.Object
);
```

### Managed Extensions for C++

```
void ExtrudeEntitiesToSurfaceByHeight(
   System.Object* EntitiesArray,
   System.double Height,
   System.double TaperAngle,
   [PARAMFLAG::Out] System.Object* ExtrudedSurfaceArray
)
```

### C++/CLI

```cpp
void ExtrudeEntitiesToSurfaceByHeight(
   System.Object^ EntitiesArray,
   System.double Height,
   System.double TaperAngle,
   [Out] System.Object^ ExtrudedSurfaceArray
)
```

### Parameters

- `EntitiesArray`: Array of entities to extrude
- `Height`: Height of the extrusion
- `TaperAngle`: -1.5708 <= Angle of taper in radians <= 1.5708
- `ExtrudedSurfaceArray`: Array of [IExtrudedSurface](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface.html)s

## Examples

[Extruding Entities (C#)](Extruding_Entities_Example_CSharp.htm)
[Slicing Entities (C#)](Slicing_Entities_Example_CSharp.htm)
[Extruding Entities (VB.NET)](Extruding_Entities_Example_VBNET.htm)
[Extruding Entities (VBA)](Extruding_Entities_Example_VBA.htm)
[Extruding Entities (JS)](Extruding_Entities_Example_JS.htm)

## Remarks

See the **3D Modeling > Creating Solids > Creating 3D Solids and 3D Surfaces by Extruding 2D Entities** topic in the DraftSight (Premium & Enterprise Plus) user-interface help.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::ExtrudeEntitiesToSolidByHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtrudeEntitiesToSolidByHeight.html)
[ISketchManager::ExtrudeEntitiesToSolidByPath Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtrudeEntitiesToSolidByPath.html)
[ISketchManager::ExtrudeEntitiesToSurfaceByPath Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtrudeEntitiesToSurfaceByPath.html)

## Availability

DraftSight 2020 SP0
