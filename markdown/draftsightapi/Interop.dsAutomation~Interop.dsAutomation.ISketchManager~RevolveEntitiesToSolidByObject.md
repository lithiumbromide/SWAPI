---
title: "RevolveEntitiesToSolidByObject Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "RevolveEntitiesToSolidByObject"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RevolveEntitiesToSolidByObject.html"
---

# RevolveEntitiesToSolidByObject Method (ISketchManager)

Revolves the specified entities into a solid using the specified axis and angle of revolution.

## Syntax

### Visual Basic

```vb
Function RevolveEntitiesToSolidByObject( _
   ByVal EntitiesArray As System.Object, _
   ByVal RevolveObjectArray As System.Object, _
   ByVal RevolutionAngle As System.Double _
) As System.Object
```

### C#

```csharp
System.object RevolveEntitiesToSolidByObject(
   System.object EntitiesArray,
   System.object RevolveObjectArray,
   System.double RevolutionAngle
)
```

### JScript

```
function RevolveEntitiesToSolidByObject(
   EntitiesArray : System.Object,
   RevolveObjectArray : System.Object,
   RevolutionAngle : System.double
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* RevolveEntitiesToSolidByObject(
   System.Object* EntitiesArray,
   System.Object* RevolveObjectArray,
   System.double RevolutionAngle
)
```

### C++/CLI

```cpp
System.Object^ RevolveEntitiesToSolidByObject(
   System.Object^ EntitiesArray,
   System.Object^ RevolveObjectArray,
   System.double RevolutionAngle
)
```

### Parameters

- `EntitiesArray`: Array of entities to revolve
- `RevolveObjectArray`: Array of one entity that determines the axis of revolution
- `RevolutionAngle`: Angle of revolution in radians; default is 6.283 (360 degrees)

### Return Value

Array of [IRevolve](Interop.dsAutomation~Interop.dsAutomation.IRevolve.html)s

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
[ISketchManager::RevolveEntitiesToSolidByXAxis Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RevolveEntitiesToSolidByXAxis.html)
[ISketchManager::RevolveEntitiesToSurfaceByAxis Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RevolveEntitiesToSurfaceByAxis.html)
[ISketchManager::RevolveEntitiesToSurfaceByObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RevolveEntitiesToSurfaceByObject.html)
[ISketchManager::RevolveEntitiesToSurfaceByXAxis Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RevolveEntitiesToSurfaceByXAxis.html)

## Availability

DraftSight 2020 SP0
