---
title: "IEdmEnumeratorVersion5 Interface Members"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVersion5_members"
member: ""
kind: "members"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5_members.html"
---

# IEdmEnumeratorVersion5 Interface Members

The following tables list the members exposed by [IEdmEnumeratorVersion5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | LabelCount | Gets the number of labels set on this file. |
| Property | RevisionCount | Gets the number of revisions of this file. |
| Property | VersionCount | Gets the number of versions of this file. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | CreateLabel | Sets a label on the latest version of this file. |
| Method | GetFileCopy | Retrieves a copy of a file with the specified version from the archive and deposits it in the specified folder. |
| Method | GetFirstLabelPosition | Starts an enumeration of the labels set on this file. |
| Method | GetFirstRevisionPosition | Starts an enumeration of the revisions set on this file. |
| Method | GetFirstVersionPosition | Starts an enumeration of the versions of this file. |
| Method | GetNextLabel | Gets the label at the next position of this enumeration. |
| Method | GetNextRevision | Gets the revision at the next position of this enumeration. |
| Method | GetNextVersion | Gets the version at the next position of this enumeration. |
| Method | GetVersion | Gets a version object with the specified version number. |
| Method | Rollback | Obsolete. Superseded by IEdmEnumeratorVersion6::Rollback2 . |

[Top](#topBookmark)

## See Also

[IEdmEnumeratorVersion5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
