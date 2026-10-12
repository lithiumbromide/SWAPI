---
title: "CheckProjectPermission Method (IEdmTransition8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTransition8"
member: "CheckProjectPermission"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition8~CheckProjectPermission.html"
---

# CheckProjectPermission Method (IEdmTransition8)

Checks whether the user has permission to perform this transition for the specified project.

## Syntax

### Visual Basic

```vb
Function CheckProjectPermission( _
   ByVal lProjectID As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool CheckProjectPermission(
   System.int lProjectID
)
```

### C++/CLI

```cpp
System.bool CheckProjectPermission(
   System.int lProjectID
)
```

### Parameters

- `lProjectID`: Project ID

### Return Value

True if the user has permission to perform the transition, false if not

## See Also

[IEdmTransition8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition8.html)
[IEdmTransition8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition8_members.html)
