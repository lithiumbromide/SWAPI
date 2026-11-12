---
title: "ExtrudeEntitiesToSolidByHeight Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "ExtrudeEntitiesToSolidByHeight"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtrudeEntitiesToSolidByHeight.html"
---

# ExtrudeEntitiesToSolidByHeight Method (ISketchManager)

Extrudes the specified entities into a solid with the specified height and the specified angle of taper.

## Syntax

### Visual Basic

```vb
Sub ExtrudeEntitiesToSolidByHeight( _
   ByVal EntitiesArray As System.Object, _
   ByVal Height As System.Double, _
   ByVal TaperAngle As System.Double, _
   ByRef ExtrusionArray As System.Object _
)
```

### C#

```csharp
void ExtrudeEntitiesToSolidByHeight(
   System.object EntitiesArray,
   System.double Height,
   System.double TaperAngle,
   out System.object ExtrusionArray
)
```

### JScript

```
function ExtrudeEntitiesToSolidByHeight(
   EntitiesArray : System.Object,
   Height : System.double,
   TaperAngle : System.double,
   ExtrusionArray : System.Object
);
```

### Managed Extensions for C++

```
void ExtrudeEntitiesToSolidByHeight(
   System.Object* EntitiesArray,
   System.double Height,
   System.double TaperAngle,
   [PARAMFLAG::Out] System.Object* ExtrusionArray
)
```

### C++/CLI

```cpp
void ExtrudeEntitiesToSolidByHeight(
   System.Object^ EntitiesArray,
   System.double Height,
   System.double TaperAngle,
   [Out] System.Object^ ExtrusionArray
)
```

### Parameters

- `EntitiesArray`: Array of closed entities to extrude
- `Height`: Height of the extrusion
- `TaperAngle`: -1.5708 <= Angle of taper in radians <= 1.5708
- `ExtrusionArray`: Array of [IExtrusion](Interop.dsAutomation~Interop.dsAutomation.IExtrusion.html)s

## Examples

[Unifying, Subtracting, and Intersecting Entities (C#)](Unifying_Subtracting_and_Intersecting_Entities_Example_CSharp.htm)
[Cross-sectioning Entities (C#)](Cross-sectioning_Entities_Example_CSharp.htm)
[Creating Flat Representations of 3D Entities (C#)](Creating_Flat_Representations_of_3D_Entities_Example_CSharp.htm)
[Slicing Entities (C#)](Slicing_Entities_Example_CSharp.htm)
[Extruding Entities (VBA)](Extruding_Entities_Example_VBA.htm)
[Extruding Entities (VB.NET)](Extruding_Entities_Example_VBNET.htm)
[Extruding Entities (C#)](Extruding_Entities_Example_CSharp.htm)
[Extruding Entities (JS)](Extruding_Entities_Example_JS.htm)

## Remarks

See the **3D Modeling > Creating Solids > Creating 3D Solids and 3D Surfaces by Extruding 2D Entities** topic in the DraftSight (Premium & Enterprise Plus) user-interface help.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::ExtrudeEntitiesToSolidByPath Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtrudeEntitiesToSolidByPath.html)
[ISketchManager::ExtrudeEntitiesToSurfaceByHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtrudeEntitiesToSurfaceByHeight.html)
[ISketchManager::ExtrudeEntitiesToSurfaceByPath Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ExtrudeEntitiesToSurfaceByPath.html)

## Availability

DraftSight 2020 SP0
