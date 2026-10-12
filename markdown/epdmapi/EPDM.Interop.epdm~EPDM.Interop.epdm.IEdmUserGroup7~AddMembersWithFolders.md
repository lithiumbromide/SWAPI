---
title: "AddMembersWithFolders Method (IEdmUserGroup7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserGroup7"
member: "AddMembersWithFolders"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup7~AddMembersWithFolders.html"
---

# AddMembersWithFolders Method (IEdmUserGroup7)

Adds the specified members of this user group to the specified folders.

## Syntax

### Visual Basic

```vb
Sub AddMembersWithFolders( _
   ByVal poMemberFolders() As EdmMemberFolder _
)
```

### C#

```csharp
void AddMembersWithFolders(
   EdmMemberFolder[] poMemberFolders
)
```

### C++/CLI

```cpp
void AddMembersWithFolders(
   array<EdmMemberFolder>^ poMemberFolders
)
```

### Parameters

- `poMemberFolders`: Array of [EdmMemberFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMemberFolder.html) structures; one structure for each member folder to add to this user group

## Examples

[Add and Remove User and Group from Folder (C#)](Add_and_Remove_User_and_Group_from_Folder_Example_CSharp.htm)
[Add and Remove User and Group from Folder (VB.NET)](Add_and_Remove_User_and_Group_from_Folder_Example_VBNET.htm)

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserGroup7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup7.html)
[IEdmUserGroup7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup7_members.html)

## Availability

SOLIDWORKS PDM Professional 2011
