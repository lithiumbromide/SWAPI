---
title: "RevolveEntitiesToSurfaceByAxis Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "RevolveEntitiesToSurfaceByAxis"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RevolveEntitiesToSurfaceByAxis.html"
---

# RevolveEntitiesToSurfaceByAxis Method (ISketchManager)

Revolves the specified entities into a surface using the specified axis and angle of revolution.

## Syntax

### Visual Basic

```vb
Function RevolveEntitiesToSurfaceByAxis( _
   ByVal EntitiesArray As System.Object, _
   ByVal StartX As System.Double, _
   ByVal StartY As System.Double, _
   ByVal StartZ As System.Double, _
   ByVal EndX As System.Double, _
   ByVal EndY As System.Double, _
   ByVal EndZ As System.Double, _
   ByVal RevolutionAngle As System.Double _
) As System.Object
```

### C#

```csharp
System.object RevolveEntitiesToSurfaceByAxis(
   System.object EntitiesArray,
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double EndX,
   System.double EndY,
   System.double EndZ,
   System.double RevolutionAngle
)
```

### JScript

```
function RevolveEntitiesToSurfaceByAxis(
   EntitiesArray : System.Object,
   StartX : System.double,
   StartY : System.double,
   StartZ : System.double,
   EndX : System.double,
   EndY : System.double,
   EndZ : System.double,
   RevolutionAngle : System.double
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* RevolveEntitiesToSurfaceByAxis(
   System.Object* EntitiesArray,
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double EndX,
   System.double EndY,
   System.double EndZ,
   System.double RevolutionAngle
)
```

### C++/CLI

```cpp
System.Object^ RevolveEntitiesToSurfaceByAxis(
   System.Object^ EntitiesArray,
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double EndX,
   System.double EndY,
   System.double EndZ,
   System.double RevolutionAngle
)
```

### Parameters

- `EntitiesArray`: Array of entities
- `StartX`: X-coordinate of axis start point
- `StartY`: Y-coordinate of axis start point
- `StartZ`: Z-coordinate of axis start point
- `EndX`: X-coordinate of axis end point
- `EndY`: Y-coordinate of axis end point
- `EndZ`: Z-coordinate of axis end point
- `RevolutionAngle`: Angle of revolution in radians; default is 6.283 (360 degrees)

### Return Value

Array of [IRevolvedSurface](Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface.html)s

## Examples

[Revolving Entities (C#)](Revolving_Entities_Example_CSharp.htm)
[Revolving Entities (VB.NET)](Revolving_Entities_Example_VBNET.htm)
[Revolving Entities (VBA)](Revolving_Entities_Example_VBA.htm)
[Revolving Entities (JS)](Revolving_Entities_Example_JS.htm)

## Remarks

See the **3D Modeling > Creating Solids > Creating 3D Solids by Revolving 2D Entities Around an Axis** topic in the DraftSight (Premium & Enterprise Plus) user-interface help.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::RevolveEntitiesToSolidByAxis Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RevolveEntitiesToSolidByAxis.html)
[ISketchManager::RevolveEntitiesToSolidByObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RevolveEntitiesToSolidByObject.html)
[ISketchManager::RevolveEntitiesToSolidByXAxis Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RevolveEntitiesToSolidByXAxis.html)
[ISketchManager::RevolveEntitiesToSurfaceByObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RevolveEntitiesToSurfaceByObject.html)
[ISketchManager::RevolveEntitiesToSurfaceByXAxis Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RevolveEntitiesToSurfaceByXAxis.html)

## Availability

DraftSight 2020 SP0
