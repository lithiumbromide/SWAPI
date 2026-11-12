---
title: "EdmListFile Structure Fields"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmListFile_fields"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile_fields.html"
---

# EdmListFile Structure Fields

For a list of all members of this type, see [EdmListFile members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile_members.html).

## Public Fields

|  | Name | Description |
| --- | --- | --- |
| public Field | mbsLockComputer | Name of computer on which the file is checked out. |
| public Field | mbsLockPath | Path to the folder where the file is checked out. |
| public Field | mbsLockUser | Name of user who has the file checked out. |
| public Field | mbsRevisionName | Name of the file’s current revision. |
| public Field | mlFileID | ID of the file. |
| public Field | mlFolderID | ID of the file’s parent folder. |
| public Field | mlLatestVersion | Latest version of the file. |
| public Field | mlLocalVersion | Version of the file in the local cache, based on the date of the file passed to the IEdmBatchListing::AddFile method. |
| public Field | mlParam | Caller-defined parameter that was passed to the IEdmBatchListing::AddFile method. |
| public Field | moColumnData | Column data for the selected column set. |
| public Field | moCurrentState | File’s current workflow state. |

[Top](#topBookmark)

## See Also

[EdmListFile Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
