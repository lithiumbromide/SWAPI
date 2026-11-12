---
title: "AddFileByID Method (IEdmBatchDelete)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchDelete"
member: "AddFileByID"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~AddFileByID.html"
---

# AddFileByID Method (IEdmBatchDelete)

Adds a file with the specified file and folder IDs to the batch of files to be deleted.

## Syntax

### Visual Basic

```vb
Sub AddFileByID( _
   ByVal lFileID As System.Integer, _
   ByVal lFolderID As System.Integer _
)
```

### C#

```csharp
void AddFileByID(
   System.int lFileID,
   System.int lFolderID
)
```

### C++/CLI

```cpp
void AddFileByID(
   System.int lFileID,
   System.int lFolderID
)
```

### Parameters

- `lFileID`: ID of file to delete
- `lFolderID`: ID of file's parent folder

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
