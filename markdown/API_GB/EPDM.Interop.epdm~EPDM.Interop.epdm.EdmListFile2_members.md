---
title: "EdmListFile2 Structure Members"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmListFile2_members"
member: ""
kind: "members"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2_members.html"
---

# EdmListFile2 Structure Members

The following tables list the members exposed by [EdmListFile2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2.html).

## Public Fields

|  | Name | Description |
| --- | --- | --- |
| public Field | mbHasLockRights | Gets whether a file in a user's local cache can be checked out. |
| public Field | mbLocalOverwrittenVersionObsolete | Gets whether a file in a user's local cache is valid or obsolete because the file was overwritten by another user who checked out the file, modified the file, and checked in the file. |
| public Field | mbsLockComputer | Name of computer on which the file is checked out. |
| public Field | mbsLockPath | Path to the folder where the file is checked out. |
| public Field | mbsLockUser | Name of user to whom this file is checked out. |
| public Field | mbsLockViewID | GUID of the vault view where this file is checked out. |
| public Field | mbsRevisionName | Name of the file’s current revision. |
| public Field | mlFileID | ID of the file. |
| public Field | mlFolderID | ID of the file’s parent folder. |
| public Field | mlLatestVersion | Latest version of the file. |
| public Field | mlLocalVersion | Version of the file in the local cache, based on the date of the file passed to the IEdmBatchListing::AddFile method. |
| public Field | mlLockProjectID | ID of the project where this file is checked out. |
| public Field | mlParam | Caller-defined parameter that was passed to the IEdmBatchListing::AddFile method. |
| public Field | moColumnData | Column data for the selected column set. |
| public Field | moCurrentState | File’s current workflow state. |

[Top](#topBookmark)

## See Also

[EdmListFile2 Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
