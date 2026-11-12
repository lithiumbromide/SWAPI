---
title: "AddFolder Method (IEdmBatchDelete)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchDelete"
member: "AddFolder"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~AddFolder.html"
---

# AddFolder Method (IEdmBatchDelete)

Adds a folder with the specified ID or path to the batch of folders to delete.

## Syntax

### Visual Basic

```vb
Sub AddFolder( _
   ByVal oFolderIDorPath As System.Object _
)
```

### C#

```csharp
void AddFolder(
   System.object oFolderIDorPath
)
```

### C++/CLI

```cpp
void AddFolder(
   System.Object^ oFolderIDorPath
)
```

### Parameters

- `oFolderIDorPath`: ID of or path to folder to delete

## Examples

See the [IEdmBatchDelete](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete.html) examples.

## Remarks

After calling this method, call [IEdmBatchDelete::CommitDelete](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~CommitDelete.html) to delete the file from the vault.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchDelete Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete.html)
[IEdmBatchDelete Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete_members.html)

## Availability

SOLIDWORKS PDM Professional 2008
