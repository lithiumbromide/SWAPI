---
title: "GetGeometryPosition Method (IDSWindow)"
project: ""
interface: "IDSWindow"
member: "GetGeometryPosition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDSWindow~GetGeometryPosition.html"
---

# GetGeometryPosition Method (IDSWindow)

Gets the upper-left corner of the application or document window, relative to the parent window excluding the frame.

## Syntax

### Visual Basic

```vb
Sub GetGeometryPosition( _
   ByRef X As System.Integer, _
   ByRef Y As System.Integer _
)
```

### C#

```csharp
void GetGeometryPosition(
   out System.int X,
   out System.int Y
)
```

### JScript

```
function GetGeometryPosition(
   X : System.int,
   Y : System.int
);
```

### Managed Extensions for C++

```
void GetGeometryPosition(
   [PARAMFLAG::Out] System.int X,
   [PARAMFLAG::Out] System.int Y
)
```

### C++/CLI

```cpp
void GetGeometryPosition(
   [Out] System.int X,
   [Out] System.int Y
)
```

### Parameters

- `X`: x coordinate of the upper-left corner of the window, relative to the parent window excluding the frame
- `Y`: y coordinate of the upper-left corner of the window, relative to the parent window excluding the frame

## Examples

[Get and Set Windows Values (C#)](Get_and_Set_Windows_Values_Example_CSharp.htm)
[Get and Set Windows Values (VB.NET)](Get_and_Set_Windows_Values_Example_VBNET.htm)
[Get and Set Windows Values (VBA)](Get_and_Set_Windows_Values_Example_VBA.htm)

## See Also

[IDSWindow Interface](Interop.dsAutomation~Interop.dsAutomation.IDSWindow.html)
[IDSWindow Members](Interop.dsAutomation~Interop.dsAutomation.IDSWindow_members.html)
[IDSWindow::GetGeometrySize Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~GetGeometrySize.html)
[IDSWindow::SetGeometryPosition Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~SetGeometryPosition.html)
[IDSWindow::SetGeometrySize Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~SetGeometrySize.html)

## Availability

DraftSight V1R2.0
