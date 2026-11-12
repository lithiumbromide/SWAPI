---
title: "HasSysRightEx Method (IEdmUserGroup6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserGroup6"
member: "HasSysRightEx"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup6~HasSysRightEx.html"
---

# HasSysRightEx Method (IEdmUserGroup6)

Gets whether this user group has the specified permission.

## Syntax

### Visual Basic

```vb
Function HasSysRightEx( _
   ByVal eRight As EdmSysPerm _
) As System.Boolean
```

### C#

```csharp
System.bool HasSysRightEx(
   EdmSysPerm eRight
)
```

### C++/CLI

```cpp
System.bool HasSysRightEx(
   EdmSysPerm eRight
)
```

### Parameters

- `eRight`: Permission to check as defined in [EdmSysPerm](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSysPerm.html)

### Return Value

True if the user group has the specified permission, false if not

## Examples

[Add and Remove User and Group from Folder (C#)](Add_and_Remove_User_and_Group_from_Folder_Example_CSharp.htm)
[Add and Remove User and Group from Folder (VB.NET)](Add_and_Remove_User_and_Group_from_Folder_Example_VBNET.htm)

## Remarks

This method supersedes [IEdmUserGroup5::HasSysRight](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5~HasSysRight.html), which checked system permissions represented as bit flags that could be ORed together. As of SOLIDWORKS PDM Professional 2010, new permissions are represented as sequentially numbered constants that cannot be ORed together. You must call this method once for each permission you want to check.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserGroup6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup6.html)
[IEdmUserGroup6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup6_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
