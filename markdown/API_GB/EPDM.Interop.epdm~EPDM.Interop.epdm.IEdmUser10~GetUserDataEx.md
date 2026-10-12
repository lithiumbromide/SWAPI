---
title: "GetUserDataEx Method (IEdmUser10)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUser10"
member: "GetUserDataEx"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser10~GetUserDataEx.html"
---

# GetUserDataEx Method (IEdmUser10)

Gets information about this user.

## Syntax

### Visual Basic

```vb
Sub GetUserDataEx( _
   ByRef poUserData As EdmUserDataEx _
)
```

### C#

```csharp
void GetUserDataEx(
   out EdmUserDataEx poUserData
)
```

### C++/CLI

```cpp
void GetUserDataEx(
   [Out] EdmUserDataEx poUserData
)
```

### Parameters

- `poUserData`: [EdmUserDataEx](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserDataEx.html) (see **Remarks**)

## Examples

See the [IEdmUser10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser10.html) examples.

## Remarks

The properties and picture associated with this user can be returned. EdmUserDataEx::mlEdmUserDataExFlags indicates which properties to return.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUser10 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser10.html)
[IEdmUser10 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser10_members.html)
[IEdmuser10::SetUserDataEx Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser10~SetUserDataEx.html)

## Availability

SOLIDWORKS PDM Professional 2013
