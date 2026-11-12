---
title: "IEdmVersion5 Interface Members"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVersion5_members"
member: ""
kind: "members"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5_members.html"
---

# IEdmVersion5 Interface Members

The following tables list the members exposed by [IEdmVersion5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Comment | Gets the comment that is entered during the check-in of this version. |
| Property | FileDate | Gets the modification date for this version. |
| Property | FileSize | Gets the file size for this version. |
| Property | HasRevision | Gets whether this version has one or more revisions. |
| Property | User | Gets the user who checked in this version. |
| Property | UserID | Gets the ID of the user who checked in this version. |
| Property | VersionDate | Gets the time when this version was created. |
| Property | VersionNo | Gets the version number of this version. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetFileCopy | Retrieves from the archive a copy of this version of a file and places it in the specified location. |
| Method | GetFirstRevisionPosition | Starts an enumeration of the revisions of this version. |
| Method | GetNextRevision | Gets the next revision set on this version in an enumeration. |
| Method | Rollback | Obsolete. Superseded by IEdmVersion6::Rollback2 . |

[Top](#topBookmark)

## See Also

[IEdmVersion5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
