---
title: "GetDefaultCustomCoordinateSystem Method (ICustomCoordinateSystemManager)"
project: ""
interface: "ICustomCoordinateSystemManager"
member: "GetDefaultCustomCoordinateSystem"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~GetDefaultCustomCoordinateSystem.html"
---

# GetDefaultCustomCoordinateSystem Method (ICustomCoordinateSystemManager)

Gets a default coordinate system.

## Syntax

### Visual Basic

```vb
Function GetDefaultCustomCoordinateSystem( _
   ByVal DefaultCustomCoordinateSystem As dsDefaultCustomCoordinateSystem_e _
) As CustomCoordinateSystem
```

### C#

```csharp
CustomCoordinateSystem GetDefaultCustomCoordinateSystem(
   dsDefaultCustomCoordinateSystem_e DefaultCustomCoordinateSystem
)
```

### JScript

```
function GetDefaultCustomCoordinateSystem(
   DefaultCustomCoordinateSystem : dsDefaultCustomCoordinateSystem_e
) : CustomCoordinateSystem;
```

### Managed Extensions for C++

```
CustomCoordinateSystem* GetDefaultCustomCoordinateSystem(
   dsDefaultCustomCoordinateSystem_e DefaultCustomCoordinateSystem
)
```

### C++/CLI

```cpp
CustomCoordinateSystem^ GetDefaultCustomCoordinateSystem(
   dsDefaultCustomCoordinateSystem_e DefaultCustomCoordinateSystem
)
```

### Parameters

- `DefaultCustomCoordinateSystem`: Kind of coordinate system as defined in [dsDefaultCustomCoordinateSystem_e](Interop.dsAutomation~Interop.dsAutomation.dsDefaultCustomCoordinateSystem_e.html)

### Return Value

[ICustomCoordinateSystem](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem.html)

## Examples

[Manage Custom Coordinate Systems (C#)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_CSharp.htm)
[Manage Custom Coordinate Systems (VB.NET)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_VBNET.htm)
[Manage Custom Coordinate Systems (JavaScript)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_JS.htm)
[Manage Custom Coordinate Systems (VBA)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_VBA.htm)

## See Also

[ICustomCoordinateSystemManager Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager.html)
[ICustomCoordinateSystemManager Members](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager_members.html)
[ICustomCoordinateSystemManager::GetActiveCustomCoordinateSystem Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~GetActiveCustomCoordinateSystem.html)
[ICustomCoordinateSystemManager::GetNamedCustomCoordinateSystem Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~GetNamedCustomCoordinateSystem.html)
[ICustomCoordinateSystemManager::GetNamedCustomCoordinateSystemList Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~GetNamedCustomCoordinateSystemList.html)
[ICustomCoordinateSystemManager::GetPreviousCustomCoordinateSystem Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~GetPreviousCustomCoordinateSystem.html)
[ICustomCoordinateSystemManager::GetWorldCustomCoordinateSystem Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~GetWorldCustomCoordinateSystem.html)

## Availability

DraftSight V1R1.4
