---
title: "HasSysRightEx Method (IEdmUser7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUser7"
member: "HasSysRightEx"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser7~HasSysRightEx.html"
---

# HasSysRightEx Method (IEdmUser7)

Gets whether this user has the specified permission.

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

- `eRight`: Permission as defined in [EdmSysPerm](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSysPerm.html)

### Return Value

True if the user has the permission, false if not

## Examples

[Send Message to Users (C#)](Send_Message_to_Users_Example_CSharp.htm)
[Send Message to Users (VB.NET)](Send_Message_to_Users_Example_VBNET.htm)
[Add and Remove User and Group from Folder (C#)](Add_and_Remove_User_and_Group_from_Folder_Example_CSharp.htm)
[Add and Remove User and Group from Folder (VB.NET)](Add_and_Remove_User_and_Group_from_Folder_Example_VBNET.htm)

## Remarks

This method supersedes [IEdmUser5::HasSysRight](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5~HasSysRight.html), which checked system permissions represented as bit flags that could be ORed together. As of SOLIDWORKS PDM Professional 2010, new permissions are represented as sequentially numbered constants that cannot be ORed together. You must call this method once for each permission you want to check.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUser7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser7.html)
[IEdmUser7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser7_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
