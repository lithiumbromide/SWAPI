---
title: "SetUserDataEx Method (IEdmUser10)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUser10"
member: "SetUserDataEx"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser10~SetUserDataEx.html"
---

# SetUserDataEx Method (IEdmUser10)

Sets information about this user.

## Syntax

### Visual Basic

```vb
Sub SetUserDataEx( _
   ByRef poUserData As EdmUserDataEx _
)
```

### C#

```csharp
void SetUserDataEx(
   ref EdmUserDataEx poUserData
)
```

### C++/CLI

```cpp
void SetUserDataEx(
   EdmUserDataEx% poUserData
)
```

### Parameters

- `poUserData`: [EdmUserDataEx](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserDataEx.html) structure (see **Remarks**)

## Examples

See the [IEdmUser10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser10.html) examples.

## Remarks

The properties and picture associated with this user can be updated using this method. EdmUserDataEx::mlEdmUserDataExFlags indicates which properties to update. EdmUserDataEx::mlUserID is ignored.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_PERMISSION_DENIED: The logged-in user doesn't have user administration privileges.
- E_EDM_FILE_NOT_FOUND: A new user picture path was specified, but the file wasn't found.
- E_EDM_INVALID_FILE: A new user picture path was specified, but the file format isn't supported.

## See Also

[IEdmUser10 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser10.html)
[IEdmUser10 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser10_members.html)

## Availability

SOLIDWORKS PDM Professional 2013
