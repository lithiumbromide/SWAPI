---
title: "GetGroupMembershipsInFolder Method (IEdmUser9)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUser9"
member: "GetGroupMembershipsInFolder"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser9~GetGroupMembershipsInFolder.html"
---

# GetGroupMembershipsInFolder Method (IEdmUser9)

Gets all of the groups to which this user belongs and for the specified folder.

## Syntax

### Visual Basic

```vb
Function GetGroupMembershipsInFolder( _
   ByVal lFolderID As System.Integer _
) As System.Object()
```

### C#

```csharp
System.object[] GetGroupMembershipsInFolder(
   System.int lFolderID
)
```

### C++/CLI

```cpp
System.array<Object^>^ GetGroupMembershipsInFolder(
   System.int lFolderID
)
```

### Parameters

- `lFolderID`: ID of folder for which to get memberships

### Return Value

Array of [IEdmUserGroup8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup8.html) interfaces

## Examples

[Add and Remove User and Group from Folder (C#)](Add_and_Remove_User_and_Group_from_Folder_Example_CSharp.htm)
[Add and Remove User and Group from Folder (VB.NET)](Add_and_Remove_User_and_Group_from_Folder_Example_VBNET.htm)

## Remarks

This method extends [IEdmUser8::GetGroupMemberships](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser8~GetGroupMemberships.html), which only gets global group memberships. As of SOLIDWORKS PDM Professional 2011, it is possible to assign group memberships to a specific folder. This method gets folder-specific group memberships.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUser9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser9.html)
[IEdmUser9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser9_members.html)

## Availability

SOLIDWORKS PDM Professional 2011
