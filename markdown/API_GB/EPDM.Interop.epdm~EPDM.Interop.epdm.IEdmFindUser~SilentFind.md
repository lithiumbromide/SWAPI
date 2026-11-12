---
title: "SilentFind Method (IEdmFindUser)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFindUser"
member: "SilentFind"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser~SilentFind.html"
---

# SilentFind Method (IEdmFindUser)

Silently searches for users with search criteria specified by [IEdmFindUser::SetPropt](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser~SetPropt.html).

## Syntax

### Visual Basic

```vb
Sub SilentFind()
```

### C#

```csharp
void SilentFind()
```

### C++/CLI

```cpp
void SilentFind();
```

## Examples

See the example for [IEdmFindUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser.html).

## Remarks

The result of the search is returned in the property, [IEdmFindUser.Result](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser~Result.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: An argument is invalid.

## See Also

[IEdmFindUser Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser.html)
[IEdmFindUser Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser_members.html)

## Availability

SOLIDWORKS PDM Professional 2013
