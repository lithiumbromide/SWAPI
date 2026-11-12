---
title: "GetHWND64 Method (IDSWindow)"
project: ""
interface: "IDSWindow"
member: "GetHWND64"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDSWindow~GetHWND64.html"
---

# GetHWND64 Method (IDSWindow)

Gets the 64-bit window handle of this DraftSight application or document.

## Syntax

### Visual Basic

```vb
Sub GetHWND64( _
   ByRef HWND As System.Long _
)
```

### C#

```csharp
void GetHWND64(
   out System.long HWND
)
```

### JScript

```
function GetHWND64(
   HWND : System.long
);
```

### Managed Extensions for C++

```
void GetHWND64(
   [PARAMFLAG::Out] System.long HWND
)
```

### C++/CLI

```cpp
void GetHWND64(
   [Out] System.int64 HWND
)
```

### Parameters

- `HWND`: 64-bit window handle of this DraftSight application or document

## See Also

[IDSWindow Interface](Interop.dsAutomation~Interop.dsAutomation.IDSWindow.html)
[IDSWindow Members](Interop.dsAutomation~Interop.dsAutomation.IDSWindow_members.html)

## Availability

DraftSight 2022 SP0
