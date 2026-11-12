---
title: "ComputePermissions Method (IEdmBatchDelete)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchDelete"
member: "ComputePermissions"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~ComputePermissions.html"
---

# ComputePermissions Method (IEdmBatchDelete)

Specifies whether files or folders should be permanently deleted or moved to the recycle bin.

## Syntax

### Visual Basic

```vb
Function ComputePermissions( _
   ByVal bDestroy As System.Boolean, _
   Optional ByVal poCallback As EdmCallback _
) As System.Boolean
```

### C#

```csharp
System.bool ComputePermissions(
   System.bool bDestroy,
   EdmCallback poCallback
)
```

### C++/CLI

```cpp
System.bool ComputePermissions(
   System.bool bDestroy,
   EdmCallback^ poCallback
)
```

### Parameters

- `bDestroy`: True to permanently delete files and folders, false to move files and folders to the recycle bin
- `poCallback`: Optional pointer to a class that implements [IEdmCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback.html) to provide delete progress feedback to the user

### Return Value

True if no errors occurred, false otherwise

## Examples

See the [IEdmBatchDelete](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete.html) examples.

## Remarks

Before calling this method, you must add files and folders to the batch using [IEdmBatchDelete::AddFileByID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~AddFileByID.html), [IEdmBatchDelete::AddFileByPath](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~AddFileByPath.html), and [IEdmBatchDelete::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~AddFolder.html).

If errors occurred during IEdmBatchDelete::ComputePermissions, call [IEdmBatchDelete::ShowWarningDlg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~ShowWarningDlg.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchDelete Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete.html)
[IEdmBatchDelete Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete_members.html)

## Availability

SOLIDWORKS PDM Professional 2008
