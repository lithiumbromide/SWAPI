---
title: "SetActiveCustomCoordinateSystemOrigin Method (ICustomCoordinateSystemManager)"
project: ""
interface: "ICustomCoordinateSystemManager"
member: "SetActiveCustomCoordinateSystemOrigin"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~SetActiveCustomCoordinateSystemOrigin.html"
---

# SetActiveCustomCoordinateSystemOrigin Method (ICustomCoordinateSystemManager)

Sets the origin of the active coordinate system.

## Syntax

### Visual Basic

```vb
Sub SetActiveCustomCoordinateSystemOrigin( _
   ByVal OriginX As System.Double, _
   ByVal OriginY As System.Double, _
   ByVal OriginZ As System.Double _
)
```

### C#

```csharp
void SetActiveCustomCoordinateSystemOrigin(
   System.double OriginX,
   System.double OriginY,
   System.double OriginZ
)
```

### JScript

```
function SetActiveCustomCoordinateSystemOrigin(
   OriginX : System.double,
   OriginY : System.double,
   OriginZ : System.double
);
```

### Managed Extensions for C++

```
void SetActiveCustomCoordinateSystemOrigin(
   System.double OriginX,
   System.double OriginY,
   System.double OriginZ
)
```

### C++/CLI

```cpp
void SetActiveCustomCoordinateSystemOrigin(
   System.double OriginX,
   System.double OriginY,
   System.double OriginZ
)
```

### Parameters

- `OriginX`: x coordinate of the origin
- `OriginY`: y coordinate of the origin
- `OriginZ`: z coordinate of the origin

## Examples

[Manage Custom Coordinate Systems (C#)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_CSharp.htm)
[Manage Custom Coordinate Systems (VB.NET)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_VBNET.htm)
[Manage Custom Coordinate Systems (JavaScript)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_JS.htm)
[Manage Custom Coordinate Systems (VBA)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_VBA.htm)

## See Also

[ICustomCoordinateSystemManager Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager.html)
[ICustomCoordinateSystemManager Members](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager_members.html)

## Availability

DraftSight V1R1.4
