---
title: "IEdmBatchChangeState Interface Members"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchChangeState_members"
member: ""
kind: "members"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState_members.html"
---

# IEdmBatchChangeState Interface Members

The following tables list the members exposed by [IEdmBatchChangeState](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Comment | Comment about this state change or transition revocation to add to the history listing. |

[Top](#topBookmark)

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
