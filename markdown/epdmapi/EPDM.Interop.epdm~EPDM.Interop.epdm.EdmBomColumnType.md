---
title: "EdmBomColumnType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBomColumnType"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomColumnType.html"
---

# EdmBomColumnType Enumeration

Types of Bill of Material (BOM) column content; specified in [EdmBomColumn](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomColumn.html) and in calls to [IEdmBomCell:GetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomCell~GetVar.html), and [IEdmBomCell::SetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomCell~SetVar.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmBomColumnType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmBomColumnType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmBomColumnType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmBomCol_Configuration | 21 = Name of the current configuration |
| EdmBomCol_Date | 3 = Modified date of file |
| EdmBomCol_DocType | 12 = Document |
| EdmBomCol_FileSize | 2 = File size in bytes |
| EdmBomCol_FileType | 10 = File type |
| EdmBomCol_FoundInVersion | 9 = Version where found |
| EdmBomCol_ID | 23 = File ID |
| EdmBomCol_LatestFileDate | 17 = File date of the latest version |
| EdmBomCol_LatestVersion | 4 = Latest version number of the file |
| EdmBomCol_LockDomain | 15 = Name of computer where file is checked out |
| EdmBomCol_LockedIn | 8 = Computer name and path of checked-out file |
| EdmBomCol_LockPath | 14 = File path of checked-out file |
| EdmBomCol_LockUser | 7 = Name of user who has checked out the file |
| EdmBomCol_LockUserID | 13 = ID of user who has checked out the file |
| EdmBomCol_LockViewID | 18 = ID of vault view where file is checked out |
| EdmBomCol_Name | 1 = File or folder name |
| EdmBomCol_PartNumber | 24 = Document name, configuration name, or user-specified name; used in BOM lists |
| EdmBomCol_Path | 5 = Path to file folder |
| EdmBomCol_RefCount | 11 = Reference count or BOM Quantity |
| EdmBomCol_RefCountNoBomQty | 25 = Reference count that is not multiplied by BOM quantity |
| EdmBomCol_RefVariable | 22 = Variable set on a reference to the file, e.g., position number, cut length, etc. |
| EdmBomCol_Shared | 19 = Number of folders in which the file is shared |
| EdmBomCol_State | 6 = File workflow state name + new line + file workflow state icon name |
| EdmBomCol_StateName | 16 = File workflow state name |
| EdmBomCol_Variable | 0 = This column is linked to a card variable |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
