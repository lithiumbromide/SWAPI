---
title: "RemoveMembers Method (IEdmUserGroup8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserGroup8"
member: "RemoveMembers"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup8~RemoveMembers.html"
---

# RemoveMembers Method (IEdmUserGroup8)

Removes the specified members from this user group.

## Syntax

### Visual Basic

```vb
Sub RemoveMembers( _
   ByVal poMemberFolders() As EdmMemberFolder _
)
```

### C#

```csharp
void RemoveMembers(
   EdmMemberFolder[] poMemberFolders
)
```

### C++/CLI

```cpp
void RemoveMembers(
   array<EdmMemberFolder>^ poMemberFolders
)
```

### Parameters

- `poMemberFolders`: Array of [EdmMemberFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMemberFolder.html) structures; one structure for each member to remove from this user group

## Examples

[Add and Remove User and Group from Folder (C#)](Add_and_Remove_User_and_Group_from_Folder_Example_CSharp.htm)
[Add and Remove User and Group from Folder (VB.NET)](Add_and_Remove_User_and_Group_from_Folder_Example_VBNET.htm)

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserGroup8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup8.html)
[IEdmUserGroup8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup8_members.html)

## Availability

SOLIDWORKS PDM Professional 2012
