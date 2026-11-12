---
title: "WindowState Property (IDSWindow)"
project: ""
interface: "IDSWindow"
member: "WindowState"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDSWindow~WindowState.html"
---

# WindowState Property (IDSWindow)

Gets or sets the state of the DraftSight application or document window.

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

State of DraftSight application or document window as defined in [dsWindowState_e](Interop.dsAutomation~Interop.dsAutomation.dsWindowState_e.html)

## Examples

[Get and Set Windows Values (C#)](Get_and_Set_Windows_Values_Example_CSharp.htm)
[Get and Set Windows Values (VB.NET)](Get_and_Set_Windows_Values_Example_VBNET.htm)
[Get and Set Windows Values (VBA)](Get_and_Set_Windows_Values_Example_VBA.htm)
[Minimize or Maximize Window (JavaScript)](Minimize_or_Maximize_Window_Example_JS.htm)

## See Also

[IDSWindow Interface](Interop.dsAutomation~Interop.dsAutomation.IDSWindow.html)
[IDSWindow Members](Interop.dsAutomation~Interop.dsAutomation.IDSWindow_members.html)
[IApplication::WindowState Property](Interop.dsAutomation~Interop.dsAutomation.IApplication~WindowState.html)

## Availability

DraftSight V1R2.0
