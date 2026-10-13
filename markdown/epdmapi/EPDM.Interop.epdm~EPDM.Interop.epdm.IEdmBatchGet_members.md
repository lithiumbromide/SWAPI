---
title: "IEdmBatchGet Interface Members"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchGet_members"
member: ""
kind: "members"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet_members.html"
---

# IEdmBatchGet Interface Members

The following tables list the members exposed by [IEdmBatchGet](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | FileCount | Gets the number of files in this batch. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddSelection | Adds one or more files or folders to the batch of files or folders to get. |
| Method | AddSelectionEx | Adds a file with the specified ID and version to the batch of files to get. |
| Method | CreateTree | Computes the file reference tree with the files added to the batch using IEdmBatchGet::AddSelection or IEdmBatchGet::AddSelectionEx . |
| Method | GetFileList | Gets a list of the files in this batch. |
| Method | GetFiles | Gets the files in the batch. |
| Method | ShowDlg | Displays a dialog in which are listed the files to get or check out. |

[Top](#topBookmark)

## See Also

[IEdmBatchGet Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
