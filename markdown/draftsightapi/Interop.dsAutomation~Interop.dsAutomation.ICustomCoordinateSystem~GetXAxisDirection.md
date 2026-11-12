---
title: "GetXAxisDirection Method (ICustomCoordinateSystem)"
project: ""
interface: "ICustomCoordinateSystem"
member: "GetXAxisDirection"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem~GetXAxisDirection.html"
---

# GetXAxisDirection Method (ICustomCoordinateSystem)

Gets a point on the positive x axis of this coordinate system.

## Syntax

### Visual Basic

```vb
Sub GetXAxisDirection( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetXAxisDirection(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetXAxisDirection(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetXAxisDirection(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetXAxisDirection(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate
- `Y`: y coordinate
- `Z`: z coordinate

## Examples

[Manage Custom Coordinate Systems (JavaScript)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_JS.htm)
[Manage Custom Coordinate Systems (VB.NET)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_VBNET.htm)
[Manage Custom Coordinate Systems (C#)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_CSharp.htm)
[Manage Custom Coordinate Systems (VBA)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_VBA.htm)

## See Also

[ICustomCoordinateSystem Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem.html)
[ICustomCoordinateSystem Members](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem_members.html)
[ICustomCoordinateSystem::GetYAxisDirection Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem~GetYAxisDirection.html)
[ICustomCoordinateSystem::GetZAxisDirection Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem~GetZAxisDirection.html)

## Availability

DraftSight V1R1.4
