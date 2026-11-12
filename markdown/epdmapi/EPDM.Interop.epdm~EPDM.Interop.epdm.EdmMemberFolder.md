---
title: "EdmMemberFolder Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmMemberFolder"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMemberFolder.html"
---

# EdmMemberFolder Structure

Adds a user as a member of a group to a specific folder.

## Syntax

### Visual Basic

```vb
Public Structure EdmMemberFolder
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmMemberFolder : System.ValueType
```

### C++/CLI

```cpp
public value class EdmMemberFolder : public System.ValueType
```

## Examples

struct EdmMemberFolder{
integer [mlUserID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMemberFolder~mlUserID.html);
integer [mlFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMemberFolder~mlFolderID.html);
};

## Examples

[Add and Remove User and Group from Folder (C#)](Add_and_Remove_User_and_Group_from_Folder_Example_CSharp.htm)
[Add and Remove User and Group from Folder (VB.NET)](Add_and_Remove_User_and_Group_from_Folder_Example_VBNET.htm)

## Remarks

Used by [IEdmUserGroup7::AddMembersWithFolders](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup7~AddMembersWithFolders.html).

## See Also

[EdmMemberFolder Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMemberFolder_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2011
