---
title: "GetNextUser Method (IEdmUserMgr5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr5"
member: "GetNextUser"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetNextUser.html"
---

# GetNextUser Method (IEdmUserMgr5)

Gets the next user in an enumeration of all users in the vault.

## Syntax

### Visual Basic

```vb
Function GetNextUser( _
   ByVal poPos As IEdmPos5 _
) As IEdmUser5
```

### C#

```csharp
IEdmUser5 GetNextUser(
   IEdmPos5 poPos
)
```

### C++/CLI

```cpp
IEdmUser5^ GetNextUser(
   IEdmPos5^ poPos
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position in the enumeration of the next user

### Return Value

[IEdmUser5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5.html)

## Examples

[Get and Set Folder Permissions (VB.NET)](Get_and_Set_Folder_Permissions_Example_VBNET.htm)
[Get and Set Folder Permissions (C#)](Get_and_Set_Folder_Permissions_Example_CSharp.htm)
[Send Message to Users (C#)](Send_Message_to_Users_Example_CSharp.htm)
[Send Message to Users (VB.NET)](Send_Message_to_Users_Example_VBNET.htm)

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first user in the list, IEdmPos5. Call [IEdmUserMgr5::GetFirstUserPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetFirstUserPosition.html) to obtain poPos.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the users in the list.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserMgr5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5.html)
[IEdmUserMgr5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
