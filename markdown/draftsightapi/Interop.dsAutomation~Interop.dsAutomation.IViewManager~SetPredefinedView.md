---
title: "SetPredefinedView Method (IViewManager)"
project: ""
interface: "IViewManager"
member: "SetPredefinedView"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewManager~SetPredefinedView.html"
---

# SetPredefinedView Method (IViewManager)

Sets a predefined orthographic or isometric view as the current view.

## Syntax

### Visual Basic

```vb
Sub SetPredefinedView( _
   ByVal PredefinedView As dsPredefinedView_e _
)
```

### C#

```csharp
void SetPredefinedView(
   dsPredefinedView_e PredefinedView
)
```

### JScript

```
function SetPredefinedView(
   PredefinedView : dsPredefinedView_e
);
```

### Managed Extensions for C++

```
void SetPredefinedView(
   dsPredefinedView_e PredefinedView
)
```

### C++/CLI

```cpp
void SetPredefinedView(
   dsPredefinedView_e PredefinedView
)
```

### Parameters

- `PredefinedView`: Predefined orthographic or isometric view as defined in [dsPredefinedView_e](Interop.dsAutomation~Interop.dsAutomation.dsPredefinedView_e.html)

## Examples

[Manage Custom Coordinate Systems (JavaScript)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_JS.htm)
[Manage Custom Coordinate Systems (VB.NET)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_VBNET.htm)
[Manage Custom Coordinate Systems (C#)](Manage_Default_and_Named_Custom_Coordinate_Systems_Example_CSharp.htm)

## See Also

[IViewManager Interface](Interop.dsAutomation~Interop.dsAutomation.IViewManager.html)
[IViewManager Members](Interop.dsAutomation~Interop.dsAutomation.IViewManager_members.html)

## Availability

DraftSight V1R1.4
