---
title: "HasSysRight Method (IEdmUser5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUser5"
member: "HasSysRight"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5~HasSysRight.html"
---

# HasSysRight Method (IEdmUser5)

Obsolete. Superseded by [IEdmUser7::HasSysRightEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser7~HasSysRightEx.html).

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

- `eRight`: Permissions as defined in [EdmSysRightFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSysRightFlags.html)

### Return Value

True if the user has all of the permissions, false if the user lacks one or more of the permissions

## Remarks

This method is superseded by [IEdmUser7::HasSysRightEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser7~HasSysRightEx.html).

Before SOLIDWORKS PDM Professional 2010, IEdmUser5::HasSysRight supported the bit-wise combination of system permissions. Because the number of system permissions has grown, and they do not all fit in a 32-bit integer, system permissions added in SOLIDWORKS PDM Professional 2010 and later are sequential numeric constants instead of bit flags. You must use IEdmUser7::HasSysRightEx to check permissions added in SOLIDWORKS PDM Professional 2010 and later.

This method checks both the permissions set directly on the user and the permissions inherited from the groups of which the user is a member.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- S_FALSE: The method successfully executed, but the user lacks the specified permissions.

## See Also

[IEdmUser5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5.html)
[IEdmUser5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
