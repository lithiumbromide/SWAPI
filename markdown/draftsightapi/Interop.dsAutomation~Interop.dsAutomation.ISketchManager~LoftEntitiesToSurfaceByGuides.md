---
title: "LoftEntitiesToSurfaceByGuides Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "LoftEntitiesToSurfaceByGuides"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~LoftEntitiesToSurfaceByGuides.html"
---

# LoftEntitiesToSurfaceByGuides Method (ISketchManager)

Creates a new lofted surface using the specified entities, profile guide lines, draft angles, and draft curvatures.

## Syntax

### Visual Basic

```vb
Function LoftEntitiesToSurfaceByGuides( _
   ByVal EntitiesArray As System.Object, _
   ByVal CrossSectionOnly As System.Boolean, _
   ByVal GuidesArray As System.Object, _
   ByVal LoftSurfaceOption As dsLoftSurfaceNormalOption_e, _
   ByVal LoftOption As dsLoftedSurfaceNormalOption_e, _
   ByVal DraftStartAngle As System.Double, _
   ByVal DraftEndAngle As System.Double, _
   ByVal DraftStartCurvature As System.Double, _
   ByVal DraftEndCurvature As System.Double _
) As LoftedSurface
```

### C#

```csharp
LoftedSurface LoftEntitiesToSurfaceByGuides(
   System.object EntitiesArray,
   System.bool CrossSectionOnly,
   System.object GuidesArray,
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
function LoftEntitiesToSurfaceByGuides(
   EntitiesArray : System.Object,
   CrossSectionOnly : System.boolean,
   GuidesArray : System.Object,
   LoftSurfaceOption : dsLoftSurfaceNormalOption_e,
   LoftOption : dsLoftedSurfaceNormalOption_e,
   DraftStartAngle : System.double,
   DraftEndAngle : System.double,
   DraftStartCurvature : System.double,
   DraftEndCurvature : System.double
) : LoftedSurface;
```

### Managed Extensions for C++

```
LoftedSurface* LoftEntitiesToSurfaceByGuides(
   System.Object* EntitiesArray,
   System.bool CrossSectionOnly,
   System.Object* GuidesArray,
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
LoftedSurface^ LoftEntitiesToSurfaceByGuides(
   System.Object^ EntitiesArray,
   System.bool CrossSectionOnly,
   System.Object^ GuidesArray,
   dsLoftSurfaceNormalOption_e LoftSurfaceOption,
   dsLoftedSurfaceNormalOption_e LoftOption,
   System.double DraftStartAngle,
   System.double DraftEndAngle,
   System.double DraftStartCurvature,
   System.double DraftEndCurvature
)
```

### Parameters

- `EntitiesArray`: Array of non-closed entities
- `CrossSectionOnly`: True to only use cross sections defined by arcs, lines, polylines, or polygons, false to also use guide lines defined by multiple entities that intersect each cross section
- `GuidesArray`: Array of guide lines that intersect each cross section to shape the surface; valid only if CrossSectionOnly is false
- `LoftSurfaceOption`: Loft surfacing option as defined in [dsLoftSurfaceNormalOption_e](Interop.dsAutomation~Interop.dsAutomation.dsLoftSurfaceNormalOption_e.html)
- `LoftOption`: Loft option as defined in [dsLoftedSurfaceNormalOption_e](Interop.dsAutomation~Interop.dsAutomation.dsLoftedSurfaceNormalOption_e.html) only if LoftSurfaceOption is dsLoftSurfaceNormalOption_NormalTo
- `DraftStartAngle`: Starting draft angle in radians; valid only if LoftSurfaceOption is dsLoftSurfaceNormalOpion_DraftAngles
- `DraftEndAngle`: Ending draft angle in radians; valid only if LoftSurfaceOption is dsLoftSurfaceNormalOpion_DraftAngles
- `DraftStartCurvature`: Starting draft curvature; valid only if LoftSurfaceOption is dsLoftSurfaceNormalOpion_DraftAngles
- `DraftEndCurvature`: Ending draft curvature; valid only if LoftSurfaceOption is dsLoftSurfaceNormalOpion_DraftAngles

### Return Value

[ILoftedSurface](Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface.html)

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
[ISketchManager::LoftEntitiesToSolidByPath Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~LoftEntitiesToSolidByPath.html)
[ISketchManager::LoftEntitiesToSurfaceByPath Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~LoftEntitiesToSurfaceByPath.html)

## Availability

DraftSight 2020 SP0
