---
title: "GetHWND Method (IDSWindow)"
project: ""
interface: "IDSWindow"
member: "GetHWND"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDSWindow~GetHWND.html"
---

# GetHWND Method (IDSWindow)

Gets the DraftSight application or document window's handle.

## Syntax

### Visual Basic

```vb
Sub GetHWND( _
   ByRef HWND As System.Integer _
)
```

### C#

```csharp
void GetHWND(
   out System.int HWND
)
```

### JScript

```
function GetHWND(
   HWND : System.int
);
```

### Managed Extensions for C++

```
void GetHWND(
   [PARAMFLAG::Out] System.int HWND
)
```

### C++/CLI

```cpp
void GetHWND(
   [Out] System.int HWND
)
```

### Parameters

- `HWND`: DraftSight application or document window's handle

## Examples

[Get and Set Windows Values (C#)](Get_and_Set_Windows_Values_Example_CSharp.htm)
[Get and Set Windows Values (VB.NET)](Get_and_Set_Windows_Values_Example_VBNET.htm)
[Get and Set Windows Values (VBA)](Get_and_Set_Windows_Values_Example_VBA.htm)

## See Also

[IDSWindow Interface](Interop.dsAutomation~Interop.dsAutomation.IDSWindow.html)
[IDSWindow Members](Interop.dsAutomation~Interop.dsAutomation.IDSWindow_members.html)
[IApplication::GetHWND Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetHWND.html)

## Availability

DraftSight V1R2.0
