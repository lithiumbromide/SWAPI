---
title: "GetFirstSubFolderPosition Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "GetFirstSubFolderPosition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetFirstSubFolderPosition.html"
---

# GetFirstSubFolderPosition Method (IEdmFolder5)

Starts an enumeration of the subfolders in this folder.

## Syntax

### Visual Basic

```vb
Function GetFirstSubFolderPosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstSubFolderPosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstSubFolderPosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first sub-folder in this folder

## Examples

[Get and Set Folder Permissions (VB.NET)](Get_and_Set_Folder_Permissions_Example_VBNET.htm)
[Get and Set Folder Permissions (C#)](Get_and_Set_Folder_Permissions_Example_CSharp.htm)
[Traverse Folders and Files in Vault (C#)](Traverse_Folders_and_Files_in_Vault_Example_CSharp.htm)
[Traverse Folders and Files in Vault (VB.NET)](Traverse_Folders_and_Files_in_Vault_Example_VBNET.htm)

## Remarks

After calling this method, pass the returned first subfolder position to [IEdmFolder5::GetNextSubFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetNextSubFolder.html) to get the first subfolder in the list. Then call IEdmFolder5::GetNextSubFolder repeatedly to get the rest of the subfolders in the list.

C++ users not using smart-pointer wrapper functions must release the returned pointer, IEdmPos5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)
[IEdmFolder5::GetFirstFilePosition Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetFirstFilePosition.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
