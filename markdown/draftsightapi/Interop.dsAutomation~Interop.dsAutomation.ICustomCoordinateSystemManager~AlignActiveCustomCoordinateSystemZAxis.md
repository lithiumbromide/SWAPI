---
title: "AlignActiveCustomCoordinateSystemZAxis Method (ICustomCoordinateSystemManager)"
project: ""
interface: "ICustomCoordinateSystemManager"
member: "AlignActiveCustomCoordinateSystemZAxis"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~AlignActiveCustomCoordinateSystemZAxis.html"
---

# AlignActiveCustomCoordinateSystemZAxis Method (ICustomCoordinateSystemManager)

Aligns the active coordinate system's z axis in the specified direction with the specified origin.

## Syntax

### Visual Basic

```vb
Sub AlignActiveCustomCoordinateSystemZAxis( _
   ByVal OriginX As System.Double, _
   ByVal OriginY As System.Double, _
   ByVal OriginZ As System.Double, _
   ByVal DirectionX As System.Double, _
   ByVal DirectionY As System.Double, _
   ByVal DirectionZ As System.Double _
)
```

### C#

```csharp
void AlignActiveCustomCoordinateSystemZAxis(
   System.double OriginX,
   System.double OriginY,
   System.double OriginZ,
   System.double DirectionX,
   System.double DirectionY,
   System.double DirectionZ
)
```

### JScript

```
function AlignActiveCustomCoordinateSystemZAxis(
   OriginX : System.double,
   OriginY : System.double,
   OriginZ : System.double,
   DirectionX : System.double,
   DirectionY : System.double,
   DirectionZ : System.double
);
```

### Managed Extensions for C++

```
void AlignActiveCustomCoordinateSystemZAxis(
   System.double OriginX,
   System.double OriginY,
   System.double OriginZ,
   System.double DirectionX,
   System.double DirectionY,
   System.double DirectionZ
)
```

### C++/CLI

```cpp
void AlignActiveCustomCoordinateSystemZAxis(
   System.double OriginX,
   System.double OriginY,
   System.double OriginZ,
   System.double DirectionX,
   System.double DirectionY,
   System.double DirectionZ
)
```

### Parameters

- `OriginX`: x coordinate of the origin
- `OriginY`: y coordinate of the origin
- `OriginZ`: z coordinate of the origin
- `DirectionX`: x coordinate of the direction point
- `DirectionY`: y coordinate of the direction point
- `DirectionZ`: z coordinate of the direction point

## See Also

[ICustomCoordinateSystemManager Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager.html)
[ICustomCoordinateSystemManager Members](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager_members.html)
[ICustomCoordinateSystemManager::AlignActiveCustomCoordinateSystemByEntity Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~AlignActiveCustomCoordinateSystemByEntity.html)
[ICustomCoordinateSystemManager::AlignActiveCustomCoordinateSystemByView Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~AlignActiveCustomCoordinateSystemByView.html)
[ICustomCoordinateSystemManager::AlignActiveCustomCoordinateSystemXYPlane Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~AlignActiveCustomCoordinateSystemXYPlane.html)

## Availability

DraftSight V1R1.4
