---
title: "LoftEntitiesToSolidByPath Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "LoftEntitiesToSolidByPath"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~LoftEntitiesToSolidByPath.html"
---

# LoftEntitiesToSolidByPath Method (ISketchManager)

Creates a new Loft using the specified closed entities, path curves, draft angles, and draft curvatures.

## Syntax

### Visual Basic

```vb
Function LoftEntitiesToSolidByPath( _
   ByVal EntitiesArray As System.Object, _
   ByVal CrossSectionOnly As System.Boolean, _
   ByVal PathArray As System.Object, _
   ByVal LoftSurfaceOption As dsLoftSurfaceNormalOption_e, _
   ByVal LoftOption As dsLoftedSurfaceNormalOption_e, _
   ByVal DraftStartAngle As System.Double, _
   ByVal DraftEndAngle As System.Double, _
   ByVal DraftStartCurvature As System.Double, _
   ByVal DraftEndCurvature As System.Double _
) As Loft
```

### C#

```csharp
Loft LoftEntitiesToSolidByPath(
   System.object EntitiesArray,
   System.bool CrossSectionOnly,
   System.object PathArray,
   dsLoftSurfaceNormalOption_e LoftSurfaceOption,
   dsLoftedSurfaceNormalOption_e LoftOption,
   System.double DraftStartAngle,
   System.double DraftEndAngle,
   System.double DraftStartCurvature,
   System.double DraftEndCurvature
)
```

### JScript

```
function LoftEntitiesToSolidByPath(
   EntitiesArray : System.Object,
   CrossSectionOnly : System.boolean,
   PathArray : System.Object,
   LoftSurfaceOption : dsLoftSurfaceNormalOption_e,
   LoftOption : dsLoftedSurfaceNormalOption_e,
   DraftStartAngle : System.double,
   DraftEndAngle : System.double,
   DraftStartCurvature : System.double,
   DraftEndCurvature : System.double
) : Loft;
```

### Managed Extensions for C++

```
Loft* LoftEntitiesToSolidByPath(
   System.Object* EntitiesArray,
   System.bool CrossSectionOnly,
   System.Object* PathArray,
   dsLoftSurfaceNormalOption_e LoftSurfaceOption,
   dsLoftedSurfaceNormalOption_e LoftOption,
   System.double DraftStartAngle,
   System.double DraftEndAngle,
   System.double DraftStartCurvature,
   System.double DraftEndCurvature
)
```

### C++/CLI

```cpp
Loft^ LoftEntitiesToSolidByPath(
   System.Object^ EntitiesArray,
   System.bool CrossSectionOnly,
   System.Object^ PathArray,
   dsLoftSurfaceNormalOption_e LoftSurfaceOption,
   dsLoftedSurfaceNormalOption_e LoftOption,
   System.double DraftStartAngle,
   System.double DraftEndAngle,
   System.double DraftStartCurvature,
   System.double DraftEndCurvature
)
```

### Parameters

- `EntitiesArray`: Array of closed entities
- `CrossSectionOnly`: True to only use cross sections defined by arcs, lines, polylines, or polygons, false to also use a path curve that intersects each cross section
- `PathArray`: Array of one path curve that intersects each cross section to shape the solid; valid only if CrossSectionOnly is false
- `LoftSurfaceOption`: Loft surfacing option as defined in [dsLoftSurfaceNormalOption_e](Interop.dsAutomation~Interop.dsAutomation.dsLoftSurfaceNormalOption_e.html)
- `LoftOption`: Loft option as defined in [dsLoftedSurfaceNormalOption_e](Interop.dsAutomation~Interop.dsAutomation.dsLoftedSurfaceNormalOption_e.html) only if LoftSurfaceOption is dsLoftSurfaceNormalOption_NormalTo
- `DraftStartAngle`: Starting draft angle in radians; valid only if LoftSurfaceOption is dsLoftSurfaceNormalOpion_DraftAngles
- `DraftEndAngle`: Ending draft angle in radians; valid only if LoftSurfaceOption is dsLoftSurfaceNormalOpion_DraftAngles
- `DraftStartCurvature`: Starting draft curvature; valid only if LoftSurfaceOption is dsLoftSurfaceNormalOpion_DraftAngles
- `DraftEndCurvature`: Ending draft curvature; valid only if LoftSurfaceOption is dsLoftSurfaceNormalOpion_DraftAngles

### Return Value

[ILoft](Interop.dsAutomation~Interop.dsAutomation.ILoft.html)

## Examples

[Lofting Entities (C#)](Lofting_Entities_Example_CSharp.htm)
[Lofting Entities (VB.NET)](Lofting_Entities_Example_VBNET.htm)
[Lofting Entities (VBA)](Lofting_Entities_Example_VBA.htm)
[Lofting Entities (JS)](Lofting_Entities_Example_JS.htm)

## Remarks

See the **3D Modeling > Creating Solids > Creating 3D Solids by Lofting Between 2D Entities** topic in the DraftSight (Premium & Enterprise Plus) user-interface help.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::LoftEntitiesToSolidByGuides Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~LoftEntitiesToSolidByGuides.html)
[ISketchManager::LoftEntitiesToSurfaceByGuides Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~LoftEntitiesToSurfaceByGuides.html)
[ISketchManager::LoftEntitiesToSurfaceByPath Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~LoftEntitiesToSurfaceByPath.html)

## Availability

DraftSight 2020 SP0
