---
title: "IEdmBatchDelete Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchDelete"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete.html"
---

# IEdmBatchDelete Interface

Allows you to delete several files and folders from the vault at once.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBatchDelete
```

### C#

```csharp
public interface IEdmBatchDelete
```

### C++/CLI

```cpp
public interface class IEdmBatchDelete
```

## Examples

[Batch Delete Files and Folders from Vault (VB.NET)](Batch_Delete_Files_and_Folders_Example_VBNET.htm)
[Batch Delete Files and Folders from Vault (C#)](Batch_Delete_Files_and_Folders_Example_CSharp.htm)

## Remarks

This interface:

- inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).
- is extended by [IEdmBatchDelete2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete2.html).

To delete several files and folders from the vault at once:

1. Access this interface by calling [IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html), passing [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_BatchDelete as a parameter.
2. Call [IEdmBatchDelete::AddFileByID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~AddFileByID.html), [IEdmBatchDelete::AddFileByPath](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~AddFileByPath.html), or [IEdmBatchDelete::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~AddFolder.html) one or more times to add files and folders to the batch for deletion.
3. Call [IEdmBatchDelete::ComputePermissions](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~ComputePermissions.html) to prepare the delete operation.
4. Optionally call [IEdmBatchDelete2::ShowWarningDlg2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete2~ShowWarningDlg2.html) to display a message about any errors found in step 3.
5. Call [IEdmBatchDelete::CommitDelete](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~CommitDelete.html) to delete the files and folders added to the batch.
6. Optionally call [IEdmBatchDelete::ShowCommitErrorsDlg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~ShowCommitErrorsDlg.html) or [IEdmBatchDelete3::GetCommitErrors](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete3~GetCommitErrors.html) to get any errors that might have occurred in step 5.

Using IEdmBatchDelete is more efficient than calling [IEdmFolder5::DeleteFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~DeleteFile.html) or [IEdmFolder5::DeleteFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~DeleteFolder.html) multiple times.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmBatchDelete Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
