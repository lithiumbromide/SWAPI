---
title: "SweepEntitiesToSolid Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "SweepEntitiesToSolid"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SweepEntitiesToSolid.html"
---

# SweepEntitiesToSolid Method (ISketchManager)

Creates a swept solid using the specified 2D entities, closed sweep path, base point, scale, banking, and twist angle.

## Syntax

### Visual Basic

```vb
Function SweepEntitiesToSolid( _
   ByVal EntitiesArray As System.Object, _
   ByVal Obj As System.Object, _
   ByVal Alignment As System.Boolean, _
   ByVal Bank As System.Boolean, _
   ByVal UseBasePoint As System.Boolean, _
   ByVal BasePointX As System.Double, _
   ByVal BasePointY As System.Double, _
   ByVal BasePointZ As System.Double, _
   ByVal Scale As System.Double, _
   ByVal TwistAngle As System.Double _
) As System.Object
```

### C#

```csharp
System.object SweepEntitiesToSolid(
   System.object EntitiesArray,
   System.object Obj,
   System.bool Alignment,
   System.bool Bank,
   System.bool UseBasePoint,
   System.double BasePointX,
   System.double BasePointY,
   System.double BasePointZ,
   System.double Scale,
   System.double TwistAngle
)
```

### JScript

```
function SweepEntitiesToSolid(
   EntitiesArray : System.Object,
   Obj : System.Object,
   Alignment : System.boolean,
   Bank : System.boolean,
   UseBasePoint : System.boolean,
   BasePointX : System.double,
   BasePointY : System.double,
   BasePointZ : System.double,
   Scale : System.double,
   TwistAngle : System.double
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* SweepEntitiesToSolid(
   System.Object* EntitiesArray,
   System.Object* Obj,
   System.bool Alignment,
   System.bool Bank,
   System.bool UseBasePoint,
   System.double BasePointX,
   System.double BasePointY,
   System.double BasePointZ,
   System.double Scale,
   System.double TwistAngle
)
```

### C++/CLI

```cpp
System.Object^ SweepEntitiesToSolid(
   System.Object^ EntitiesArray,
   System.Object^ Obj,
   System.bool Alignment,
   System.bool Bank,
   System.bool UseBasePoint,
   System.double BasePointX,
   System.double BasePointY,
   System.double BasePointZ,
   System.double Scale,
   System.double TwistAngle
)
```

### Parameters

- `EntitiesArray`: Array of 2D entities to sweep
- `Obj`: Array of closed path entities
- `Alignment`: True to align the sweep objects perpendicular to the path before sweep, false to not
- `Bank`: True to allow banking for a non-planar sweep path, false to not
- `UseBasePoint`: True to specify a base point for the entities to be swept, false to not
- `BasePointX`: X-coordinate of base point; valid only if UseBasePoint is true
- `BasePointY`: Y-coordinate of base point; valid only if UseBasePoint is true
- `BasePointZ`: Z-coordinate of base point; valid only if UseBasePoint is true
- `Scale`: Scale factor for the entities to be swept
- `TwistAngle`: Angle in radians of twist for the entities to be swept along the total length of the path

### Return Value

Array of [ISweep](Interop.dsAutomation~Interop.dsAutomation.ISweep.html)s

## Examples

[Sweeping Entities (C#)](Sweeping_Entities_Example_CSharp.htm)
[Sweeping Entities (VB.NET)](Sweeping_Entities_Example_VBNET.htm)
[Sweeping Entities (VBA)](Sweeping_Entities_Example_VBA.htm)
[Sweeping Entities (JS)](Sweeping_Entities_Example_JS.htm)

## Remarks

See the **3D Modeling > Creating Solids > Creating 3D Solids by Sweeping 2D Entities Along a Path** topic in the DraftSight (Premium & Enterprise Plus) user-interface help.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::SweepEntitiesToSurface Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SweepEntitiesToSurface.html)

## Availability

DraftSight 2020 SP0
