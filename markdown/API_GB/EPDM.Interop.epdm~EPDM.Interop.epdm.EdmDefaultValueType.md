---
title: "EdmDefaultValueType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmDefaultValueType"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDefaultValueType.html"
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
| Edmdef_CreatedByUser | 8 = ID of user who created the document |
| Edmdef_CreatedByUserData | 21 = User data of the user who created the file |
| Edmdef_CreatedByUserFullName | 22 = Full name of the user who created the file |
| Edmdef_CreatedByUserInitials | 20 = Initials of the user who created the file |
| Edmdef_CurrentStatus | 12 = Name of the document's current status |
| Edmdef_CurrentStatusDescription | 15 = Description of the document's current status |
| Edmdef_CurrentTime | 2 = Current time |
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
| Edmdef_LockedByUser | 9 = ID of the user who currently has the document checked out |
| Edmdef_LockedByUserData | 24 = User data of the user who checked out the file |
| Edmdef_LockedByUserFullName | 22 = Full name of the user who checked out the file |
| Edmdef_LockedByUserInitials | 23 = Initials of the user who locked the file |
| Edmdef_LoggedInUserData | 27 = User data of the logged in user |
| Edmdef_LoggedInUserFullName | 3 = ID of currently logged in user |
| Edmdef_LoggedInUserInitials | 26 = Initials of the logged in user |
| Edmdef_LoggedInUserName | 3 = ID of the currently logged in user |
| Edmdef_NoDefaultValue | 0 = No default value |
| Edmdef_SerialNumber | 1003 = The control is connected to a serial number |
| Edmdef_String | 1001 = The control has a fixed string as a default value |
| Edmdef_TodaysDate | 1 = Today's date |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
