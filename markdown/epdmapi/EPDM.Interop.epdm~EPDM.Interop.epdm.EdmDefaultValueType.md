---
title: "EdmDefaultValueType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmDefaultValueType"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDefaultValueType.html"
---

# EdmDefaultValueType Enumeration

Default value types in SOLIDWORKS PDM Professional; used in calls to [IEdmCardViewCallback6::GetCtrlData](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6~GetCtrlData.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmDefaultValueType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmDefaultValueType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmDefaultValueType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Edmdef_CreatedByUser | 8 = ID of created-by user |
| Edmdef_CreatedByUserAddress | 48 = Address of created-by user |
| Edmdef_CreatedByUserCity | 50 = City of created-by user |
| Edmdef_CreatedByUserCompany | 44 = Company of created-by user |
| Edmdef_CreatedByUserCountry | 52 = Country of created-by user |
| Edmdef_CreatedByUserData | 21 = User data of created-by user |
| Edmdef_CreatedByUserData2 | 39 = User data of created-by user |
| Edmdef_CreatedByUserData3 | 40 = User data of created-by user |
| Edmdef_CreatedByUserDepartment | 45 = Company department of created-by user |
| Edmdef_CreatedByUserEmail | 36 = Email of created-by user |
| Edmdef_CreatedByUserEmail2 | 37 = Email of created-by user |
| Edmdef_CreatedByUserEmail3 | 38 = Email of created-by user |
| Edmdef_CreatedByUserFirstName | 31 = First name of created-by user |
| Edmdef_CreatedByUserFullName | 22 = Full name of created-by user |
| Edmdef_CreatedByUserHomePhone | 42 = Home phone of created-by user |
| Edmdef_CreatedByUserInitials | 20 = Initials of created-by user |
| Edmdef_CreatedByUserJobTitle | 46 = Job title of created-by user |
| Edmdef_CreatedByUserLastName | 32 = Last name of created-by user |
| Edmdef_CreatedByUserMiddleName | 33 = Middle name of created-by user |
| Edmdef_CreatedByUserMobilePhone | 43 = Mobile phone of created-by user |
| Edmdef_CreatedByUserOffice | 47 = Office of created-by user |
| Edmdef_CreatedByUserPrefix | 34 = Prefix of created-by user |
| Edmdef_CreatedByUserState | 51 = State of created-by user |
| Edmdef_CreatedByUserSuffix | 35 = Suffix of created-by user |
| Edmdef_CreatedByUserWorkPhone | 41 = Work phone of created-by user |
| Edmdef_CreatedByUserZipCode | 49 = Zip code of created-by user |
| Edmdef_CurrentStatus | 12 = Name of the document's current status |
| Edmdef_CurrentStatusDescription | 15 = Description of the document's current status |
| Edmdef_CurrentTime | 2 = Show current time |
| Edmdef_DocumentPath | 6 = File path of the document |
| Edmdef_FileCardVariable | 1005 = The control gets a default value from the file card |
| Edmdef_Filename | 18 = Name of the document file |
| Edmdef_FileNameNoExt | 28 = File name without the extension. |
| Edmdef_FolderCardVariable | 1004 = The control gets a default value from the folder card |
| Edmdef_LastLabel | 7 = Last label placed on the document |
| Edmdef_LastRevComment | 4 = Last revision comment for the document |
| Edmdef_LastTransComment | 5 = Last transition comment for the document |
| Edmdef_LastTransitionXByUser | 11 = ID of the last user to perform a certain transition on the document |
| Edmdef_LastVersion | 10 = Current version number |
| Edmdef_LastVersionInStatusX | 13 = Version of document the last time it was in a certain workflow state |
| Edmdef_LastVersionInTransitionX | 14 = Version of document the last time it was subject to a certain workflow transition |
| Edmdef_LatestTransition | 16 = Name of the latest transition |
| Edmdef_LatestTransitionDesc | 17 = Description of the latest transition |
| Edmdef_LockedByUser | 9 = ID of the locked-by user |
| Edmdef_LockedByUserAddress | 92 = Address of the locked-by user |
| Edmdef_LockedByUserCity | 94 = City of the locked-by user |
| Edmdef_LockedByUserCompany | 88 = Company of the locked-by user |
| Edmdef_LockedByUserCountry | 96 = Country of the locked-by user |
| Edmdef_LockedByUserData | 24 = User data of the locked-by user |
| Edmdef_LockedByUserData2 | 83 = User data of the locked-by user |
| Edmdef_LockedByUserData3 | 84 = User data of the locked-by user |
| Edmdef_LockedByUserDepartment | 89 = Department of the locked-by user |
| Edmdef_LockedByUserEmail | 80 = Email of the locked-by user |
| Edmdef_LockedByUserEmail2 | 81 = Email of the locked-by user |
| Edmdef_LockedByUserEmail3 | 82 = Email of the locked-by user |
| Edmdef_LockedByUserFirstName | 75 = First name of the locked-by user |
| Edmdef_LockedByUserFullName | 22 = Full name of the locked-by user |
| Edmdef_LockedByUserHomePhone | 86 = Home phone of the locked-by user |
| Edmdef_LockedByUserInitials | 23 = Initials of the locked-by user |
| Edmdef_LockedByUserJobTitle | 90 = Job title of the locked-by user |
| Edmdef_LockedByUserLastName | 76 = Last name of the locked-by user |
| Edmdef_LockedByUserMiddleName | 77 = Middle name of the locked-by user |
| Edmdef_LockedByUserMobilePhone | 87 = Mobile phone of the locked-by user |
| Edmdef_LockedByUserOffice | 91 = Office of the locked-by user |
| Edmdef_LockedByUserPrefix | 78 = Prefix of the locked-by user |
| Edmdef_LockedByUserState | 95 = State of the locked-by user |
| Edmdef_LockedByUserSuffix | 79 = Suffix of the locked-by user |
| Edmdef_LockedByUserWorkPhone | 85 = Work phone of the locked-by user |
| Edmdef_LockedByUserZipCode | 93 = Zip code of the locked-by user |
| Edmdef_LoggedInUserAddress | 70 = Address of the logged-in user |
| Edmdef_LoggedInUserCity | 72 = City of the logged-in user |
| Edmdef_LoggedInUserCompany | 66 = Company of the logged-in user |
| Edmdef_LoggedInUserCountry | 74 = Country of the logged-in user |
| Edmdef_LoggedInUserData | 27 = User data of the logged-in user |
| Edmdef_LoggedInUserData2 | 61 = User data of the logged-in user |
| Edmdef_LoggedInUserData3 | 62 = User data of the logged-in user |
| Edmdef_LoggedInUserDepartment | 67 = Department of the logged-in user |
| Edmdef_LoggedInUserEmail | 58 = Email of the logged-in user |
| Edmdef_LoggedInUserEmail2 | 59 = Email of the logged-in user |
| Edmdef_LoggedInUserEmail3 | 60 = Email of the logged-in user |
| Edmdef_LoggedInUserFirstName | 53 = First name of the logged-in user |
| Edmdef_LoggedInUserFullName | 3 = ID of the current logged-in user |
| Edmdef_LoggedInUserHomePhone | 64 = Home phone of the logged-in user |
| Edmdef_LoggedInUserInitials | 26 = Initials of the logged-in user |
| Edmdef_LoggedInUserJobTitle | 68 = Job title of the logged-in user |
| Edmdef_LoggedInUserLastName | 54 = Last name of the logged-in user |
| Edmdef_LoggedInUserMiddleName | 55 = Middle name of the logged-in user |
| Edmdef_LoggedInUserMobilePhone | 65 = Mobile phone of the logged-in user |
| Edmdef_LoggedInUserName | 3 = ID of the current logged-in user |
| Edmdef_LoggedInUserOffice | 69 = Office of the logged-in user |
| Edmdef_LoggedInUserPrefix | 56 = Prefix of the logged-in user |
| Edmdef_LoggedInUserState | 73 = State of the logged-in user |
| Edmdef_LoggedInUserSuffix | 57 = Suffix of the logged-in user |
| Edmdef_LoggedInUserWorkPhone | 63 = Work phone of the logged-in user |
| Edmdef_LoggedInUserZipCode | 71 = Zip code of the logged-in user |
| Edmdef_NoDefaultValue | 0 = No default value |
| Edmdef_SerialNumber | 1003 = The control is connected to a serial number |
| Edmdef_String | 1001 = The control has a fixed string as a default value |
| Edmdef_TodaysDate | 1 = Show today's date |
| Edmdef_UserListAddress | 128 = Addresses of all users |
| Edmdef_UserListCity | 130 = Cities of all users |
| Edmdef_UserListCompany | 124 = Companies of all users |
| Edmdef_UserListCountry | 132 = Countries of all users |
| Edmdef_UserListData2 | 119 = User data of all users |
| Edmdef_UserListData3 | 120 = User data of all users |
| Edmdef_UserListDepartment | 125 = Departments of all users |
| Edmdef_UserListEmail | 116 = Emails of all users |
| Edmdef_UserListEmail2 | 117 = Emails of all users |
| Edmdef_UserListEmail3 | 118 = Emails of all users |
| Edmdef_UserListFirstName | 111 = First names of all users |
| Edmdef_UserListHomePhone | 122 = Home phones of all users |
| Edmdef_UserListJobTitle | 126 = Job titles of all users |
| Edmdef_UserListLastName | 112 = Last names of all users |
| Edmdef_UserListMiddleName | 113 = Middle names of all users |
| Edmdef_UserListMobilePhone | 123 = Mobile phones of all users |
| Edmdef_UserListOffice | 127 = Offices of all users |
| Edmdef_UserListPrefix | 114 = Prefixes of all users |
| Edmdef_UserListState | 131 = States of all users |
| Edmdef_UserListSuffix | 115 = Suffixes of all users |
| Edmdef_UserListWorkPhone | 121 = Work phones of all users |
| Edmdef_UserListZipCode | 129 = Zip codes of all users |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
