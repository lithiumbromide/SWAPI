---
title: "RevolveEntitiesToSolidByXAxis Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "RevolveEntitiesToSolidByXAxis"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RevolveEntitiesToSolidByXAxis.html"
---

# RevolveEntitiesToSolidByXAxis Method (ISketchManager)

Revolves the specified entities into a solid using the specified X-axis and angle of revolution.

## Syntax

### Visual Basic

```vb
Function RevolveEntitiesToSolidByXAxis( _
   ByVal EntitiesArray As System.Object, _
   ByVal RevolutionAngle As System.Double, _
   ByVal XAxis As System.Boolean _
) As System.Object
```

### C#

```csharp
System.object RevolveEntitiesToSolidByXAxis(
   System.object EntitiesArray,
   System.double RevolutionAngle,
   System.bool XAxis
)
```

### JScript

```
function RevolveEntitiesToSolidByXAxis(
   EntitiesArray : System.Object,
   RevolutionAngle : System.double,
   XAxis : System.boolean
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* RevolveEntitiesToSolidByXAxis(
   System.Object* EntitiesArray,
   System.double RevolutionAngle,
   System.bool XAxis
)
```

### C++/CLI

```cpp
System.Object^ RevolveEntitiesToSolidByXAxis(
   System.Object^ EntitiesArray,
   System.double RevolutionAngle,
   System.bool XAxis
)
```

### Parameters

- `EntitiesArray`: Array of entities
- `RevolutionAngle`: Angle of revolution in radians; default is 6.283 (360 degrees)
- `XAxis`: True if X-axis of revolution, false if Y-axis of revolution

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
[ISketchManager::RevolveEntitiesToSolidByObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RevolveEntitiesToSolidByObject.html)
[ISketchManager::RevolveEntitiesToSurfaceByAxis Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RevolveEntitiesToSurfaceByAxis.html)
[ISketchManager::RevolveEntitiesToSurfaceByObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RevolveEntitiesToSurfaceByObject.html)
[ISketchManager::RevolveEntitiesToSurfaceByXAxis Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~RevolveEntitiesToSurfaceByXAxis.html)

## Availability

DraftSight 2020 SP0
