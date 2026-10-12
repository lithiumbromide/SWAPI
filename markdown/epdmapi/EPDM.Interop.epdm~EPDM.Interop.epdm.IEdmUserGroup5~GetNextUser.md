---
title: "GetNextUser Method (IEdmUserGroup5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserGroup5"
member: "GetNextUser"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5~GetNextUser.html"
---

# GetNextUser Method (IEdmUserGroup5)

Gets the next user in the enumeration.

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

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next user (see **Remarks**)

### Return Value

[IEdmUser5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5.html)

## Examples

[Traverse Users and Groups in Vault (C#)](Traverse_Users_and_Groups_in_Vault_Example_CSharp.htm)
[Traverse Users and Groups in Vault (VB.NET)](Traverse_Users_and_Groups_in_Vault_Example_VBNET.htm)

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first user in the list, IEdmPos5. Call [IEdmUserGroup5::GetFirstUserPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5~GetFirstUserPosition.html) to obtain poPos.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the users in the list.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmUser5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserGroup5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5.html)
[IEdmUserGroup5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5_members.html)

## Availability

SOLIDWORKS PDM Professional version 5.2
