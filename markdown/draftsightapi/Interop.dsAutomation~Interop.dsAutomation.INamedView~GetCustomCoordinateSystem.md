---
title: "GetCustomCoordinateSystem Method (INamedView)"
project: ""
interface: "INamedView"
member: "GetCustomCoordinateSystem"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.INamedView~GetCustomCoordinateSystem.html"
---

# GetCustomCoordinateSystem Method (INamedView)

Gets the custom coordinate system associated with this named view.

## Syntax

### Visual Basic

```vb
Function GetCustomCoordinateSystem() As CustomCoordinateSystem
```

### C#

```csharp
CustomCoordinateSystem GetCustomCoordinateSystem()
```

### JScript

```
function GetCustomCoordinateSystem() : CustomCoordinateSystem;
```

### Managed Extensions for C++

```
CustomCoordinateSystem* GetCustomCoordinateSystem();
```

### C++/CLI

```cpp
CustomCoordinateSystem^ GetCustomCoordinateSystem();
```

### Return Value

[Custom coordinate system](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem.html)

## Remarks

Null or nothing is returned if a custom coordinate system is not associated with this named view.

## See Also

[INamedView Interface](Interop.dsAutomation~Interop.dsAutomation.INamedView.html)
[INamedView Members](Interop.dsAutomation~Interop.dsAutomation.INamedView_members.html)
[INamedView::RemoveCustomCoordinateSystem Method ()](Interop.dsAutomation~Interop.dsAutomation.INamedView~RemoveCustomCoordinateSystem.html)
[INamedView::SetCustomCoordinateSystem Method ()](Interop.dsAutomation~Interop.dsAutomation.INamedView~SetCustomCoordinateSystem.html)

## Availability

DraftSight V1R5.0
