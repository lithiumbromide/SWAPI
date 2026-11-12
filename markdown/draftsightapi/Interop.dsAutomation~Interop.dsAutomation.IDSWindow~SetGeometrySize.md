---
title: "SetGeometrySize Method (IDSWindow)"
project: ""
interface: "IDSWindow"
member: "SetGeometrySize"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDSWindow~SetGeometrySize.html"
---

# SetGeometrySize Method (IDSWindow)

Sets the size of the application or document window, relative to the parent window excluding the frame.

## Syntax

### Visual Basic

```vb
Sub SetGeometrySize( _
   ByVal Height As System.Integer, _
   ByVal Width As System.Integer _
)
```

### C#

```csharp
void SetGeometrySize(
   System.int Height,
   System.int Width
)
```

### JScript

```
function SetGeometrySize(
   Height : System.int,
   Width : System.int
);
```

### Managed Extensions for C++

```
void SetGeometrySize(
   System.int Height,
   System.int Width
)
```

### C++/CLI

```cpp
void SetGeometrySize(
   System.int Height,
   System.int Width
)
```

### Parameters

- `Height`: Height of the window, in pixels, relative to the parent window excluding the frame
- `Width`: Width of the window, in pixels, relative to the parent window excluding the frame

## See Also

[IDSWindow Interface](Interop.dsAutomation~Interop.dsAutomation.IDSWindow.html)
[IDSWindow Members](Interop.dsAutomation~Interop.dsAutomation.IDSWindow_members.html)
[IDSWindow::GetGeometryPosition Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~GetGeometryPosition.html)
[IDSWindow::GetGeometrySize Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~GetGeometrySize.html)
[IDSWindow::SetGeometryPosition Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~SetGeometryPosition.html)
