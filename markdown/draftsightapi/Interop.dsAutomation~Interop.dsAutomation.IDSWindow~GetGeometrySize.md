---
title: "GetGeometrySize Method (IDSWindow)"
project: ""
interface: "IDSWindow"
member: "GetGeometrySize"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDSWindow~GetGeometrySize.html"
---

# GetGeometrySize Method (IDSWindow)

Gets the size of the application or document window, relative to the parent window excluding the frame.

## Syntax

### Visual Basic

```vb
Sub GetGeometrySize( _
   ByRef Height As System.Integer, _
   ByRef Width As System.Integer _
)
```

### C#

```csharp
void GetGeometrySize(
   out System.int Height,
   out System.int Width
)
```

### JScript

```
function GetGeometrySize(
   Height : System.int,
   Width : System.int
);
```

### Managed Extensions for C++

```
void GetGeometrySize(
   [PARAMFLAG::Out] System.int Height,
   [PARAMFLAG::Out] System.int Width
)
```

### C++/CLI

```cpp
void GetGeometrySize(
   [Out] System.int Height,
   [Out] System.int Width
)
```

### Parameters

- `Height`: Height of the window, in pixels, relative to the parent window excluding the frame
- `Width`: Width of the window, in pixels, relative to the parent window excluding the frame

## Examples

[Get and Set Windows Values (C#)](Get_and_Set_Windows_Values_Example_CSharp.htm)
[Get and Set Windows Values (VB.NET)](Get_and_Set_Windows_Values_Example_VBNET.htm)
[Get and Set Windows Values (VBA)](Get_and_Set_Windows_Values_Example_VBA.htm)

## See Also

[IDSWindow Interface](Interop.dsAutomation~Interop.dsAutomation.IDSWindow.html)
[IDSWindow Members](Interop.dsAutomation~Interop.dsAutomation.IDSWindow_members.html)
[IDSWindow::GetGeometryPosition Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~GetGeometryPosition.html)
[IDSWindow::SetGeometryPosition Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~SetGeometryPosition.html)
[IDSWindow::SetGeometrySize Method](Interop.dsAutomation~Interop.dsAutomation.IDSWindow~SetGeometrySize.html)

## Availability

DraftSight V1R2.0
