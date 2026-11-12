---
title: "GetYAxisDirection Method (ICustomCoordinateSystem)"
project: ""
interface: "ICustomCoordinateSystem"
member: "GetYAxisDirection"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem~GetYAxisDirection.html"
---

# GetYAxisDirection Method (ICustomCoordinateSystem)

Gets a point on the positive y axis of this coordinate system.

## Syntax

### Visual Basic

```vb
Sub GetYAxisDirection( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetYAxisDirection(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetYAxisDirection(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetYAxisDirection(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetYAxisDirection(
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

[Manage Custom Coordinate Systems (C#)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_CSharp.htm)
[Manage Custom Coordinate Systems (VB.NET)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_VBNET.htm)
[Manage Custom Coordinate Systems (JavaScript)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_JS.htm)
[Manage Custom Coordinate Systems (VBA)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_VBA.htm)

## See Also

[ICustomCoordinateSystem Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem.html)
[ICustomCoordinateSystem Members](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem_members.html)
[ICustomCoordinateSystem::GetXAxisDirection Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem~GetXAxisDirection.html)
[ICustomCoordinateSystem::GetZAxisDirection Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem~GetZAxisDirection.html)

## Availability

DraftSight V1R1.4
