---
title: "GetFramePosition Method (IDSWindow)"
project: ""
interface: "IDSWindow"
member: "GetFramePosition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDSWindow~GetFramePosition.html"
---

# GetFramePosition Method (IDSWindow)

Gets the upper-left corner of the application or document window, relative to the parent window including the frame.

## Syntax

### Visual Basic

```vb
Sub GetFramePosition( _
   ByRef X As System.Integer, _
   ByRef Y As System.Integer _
)
```

### C#

```csharp
void GetFramePosition(
   out System.int X,
   out System.int Y
)
```

### JScript

```
function GetFramePosition(
   X : System.int,
   Y : System.int
);
```

### Managed Extensions for C++

```
void GetFramePosition(
   [PARAMFLAG::Out] System.int X,
   [PARAMFLAG::Out] System.int Y
)
```

### C++/CLI

```cpp
void GetFramePosition(
   [Out] System.int X,
   [Out] System.int Y
)
```

### Parameters

- `X`: x coordinate of the upper-left corner of the window, relative to the parent window including the frame
- `Y`: y coordinate of the upper-left corner of the window, relative to the parent window including the frame

## Examples

[Get and Set Windows Values (C#)](Get_and_Set_Windows_Values_Example_CSharp.htm)
[Get and Set Windows Values (VB.NET)](Get_and_Set_Windows_Values_Example_VBNET.htm)
[Get and Set Windows Values (VBA)](Get_and_Set_Windows_Values_Example_VBA.htm)

## See Also

[IDSWindow Interface](Interop.dsAutomation~Interop.dsAutomation.IDSWindow.html)
[IDSWindow Members](Interop.dsAutomation~Interop.dsAutomation.IDSWindow_members.html)
[IDSWindow::GetFrameSize Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~GetFrameSize.html)
[IDSWindow::SetFrameSize Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~SetFrameSize.html)
[IDSWindow::SetFramePosition Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~SetFramePosition.html)

## Availability

DraftSight V1R2.0
