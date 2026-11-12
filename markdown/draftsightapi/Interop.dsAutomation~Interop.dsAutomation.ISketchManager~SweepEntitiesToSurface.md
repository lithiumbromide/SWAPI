---
title: "SweepEntitiesToSurface Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "SweepEntitiesToSurface"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SweepEntitiesToSurface.html"
---

# SweepEntitiesToSurface Method (ISketchManager)

Creates a swept surface using the specified 2D entities, open sweep path, base point, scale, banking, and twist angle.

## Syntax

### Visual Basic

```vb
Function SweepEntitiesToSurface( _
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
System.object SweepEntitiesToSurface(
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
function SweepEntitiesToSurface(
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
System.Object* SweepEntitiesToSurface(
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
System.Object^ SweepEntitiesToSurface(
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
- `Obj`: Array of non-closed path entities
- `Alignment`: True to align the sweep objects perpendicular to the path before sweep, false to not
- `Bank`: True to allow banking for a non-planar sweep path, false to not
- `UseBasePoint`: True to specify a base point for the entities to be swept, false to not
- `BasePointX`: X-coordinate of base point; valid only if UseBasePoint is true
- `BasePointY`: Y-coordinate of base point; valid only if UseBasePoint is true
- `BasePointZ`: Z-coordinate of base point; valid only if UseBasePoint is true
- `Scale`: Scale factor for the entities to be swept
- `TwistAngle`: Angle in radians of twist for the entities to be swept along the total length of the path

### Return Value

Array of [ISweptSurface](Interop.dsAutomation~Interop.dsAutomation.ISweptSurface.html)s

## Examples

[Sweeping Entities (C#)](Sweeping_Entities_Example_CSharp.htm)
[Sweeping Entities (VB.NET)](Sweeping_Entities_Example_VBNET.htm)
[Sweeping Entities (VBA)](Sweeping_Entities_Example_VBA.htm)
[Sweeping Entities (JS)](Sweeping_Entities_Example_JS.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::SweepEntitiesToSolid Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~SweepEntitiesToSolid.html)

## Availability

DraftSight 2020 SP0
