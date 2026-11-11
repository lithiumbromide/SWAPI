---
title: "WindowState Property (IApplication)"
project: ""
interface: "IApplication"
member: "WindowState"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~WindowState.html"
---

# WindowState Property (IApplication)

Gets or sets the state of the DraftSight application window.

## Syntax

### Visual Basic

```vb
Property WindowState As dsWindowState_e
```

### C#

```csharp
dsWindowState_e WindowState {get; set;}
```

### JScript

```
function get,set WindowState : dsWindowState_e
```

### Managed Extensions for C++

```
__property dsWindowState_e get_WindowState();
__property void set_WindowState(
   dsWindowState_e value
);
```

### C++/CLI

```cpp
property dsWindowState_e WindowState {
   dsWindowState_e get();
   void set (    dsWindowState_e value);
}
```

### Property Value

State of DraftSight application window as defined in [dsWindowState_e](Interop.dsAutomation~Interop.dsAutomation.dsWindowState_e.html)

## Examples

[Get and Set Windows Values (C#)](Get_and_Set_Windows_Values_Example_CSharp.htm)
[Get and Set Windows Values (VB.NET)](Get_and_Set_Windows_Values_Example_VBNET.htm)
[Get and Set Windows Values (VBA)](Get_and_Set_Windows_Values_Example_VBA.htm)

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::GetMainWindow Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetMainWindow.html)
[IDSWindow::WindowState Property](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~WindowState.html)

## Availability

DraftSight V1R1.2
