---
title: "AlignActiveCustomCoordinateSystemByEntity Method (ICustomCoordinateSystemManager)"
project: ""
interface: "ICustomCoordinateSystemManager"
member: "AlignActiveCustomCoordinateSystemByEntity"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~AlignActiveCustomCoordinateSystemByEntity.html"
---

# AlignActiveCustomCoordinateSystemByEntity Method (ICustomCoordinateSystemManager)

Aligns the active coordinate system with the specified entity.

## Syntax

### Visual Basic

```vb
Sub AlignActiveCustomCoordinateSystemByEntity( _
   ByVal Entity As System.Object, _
   ByVal PointOnEntityDblArray As System.Object _
)
```

### C#

```csharp
void AlignActiveCustomCoordinateSystemByEntity(
   System.object Entity,
   System.object PointOnEntityDblArray
)
```

### JScript

```
function AlignActiveCustomCoordinateSystemByEntity(
   Entity : System.Object,
   PointOnEntityDblArray : System.Object
);
```

### Managed Extensions for C++

```
void AlignActiveCustomCoordinateSystemByEntity(
   System.Object* Entity,
   System.Object* PointOnEntityDblArray
)
```

### C++/CLI

```cpp
void AlignActiveCustomCoordinateSystemByEntity(
   System.Object^ Entity,
   System.Object^ PointOnEntityDblArray
)
```

### Parameters

- `Entity`: Entity with which to align the coordinate system
- `PointOnEntityDblArray`: Array of doubles of x, y, and z coordinates of a point on Entity with which to align the coordinate system

## Examples

[Manage Custom Coordinate Systems (JavaScript)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_JS.htm)
[Manage Custom Coordinate Systems (VB.NET)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_VBNET.htm)
[Manage Custom Coordinate Systems (C#)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_CSharp.htm)
[Manage Custom Coordinate Systems (VBA)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_VBA.htm)

## See Also

[ICustomCoordinateSystemManager Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager.html)
[ICustomCoordinateSystemManager Members](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager_members.html)
[ICustomCoordinateSystemManager::AlignActiveCustomCoordinateSystemByView Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~AlignActiveCustomCoordinateSystemByView.html)
[ICustomCoordinateSystemManager::AlignActiveCustomCoordinateSystemZAxis Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~AlignActiveCustomCoordinateSystemZAxis.html)
[ICustomCoordinateSystemManager::AlignActiveCustomCoordinateSystemXYPlane Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~AlignActiveCustomCoordinateSystemXYPlane.html)

## Availability

DraftSight V1R1.4
