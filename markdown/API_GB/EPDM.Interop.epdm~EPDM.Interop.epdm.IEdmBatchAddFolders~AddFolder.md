---
title: "AddFolder Method (IEdmBatchAddFolders)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchAddFolders"
member: "AddFolder"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders~AddFolder.html"
---

# AddFolder Method (IEdmBatchAddFolders)

Adds a folder or a complete folder path to the batch of folders to add to the vault.

## Syntax

### Visual Basic

```vb
Sub AddFolder( _
   ByVal lParentFolderID As System.Integer, _
   ByVal bsRelativePath As System.String, _
   ByVal lParam As System.Integer, _
   Optional ByVal lEdmBatchAddFolderFlags As System.Integer, _
   Optional ByVal poData As EdmFolderData, _
   Optional ByVal lSourceFolderID As System.Integer _
)
```

### C#

```csharp
void AddFolder(
   System.int lParentFolderID,
   System.string bsRelativePath,
   System.int lParam,
   System.int lEdmBatchAddFolderFlags,
   EdmFolderData poData,
   System.int lSourceFolderID
)
```

### C++/CLI

```cpp
void AddFolder(
   System.int lParentFolderID,
   System.String^ bsRelativePath,
   System.int lParam,
   System.int lEdmBatchAddFolderFlags,
   EdmFolderData^ poData,
   System.int lSourceFolderID
)
```

### Parameters

- `lParentFolderID`: ID of parent folder to which to add the folders
- `bsRelativePath`: Name of folder or relative path of new folder
- `lParam`: Caller-defined value
- `lEdmBatchAddFolderFlags`: Combination of [EdmBatchAddFolderFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchAddFolderFlag.html) bits
- `poData`: Optional [IEdmFolderData5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolderData5.html) permission settings and card layouts are copied to the added folders
- `lSourceFolderID`: Optional ID of folder to copy; if not 0, permission settings and card layouts from the source folder with this lSourceFolderID are copied to the added folders

## Examples

See the [IEdmBatchAddFolders](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders.html) examples.

## Remarks

After calling this method, you must call [IEdmBatchAddFolders::Create](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders~Create.html) to actually add the folder to the vault.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_INVALID_NAME: The folder name contained invalid characters.

## See Also

[IEdmBatchAddFolders Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders.html)
[IEdmBatchAddFolders Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
