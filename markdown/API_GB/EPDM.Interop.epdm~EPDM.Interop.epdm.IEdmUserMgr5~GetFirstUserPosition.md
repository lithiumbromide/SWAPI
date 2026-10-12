---
title: "GetFirstUserPosition Method (IEdmUserMgr5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr5"
member: "GetFirstUserPosition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetFirstUserPosition.html"
---

# GetFirstUserPosition Method (IEdmUserMgr5)

Starts an enumeration of the users in the vault.

## Syntax

### Visual Basic

```vb
Function GetFirstUserPosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstUserPosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstUserPosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first user in the enumeration

## Examples

[Get and Set Folder Permissions (VB.NET)](Get_and_Set_Folder_Permissions_Example_VBNET.htm)
[Get and Set Folder Permissions (C#)](Get_and_Set_Folder_Permissions_Example_CSharp.htm)
[Send Message to Users (C#)](Send_Message_to_Users_Example_CSharp.htm)
[Send Message to Users (VB.NET)](Send_Message_to_Users_Example_VBNET.htm)

## Remarks

After calling this method, pass the returned position of the first user to [IEdmUserMgr5::GetNextUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5~GetNextUser.html) to get the first user in this list. Then call IEdmUserMgr5::GetNextUser repeatedly to get the rest of the users.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserMgr5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5.html)
[IEdmUserMgr5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
