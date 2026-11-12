---
title: "SaveActiveViewAs Method (ICustomCoordinateSystemManager)"
project: ""
interface: "ICustomCoordinateSystemManager"
member: "SaveActiveViewAs"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~SaveActiveViewAs.html"
---

# SaveActiveViewAs Method (ICustomCoordinateSystemManager)

Creates a new instance of a coordinate system with the specified name for the active view.

## Syntax

### Visual Basic

```vb
Function SaveActiveViewAs( _
   ByVal Name As System.String, _
   ByRef CustomCoordinateSystem As CustomCoordinateSystem _
) As dsCreateObjectResult_e
```

### C#

```csharp
dsCreateObjectResult_e SaveActiveViewAs(
   System.string Name,
   out CustomCoordinateSystem CustomCoordinateSystem
)
```

### JScript

```
function SaveActiveViewAs(
   Name : System.String,
   CustomCoordinateSystem : CustomCoordinateSystem
) : dsCreateObjectResult_e;
```

### Managed Extensions for C++

```
dsCreateObjectResult_e SaveActiveViewAs(
   System.string* Name,
   [PARAMFLAG::Out] CustomCoordinateSystem* CustomCoordinateSystem
)
```

### C++/CLI

```cpp
dsCreateObjectResult_e SaveActiveViewAs(
   System.String^ Name,
   [Out] CustomCoordinateSystem^ CustomCoordinateSystem
)
```

### Parameters

- `Name`: New name for the coordinate system
- `CustomCoordinateSystem`: [ICustomCoordinateSystem](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem.html)

### Return Value

Return status as defined in [dsCreateObjectResult_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateObjectResult_e.html)

## Examples

[Manage Custom Coordinate Systems (JavaScript)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_JS.htm)
[Manage Custom Coordinate Systems (VB.NET)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_VBNET.htm)
[Manage Custom Coordinate Systems (C#)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_CSharp.htm)
[Manage Custom Coordinate Systems (VBA)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_VBA.htm)

## See Also

[ICustomCoordinateSystemManager Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager.html)
[ICustomCoordinateSystemManager Members](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager_members.html)

## Availability

DraftSight V1R1.4
