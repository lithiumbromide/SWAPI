---
title: "SetFrameSize Method (IDSWindow)"
project: ""
interface: "IDSWindow"
member: "SetFrameSize"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDSWindow~SetFrameSize.html"
---

# SetFrameSize Method (IDSWindow)

Sets the size of the application or document window, relative to the parent window including the frame.

## Syntax

### Visual Basic

```vb
Sub SetFrameSize( _
   ByVal Height As System.Integer, _
   ByVal Width As System.Integer _
)
```

### C#

```csharp
void SetFrameSize(
   System.int Height,
   System.int Width
)
```

### JScript

```
function SetFrameSize(
   Height : System.int,
   Width : System.int
);
```

### Managed Extensions for C++

```
void SetFrameSize(
   System.int Height,
   System.int Width
)
```

### C++/CLI

```cpp
void SetFrameSize(
   System.int Height,
   System.int Width
)
```

### Parameters

- `Height`: Height of the window, in pixels, relative to the parent window including the frame
- `Width`: Width of the window, in pixels, relative to the parent window including the frame

## See Also

[IDSWindow Interface](Interop.dsAutomation~Interop.dsAutomation.IDSWindow.html)
[IDSWindow Members](Interop.dsAutomation~Interop.dsAutomation.IDSWindow_members.html)
[IDSWindow::GetFramePosition Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~GetFramePosition.html)
[IDSWindow::GetFrameSize Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~GetFrameSize.html)
[IDSWindow::SetFramePosition Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~SetFramePosition.html)

## Availability

DraftSight V1R2.0
