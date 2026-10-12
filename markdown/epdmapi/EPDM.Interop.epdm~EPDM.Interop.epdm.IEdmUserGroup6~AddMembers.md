---
title: "AddMembers Method (IEdmUserGroup6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserGroup6"
member: "AddMembers"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup6~AddMembers.html"
---

# AddMembers Method (IEdmUserGroup6)

Adds the specified users to this user group.

## Syntax

### Visual Basic

```vb
Sub AddMembers( _
   ByVal poUserIDs() As System.Integer _
)
```

### C#

```csharp
void AddMembers(
   System.int[] poUserIDs
)
```

### C++/CLI

```cpp
void AddMembers(
   System.array<int>^ poUserIDs
)
```

### Parameters

- `poUserIDs`: Array of database IDs of users to add to this user group (see **Remarks**)

## Examples

[Add and Remove User and Group from Folder (C#)](Add_and_Remove_User_and_Group_from_Folder_Example_CSharp.htm)
[Add and Remove User and Group from Folder (VB.NET)](Add_and_Remove_User_and_Group_from_Folder_Example_VBNET.htm)

## Remarks

Call IEdmUser5::[ID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5~ID.html) to populate the array of poUserIDs.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserGroup6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup6.html)
[IEdmUserGroup6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup6_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
