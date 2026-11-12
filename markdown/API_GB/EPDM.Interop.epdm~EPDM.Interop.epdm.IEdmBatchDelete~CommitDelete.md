---
title: "CommitDelete Method (IEdmBatchDelete)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchDelete"
member: "CommitDelete"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~CommitDelete.html"
---

# CommitDelete Method (IEdmBatchDelete)

Deletes the files and folders added to the batch by [IEdmBatchDelete::AddFileByID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~AddFileByID.html), [IEdmBatchDelete::AddFileByPath](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~AddFileByPath.html), and/or [IEdmBatchDelete::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~AddFolder.html).

## Syntax

### Visual Basic

```vb
Function CommitDelete( _
   ByVal hParentWnd As System.Integer, _
   Optional ByVal poCallback As EdmCallback _
) As System.Boolean
```

### C#

```csharp
System.bool CommitDelete(
   System.int hParentWnd,
   EdmCallback poCallback
)
```

### C++/CLI

```cpp
System.bool CommitDelete(
   System.int hParentWnd,
   EdmCallback^ poCallback
)
```

### Parameters

- `hParentWnd`: Parent window handle that is passed to add-ins that are notified about file or folder deletions from the vault
- `poCallback`: Optional pointer to a class that implements [IEdmCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback.html) to provide delete progress feedback to the user

### Return Value

True if no errors occurred, false if errors occurred

## Examples

See the [IEdmBatchDelete](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete.html) examples.

## Remarks

Before calling this method, you must call [IEdmBatchDelete::ComputePermissions](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~ComputePermissions.html).

If errors occurred during IEdmBatchDelete::CommitDelete, call [IEdmBatchDelete::ShowCommitErrorsDlg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~ShowCommitErrorsDlg.html) or [IEdmBatchDelete3::GetCommitErrors](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete3~GetCommitErrors.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_NOT_INITIALIZED: IEdmBatchDelete::ComputePermissions has not been called.

## See Also

[IEdmBatchDelete Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete.html)
[IEdmBatchDelete Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete_members.html)

## Availability

SOLIDWORKS PDM Professional 2008
