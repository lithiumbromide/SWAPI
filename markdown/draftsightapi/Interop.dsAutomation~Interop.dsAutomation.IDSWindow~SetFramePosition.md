---
title: "SetFramePosition Method (IDSWindow)"
project: ""
interface: "IDSWindow"
member: "SetFramePosition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDSWindow~SetFramePosition.html"
---

# SetFramePosition Method (IDSWindow)

Sets the upper-left corner of the application or document window, relative to the parent window including the frame.

## Syntax

### Visual Basic

```vb
Sub SetFramePosition( _
   ByVal X As System.Integer, _
   ByVal Y As System.Integer _
)
```

### C#

```csharp
void SetFramePosition(
   System.int X,
   System.int Y
)
```

### JScript

```
function SetFramePosition(
   X : System.int,
   Y : System.int
);
```

### Managed Extensions for C++

```
void SetFramePosition(
   System.int X,
   System.int Y
)
```

### C++/CLI

```cpp
void SetFramePosition(
   System.int X,
   System.int Y
)
```

### Parameters

- `X`: x coordinate of the upper-left corner of the window, relative to the parent window including the frame
- `Y`: y coordinate of the upper-left corner of the window, relative to the parent window including the frame

## See Also

[IDSWindow Interface](Interop.dsAutomation~Interop.dsAutomation.IDSWindow.html)
[IDSWindow Members](Interop.dsAutomation~Interop.dsAutomation.IDSWindow_members.html)
[IDSWindow::GetFramePosition Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~GetFramePosition.html)
[IDSWindow::GetFrameSize Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~GetFrameSize.html)
[IDSWindow::SetFrameSize Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~SetFrameSize.html)

## Availability

DraftSight V1R2.0
