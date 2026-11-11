---
title: "GetOrigin Method (ICustomCoordinateSystem)"
project: ""
interface: "ICustomCoordinateSystem"
member: "GetOrigin"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem~GetOrigin.html"
---

# GetOrigin Method (ICustomCoordinateSystem)

Gets the coordinates of the origin of this coordinate system.

## Syntax

### Visual Basic

```vb
Sub GetOrigin( _
   ByRef OriginX As System.Double, _
   ByRef OriginY As System.Double, _
   ByRef OriginZ As System.Double _
)
```

### C#

```csharp
void GetOrigin(
   out System.double OriginX,
   out System.double OriginY,
   out System.double OriginZ
)
```

### JScript

```
function GetOrigin(
   OriginX : System.double,
   OriginY : System.double,
   OriginZ : System.double
);
```

### Managed Extensions for C++

```
void GetOrigin(
   [PARAMFLAG::Out] System.double OriginX,
   [PARAMFLAG::Out] System.double OriginY,
   [PARAMFLAG::Out] System.double OriginZ
)
```

### C++/CLI

```cpp
void GetOrigin(
   [Out] System.double OriginX,
   [Out] System.double OriginY,
   [Out] System.double OriginZ
)
```

### Parameters

- `OriginX`: x coordinate
- `OriginY`: y coordinate
- `OriginZ`: z coordinate

## Examples

[Manage Custom Coordinate Systems (C#)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_CSharp.htm)
[Manage Custom Coordinate Systems (VB.NET)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_VBNET.htm)
[Manage Custom Coordinate Systems (JavaScript)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_JS.htm)
[Manage Custom Coordinate Systems (VBA)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_VBA.htm)

## See Also

[ICustomCoordinateSystem Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem.html)
[ICustomCoordinateSystem Members](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem_members.html)

## Availability

DraftSight V1R1.4
