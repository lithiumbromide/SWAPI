---
title: "EdmUserData2 Structure Fields"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUserData2_fields"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData2_fields.html"
---

# EdmUserData2 Structure Fields

For a list of all members of this type, see [EdmUserData2 members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData2_members.html).

## Public Fields

|  | Name | Description |
| --- | --- | --- |
| public Field | mbsColumnView | Name of the column view that the user should see in File Explorer file listings. |
| public Field | mbsCompleteName | Complete user name. |
| public Field | mbsEmail | Email address. |
| public Field | mbsInitials | User's initials. |
| public Field | mbsPassword | User's password in SOLIDWORKS PDM Professional. |
| public Field | mbsUserData | Arbitrary text to associate with the user. |
| public Field | mbsUserName | User's login name in SOLIDWORKS PDM Professional. |
| public Field | mhStatus | HRESULT code containing the status of the creation of the user. |
| public Field | mlFlags | Combination of EdmUserDataFlags flags. |
| public Field | mlUserID | Database ID of the just-created user. |
| public Field | moSysPerms | User's system permissions. |
| public Field | mpoUser | User's interface if mlFlags contains the edmUserDataFlags.edmudf_GetInterface and mhStatus is S_OK (0), otherwise the pointer is null. |

[Top](#topBookmark)

## See Also

[EdmUserData2 Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData2.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
