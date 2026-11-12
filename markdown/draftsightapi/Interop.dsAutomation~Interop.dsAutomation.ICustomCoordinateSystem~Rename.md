---
title: "Rename Method (ICustomCoordinateSystem)"
project: ""
interface: "ICustomCoordinateSystem"
member: "Rename"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem~Rename.html"
---

# Rename Method (ICustomCoordinateSystem)

Renames this coordinate system.

## Syntax

### Visual Basic

```vb
Function Rename( _
   ByVal NewName As System.String _
) As dsCreateObjectResult_e
```

### C#

```csharp
dsCreateObjectResult_e Rename(
   System.string NewName
)
```

### JScript

```
function Rename(
   NewName : System.String
) : dsCreateObjectResult_e;
```

### Managed Extensions for C++

```
dsCreateObjectResult_e Rename(
   System.string* NewName
)
```

### C++/CLI

```cpp
dsCreateObjectResult_e Rename(
   System.String^ NewName
)
```

### Parameters

- `NewName`: New name of this coordinate system

### Return Value

Return status as defined in [dsCreateObjectResult_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateObjectResult_e.html)

## Examples

[Manage Custom Coordinate Systems (C#)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_CSharp.htm)
[Manage Custom Coordinate Systems (VB.NET)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_VBNET.htm)
[Manage Custom Coordinate Systems (JavaScript)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_JS.htm)
[Manage Custom Coordinate Systems (VBA)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_VBA.htm)

## See Also

[ICustomCoordinateSystem Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem.html)
[ICustomCoordinateSystem Members](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem_members.html)
[ICustomCoordinateSystem::GetName Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem~GetName.html)

## Availability

DraftSight V1R1.4
