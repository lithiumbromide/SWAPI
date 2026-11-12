---
title: "IEdmBatchChangeState Interface Methods"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchChangeState_methods"
member: ""
kind: "methods"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState_methods.html"
---

# IEdmBatchChangeState Interface Methods

For a list of all members of this type, see [IEdmBatchChangeState members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddFile | Adds a file to this batch of files whose states you want to change or whose transitions you want to revoke. |
| Method | ChangeState | Obsolete. Superseded by IEdmBatchChangeState4::ChangeState2 . |
| Method | CreateTree | Computes the file reference tree and checks that the specified state transition can be performed for the files added to this batch using IEdmBatchChangeState::AddFile . |
| Method | GetFileList | Gets the list of files affected by the state change or transition revocation. |
| Method | SetAux | Reserved for future use. |
| Method | ShowDlg | Shows the change state or revoke transition dialog box. |

[Top](#topBookmark)

## See Also

[IEdmBatchChangeState Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
