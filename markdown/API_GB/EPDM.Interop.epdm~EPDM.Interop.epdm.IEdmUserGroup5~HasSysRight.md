---
title: "HasSysRight Method (IEdmUserGroup5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserGroup5"
member: "HasSysRight"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5~HasSysRight.html"
---

# HasSysRight Method (IEdmUserGroup5)

Obsolete. Superseded by [IEdmUserGroup6::HasSysRightEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup6~HasSysRightEx.html).

## Syntax

### Visual Basic

```vb
Function HasSysRight( _
   ByVal eRight As EdmSysRightFlags _
) As System.Boolean
```

### C#

```csharp
System.bool HasSysRight(
   EdmSysRightFlags eRight
)
```

### C++/CLI

```cpp
System.bool HasSysRight(
   EdmSysRightFlags eRight
)
```

### Parameters

- `eRight`: Combination of [EdmSysRightFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSysRightFlags.html)

### Return Value

True if the user group has all the permissions, false if not

## Remarks

This method is superseded by [IEdmUserGroup6::HasSysRightEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup6~HasSysRightEx.html).

Before SOLIDWORKS PDM Professional 2010, IEdmUserGroup5::HasSysRight supported the bit-wise combination of system permissions. Because the number of system permissions has grown, and they do not all fit in a 32-bit integer, system permissions added in SOLIDWORKS PDM Professional 2010 and later are sequential numeric constants instead of bit flags. You must use IEdmUserGroup6::HasSysRightEx to check permissions added in SOLIDWORKS PDM Professional 2010 and later.

To check individual user permissions, call [IEdmUser5::HasSysRight](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5~HasSysRight.html), which checks both permissions set directly on the user and permissions inherited from groups of which he is a member.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed, and all of the permissions are set.
- S_FALSE: The method successfully executed, but one or more of the permissions are not set.

## See Also

[IEdmUserGroup5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5.html)
[IEdmUserGroup5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5_members.html)

## Availability

SOLIDWORKS PDM Professional version 5.2
