---
title: "GetFirstUserPosition Method (IEdmUserGroup5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserGroup5"
member: "GetFirstUserPosition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5~GetFirstUserPosition.html"
---

# GetFirstUserPosition Method (IEdmUserGroup5)

Starts an enumeration of the users in this group.

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

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first user in the list

## Examples

[Traverse Users and Groups in Vault (C#)](Traverse_Users_and_Groups_in_Vault_Example_CSharp.htm)
[Traverse Users and Groups in Vault (VB.NET)](Traverse_Users_and_Groups_in_Vault_Example_VBNET.htm)

## Remarks

After calling this method, pass the returned position of the first user to [IEdmUserGroup5::GetNextUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5~GetNextUser.html) to get the first user in this list. Then call IEdmUserGroup5::GetNextUser repeatedly to get the rest of the users in this list.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserGroup5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5.html)
[IEdmUserGroup5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5_members.html)

## Availability

SOLIDWORKS PDM Professional version 5.2
