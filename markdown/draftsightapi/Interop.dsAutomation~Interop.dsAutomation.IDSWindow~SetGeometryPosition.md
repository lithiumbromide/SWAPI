---
title: "SetGeometryPosition Method (IDSWindow)"
project: ""
interface: "IDSWindow"
member: "SetGeometryPosition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDSWindow~SetGeometryPosition.html"
---

# SetGeometryPosition Method (IDSWindow)

Sets the upper-left corner of the application or document window, relative to the parent window excluding the frame.

## Syntax

### Visual Basic

```vb
Sub SetGeometryPosition( _
   ByVal X As System.Integer, _
   ByVal Y As System.Integer _
)
```

### C#

```csharp
void SetGeometryPosition(
   System.int X,
   System.int Y
)
```

### JScript

```
function SetGeometryPosition(
   X : System.int,
   Y : System.int
);
```

### Managed Extensions for C++

```
void SetGeometryPosition(
   System.int X,
   System.int Y
)
```

### C++/CLI

```cpp
void SetGeometryPosition(
   System.int X,
   System.int Y
)
```

### Parameters

- `X`: x coordinate of the upper-left corner of the window, relative to the parent window excluding the frame
- `Y`: y coordinate of the upper-left corner of the window, relative to the parent window excluding the frame

## See Also

[IDSWindow Interface](Interop.dsAutomation~Interop.dsAutomation.IDSWindow.html)
[IDSWindow Members](Interop.dsAutomation~Interop.dsAutomation.IDSWindow_members.html)
[IDSWindow::GetGeometryPosition Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~GetGeometryPosition.html)
[IDSWindow::GetGeometrySize Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~GetGeometrySize.html)
[IDSWindow::SetGeometrySize Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~SetGeometrySize.html)

## Availability

DraftSight V1R2.0
