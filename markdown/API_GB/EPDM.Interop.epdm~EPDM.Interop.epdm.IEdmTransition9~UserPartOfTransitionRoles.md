---
title: "UserPartOfTransitionRoles Property (IEdmTransition9)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTransition9"
member: "UserPartOfTransitionRoles"
kind: "property"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition9~UserPartOfTransitionRoles.html"
---

# UserPartOfTransitionRoles Property (IEdmTransition9)

Gets whether the logged-in user has a role in this parallel transition.

## Syntax

### Visual Basic

```vb
ReadOnly Property UserPartOfTransitionRoles( _
   ByVal lProjectID As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool UserPartOfTransitionRoles(
   System.int lProjectID
) {get;}
```

### C++/CLI

```cpp
property System.bool UserPartOfTransitionRoles {
   System.bool get(System.int lProjectID);
}
```

### Parameters

- `lProjectID`: Project ID

### Property Value

True if the logged-in user has a role in this parallel transition, false if not

## See Also

[IEdmTransition9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition9.html)
[IEdmTransition9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition9_members.html)
