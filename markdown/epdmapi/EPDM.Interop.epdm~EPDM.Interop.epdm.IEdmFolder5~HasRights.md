---
title: "HasRights Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "HasRights"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~HasRights.html"
---

# HasRights Method (IEdmFolder5)

Obsolete. Superseded by [IEdmFolder5::HasRightsEx.](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~HasRightsEx.html)

## Syntax

### Visual Basic

```vb
Sub HasRights( _
   ByVal lRights As System.Integer, _
   ByRef plFileID As System.Integer _
)
```

### C#

```csharp
void HasRights(
   System.int lRights,
   ref System.int plFileID
)
```

### C++/CLI

```cpp
void HasRights(
   System.int lRights,
   System.int% plFileID
)
```

### Parameters

- `lRights`: Combination of [EdmRightFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRightFlags.html) bits
- `plFileID`: ID of file to check

## Remarks

This method is superseded by [IEdmFolder5::HasRightsEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~HasRightsEx.html), which provides the ability to check rights on just this folder. Programs that do not need backwards compatibility with SOLIDWORKS PDM Professional 5.2 should use the new method.

This method takes into account both the rights set explicitly on the user and those rights that are inherited from groups of which the user is a member.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_PERMISSION_DENIED: The user lacks one or more of the specified rights.

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
