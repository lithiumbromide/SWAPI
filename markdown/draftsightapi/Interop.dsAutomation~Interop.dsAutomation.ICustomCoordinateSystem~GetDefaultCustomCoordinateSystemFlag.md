---
title: "GetDefaultCustomCoordinateSystemFlag Method (ICustomCoordinateSystem)"
project: ""
interface: "ICustomCoordinateSystem"
member: "GetDefaultCustomCoordinateSystemFlag"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem~GetDefaultCustomCoordinateSystemFlag.html"
---

# GetDefaultCustomCoordinateSystemFlag Method (ICustomCoordinateSystem)

Gets whether this is the default coordinate system.

## Syntax

### Visual Basic

```vb
Sub GetDefaultCustomCoordinateSystemFlag( _
   ByRef IsDefault As System.Boolean, _
   ByRef DefaultCustomCoordinateSystemFlag As dsDefaultCustomCoordinateSystem_e _
)
```

### C#

```csharp
void GetDefaultCustomCoordinateSystemFlag(
   out System.bool IsDefault,
   out dsDefaultCustomCoordinateSystem_e DefaultCustomCoordinateSystemFlag
)
```

### JScript

```
function GetDefaultCustomCoordinateSystemFlag(
   IsDefault : System.boolean,
   DefaultCustomCoordinateSystemFlag : dsDefaultCustomCoordinateSystem_e
);
```

### Managed Extensions for C++

```
void GetDefaultCustomCoordinateSystemFlag(
   [PARAMFLAG::Out] System.bool IsDefault,
   [PARAMFLAG::Out] dsDefaultCustomCoordinateSystem_e DefaultCustomCoordinateSystemFlag
)
```

### C++/CLI

```cpp
void GetDefaultCustomCoordinateSystemFlag(
   [Out] System.bool IsDefault,
   [Out] dsDefaultCustomCoordinateSystem_e DefaultCustomCoordinateSystemFlag
)
```

### Parameters

- `IsDefault`: True if this is the default coordinate system, false if not
- `DefaultCustomCoordinateSystemFlag`: Kind of default coordinate system as defined in [dsDefaultCustomCoordinateSystem_e](Interop.dsAutomation~Interop.dsAutomation.dsDefaultCustomCoordinateSystem_e.html); valid only if IsDefault = true

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
