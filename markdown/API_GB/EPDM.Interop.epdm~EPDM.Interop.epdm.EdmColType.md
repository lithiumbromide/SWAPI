---
title: "EdmColType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmColType"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmColType.html"
---

# EdmColType Enumeration

Types of file listing column content; specified in the [EdmListCol structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListCol.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmColType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmColType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmColType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmCol_AttachedVersion | 10000 = As-built version |
| EdmCol_Category | 12 = File category |
| EdmCol_Configuration | 21 = Configuration name |
| EdmCol_Date | 3 = File last modified date |
| EdmCol_EdmListRetFileFlag | 30 = Combination of EdmListRetFileFlag flags |
| EdmCol_FileSize | 2 = File size |
| EdmCol_FileType | 10 = File type |
| EdmCol_FoundInVersion | 9 = Version in which the search tool found the file |
| EdmCol_LatestFileDate | 17 = File latest version date |
| EdmCol_LatestVersion | 4 = File latest version number |
| EdmCol_LockComputer | 15 = Name of computer where the file is checked out |
| EdmCol_LockedIn | 8 = Name of computer and folder path where the file is checked out |
| EdmCol_LockPath | 14 = Path to folder where the file is checked out |
| EdmCol_LockUser | 7 = Name of user who has the file checked out |
| EdmCol_LockUserID | 13 = ID of user who has the file checked out |
| EdmCol_LockViewID | 18 = ID of the file vault view where the file is checked out |
| EdmCol_Name | 1 = File name |
| EdmCol_ParentFileConfiguration | 29 = Name of the configuration referencing this file |
| EdmCol_ParentFileID | 28 = ID of file referencing this file |
| EdmCol_Path | 5 = File path |
| EdmCol_RefCount | 11 = Reference count |
| EdmCol_Shared | 19 = File share count |
| EdmCol_State | 6 = File workflow state name + newline + file workflow state icon name |
| EdmCol_StateName | 16 = File workflow state name |
| EdmCol_Variable | 0 = The column is linked to a card variable |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
