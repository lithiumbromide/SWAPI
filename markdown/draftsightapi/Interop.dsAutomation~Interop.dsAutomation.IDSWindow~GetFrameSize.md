---
title: "GetFrameSize Method (IDSWindow)"
project: ""
interface: "IDSWindow"
member: "GetFrameSize"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDSWindow~GetFrameSize.html"
---

# GetFrameSize Method (IDSWindow)

Gets the size of the application or document window, relative to the parent window including the frame.

## Syntax

### Visual Basic

```vb
Sub GetFrameSize( _
   ByRef Height As System.Integer, _
   ByRef Width As System.Integer _
)
```

### C#

```csharp
void GetFrameSize(
   out System.int Height,
   out System.int Width
)
```

### JScript

```
function GetFrameSize(
   Height : System.int,
   Width : System.int
);
```

### Managed Extensions for C++

```
void GetFrameSize(
   [PARAMFLAG::Out] System.int Height,
   [PARAMFLAG::Out] System.int Width
)
```

### C++/CLI

```cpp
void GetFrameSize(
   [Out] System.int Height,
   [Out] System.int Width
)
```

### Parameters

- `Height`: Height of the window, in pixels, relative to the parent window including the frame
- `Width`: Width of the window, in pixels, relative to the parent window including the frame

## Examples

[Get and Set Windows Values (C#)](Get_and_Set_Windows_Values_Example_CSharp.htm)
[Get and Set Windows Values (VB.NET)](Get_and_Set_Windows_Values_Example_VBNET.htm)
[Get and Set Windows Values (VBA)](Get_and_Set_Windows_Values_Example_VBA.htm)

## See Also

[IDSWindow Interface](Interop.dsAutomation~Interop.dsAutomation.IDSWindow.html)
[IDSWindow Members](Interop.dsAutomation~Interop.dsAutomation.IDSWindow_members.html)
[IDSWindow::GetFramePosition Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~GetFramePosition.html)
[IDSWindow::SetFramePosition Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~SetFramePosition.html)
[IDSWindow::SetFrameSize Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~SetFrameSize.html)

## Availability

DraftSight V1R2.0
