---
title: "GetNamedCustomCoordinateSystem Method (ICustomCoordinateSystemManager)"
project: ""
interface: "ICustomCoordinateSystemManager"
member: "GetNamedCustomCoordinateSystem"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~GetNamedCustomCoordinateSystem.html"
---

# GetNamedCustomCoordinateSystem Method (ICustomCoordinateSystemManager)

Gets the coordinate system with the specified name.

## Syntax

### Visual Basic

```vb
Function GetNamedCustomCoordinateSystem( _
   ByVal CSSName As System.String _
) As CustomCoordinateSystem
```

### C#

```csharp
CustomCoordinateSystem GetNamedCustomCoordinateSystem(
   System.string CSSName
)
```

### JScript

```
function GetNamedCustomCoordinateSystem(
   CSSName : System.String
) : CustomCoordinateSystem;
```

### Managed Extensions for C++

```
CustomCoordinateSystem* GetNamedCustomCoordinateSystem(
   System.string* CSSName
)
```

### C++/CLI

```cpp
CustomCoordinateSystem^ GetNamedCustomCoordinateSystem(
   System.String^ CSSName
)
```

### Parameters

- `CSSName`: Name of coordinate system

### Return Value

[ICustomCoordinateSystem](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem.html)

## See Also

[ICustomCoordinateSystemManager Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager.html)
[ICustomCoordinateSystemManager Members](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager_members.html)
[ICustomCoordinateSystemManager::GetActiveCustomCoordinateSystem Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~GetActiveCustomCoordinateSystem.html)
[ICustomCoordinateSystemManager::GetDefaultCustomCoordinateSystem Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~GetDefaultCustomCoordinateSystem.html)
[ICustomCoordinateSystemManager::GetNamedCustomCoordinateSystemList Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~GetNamedCustomCoordinateSystemList.html)
[ICustomCoordinateSystemManager::GetPreviousCustomCoordinateSystem Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~GetPreviousCustomCoordinateSystem.html)
[ICustomCoordinateSystemManager::GetWorldCustomCoordinateSystem Method](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystemManager~GetWorldCustomCoordinateSystem.html)

## Availability

DraftSight V1R1.4
