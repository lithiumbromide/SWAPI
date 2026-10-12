---
title: "IEdmBatchDelete Interface Members"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchDelete_members"
member: ""
kind: "members"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete_members.html"
---

# IEdmBatchDelete Interface Members

The following tables list the members exposed by [IEdmBatchDelete](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddFileByID | Adds a file with the specified file and folder IDs to the batch of files to be deleted. |
| Method | AddFileByPath | Adds a file with the specified path to the batch of files to be deleted. |
| Method | AddFolder | Adds a folder with the specified ID or path to the batch of folders to delete. |
| Method | CommitDelete | Deletes the files and folders added to the batch by IEdmBatchDelete::AddFileByID , IEdmBatchDelete::AddFileByPath , and/or IEdmBatchDelete::AddFolder . |
| Method | ComputePermissions | Specifies whether files or folders should be permanently deleted or moved to the recycle bin. |
| Method | ShowCommitErrorsDlg | Shows a dialog box containing the errors that occurred during IEdmBatchDelete::CommitDelete . |
| Method | ShowWarningDlg | Obsolete. Superseded by IEdmBatchDelete2::ShowWarningDlg2 . |

[Top](#topBookmark)

## See Also

[IEdmBatchDelete Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
