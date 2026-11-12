---
title: "RemoveCustomCoordinateSystem Method (ICustomCoordinateSystemManager)"
project: ""
interface: "ICustomCoordinateSystemManager"
member: "RemoveCustomCoordinateSystem"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~RemoveCustomCoordinateSystem.html"
---

# RemoveCustomCoordinateSystem Method (ICustomCoordinateSystemManager)

Deletes the coordinate system with the specified name.

## Syntax

### Visual Basic

```vb
Function RemoveCustomCoordinateSystem( _
   ByVal CustomCoordinateSystemName As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool RemoveCustomCoordinateSystem(
   System.string CustomCoordinateSystemName
)
```

### JScript

```
function RemoveCustomCoordinateSystem(
   CustomCoordinateSystemName : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool RemoveCustomCoordinateSystem(
   System.string* CustomCoordinateSystemName
)
```

### C++/CLI

```cpp
System.bool RemoveCustomCoordinateSystem(
   System.String^ CustomCoordinateSystemName
)
```

### Parameters

- `CustomCoordinateSystemName`: Name of the coordinate system to delete

### Return Value

True if successful, false if not

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
