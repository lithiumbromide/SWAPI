---
title: "EdmFolderPermission Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmFolderPermission"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderPermission.html"
---

# EdmFolderPermission Structure

Contains permission settings.

## Syntax

### Visual Basic

```vb
Public Structure EdmFolderPermission
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmFolderPermission : System.ValueType
```

### C++/CLI

```cpp
public value class EdmFolderPermission : public System.ValueType
```

## Examples

struct EdmFolderPermission
{
integer [mlEdmRightFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderPermission~mlEdmRightFlag.html);
integer [mlFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderPermission~mlFolderID.html);
integer [mlOwnerID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderPermission~mlOwnerID.html);
[enum EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html) [meOwnerType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderPermission~meOwnerType.html);
};

## Examples

[Get and Set Folder Permissions (VB.NET)](Get_and_Set_Folder_Permissions_Example_VBNET.htm)
[Get and Set Folder Permissions (C#)](Get_and_Set_Folder_Permissions_Example_CSharp.htm)

## Remarks

Used by [IEdmUserMgr7::GetFolderPermissions](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7~GetFolderPermissions.html) and [IEdmUserMgr7::SetFolderPermissions](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7~SetFolderPermissions.html).

## See Also

[EdmFolderPermission Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFolderPermission_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2010
