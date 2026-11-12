---
title: "CheckPermission Method (IEdmTransition5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTransition5"
member: "CheckPermission"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition5~CheckPermission.html"
---

# CheckPermission Method (IEdmTransition5)

Gets whether the logged-in user has permission to perform this transition.

## Syntax

### Visual Basic

```vb
Function CheckPermission() As System.Boolean
```

### C#

```csharp
System.bool CheckPermission()
```

### C++/CLI

```cpp
System.bool CheckPermission();
```

### Return Value

True if the user can make this transition, false if not

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- S_FALSE: The user lacks permission.

## See Also

[IEdmTransition5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition5.html)
[IEdmTransition5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
