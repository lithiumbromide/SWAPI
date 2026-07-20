---
title: "EdmSearchToken Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmSearchToken"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSearchToken.html"
---

# EdmSearchToken Enumeration

Values that determine which search criteria to set.

## Syntax

### Visual Basic

```vb
Public Enum EdmSearchToken
   Inherits System.Enum
```

### C#

```csharp
public enum EdmSearchToken : System.Enum
```

### C++/CLI

```cpp
public enum class EdmSearchToken : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Edmstok_AllVersions | 2 = VT_BOOL; search all versions of a file |
| Edmstok_Category | 44 = VT_BSTR; search for files in this category |
| Edmstok_ContentText | 36 = VT_BSTR; search for this string in the file body itself; this requires that the indexing service has been enabled in the administration tool |
| Edmstok_ContentTextExact | 40 = VT_BOOL; find only exact matches of the content string, not individual words |
| Edmstok_ContentTextInBody | 37 = VT_BOOL; do content search in the file body |
| Edmstok_ContentTextInProperties | 38 = VT_BOOL; do content search in the file custom properties |
| Edmstok_ContentTextOr | 39 = VT_BOOL; search for any words, instead of all of the words, in the content search string |
| Edmstok_FindFiles | 31 = VT_BOOL; return files in the result |
| Edmstok_FindFolders | 32 = VT_BOOL; return folders in the result |
| Edmstok_FindItems | 41 = VT_BOOL; return items in the search result |
| Edmstok_FolderID | 5 = VT_I4; ID of folder to start the search in |
| Edmstok_FolderPath | 4 = VT_BSTR; search starting in this folder path |
| Edmstok_HexSearchID | 50 = VT_BSTR; search by hexadecimal search ID |
| Edmstok_HistoryAfter | 34 = VT_DATE; search history after this date |
| Edmstok_HistoryBefore | 33 = VT_DATE; search history before this date |
| Edmstok_HistoryString | 25 = VT_BSTR; search for string in file history |
| Edmstok_HistoryStringConfiguration | 43 = VT_BOOL; search for keyword among configuration names |
| Edmstok_HistoryStringFileName | 42 = VT_BOOL; search for keyword among file names |
| Edmstok_HistoryStringLabels | 27 = VT_BOOL; search labels for the history string |
| Edmstok_HistoryStringRevisionComment | 29 = VT_BOOL; search revisions comments for the history string |
| Edmstok_HistoryStringStateComment | 28 = VT_BOOL; search workflow state change comments for the history string |
| Edmstok_HistoryStringVariableValues | 30 = VT_BOOL; search variable values for the history string |
| Edmstok_HistoryStringVersionComment | 26 = VT_BOOL; search version comments for the history string |
| Edmstok_Label | 20 = VT_BSTR; search for this string in labels |
| Edmstok_LabelAfter | 24 = VT_DATE; search for labels set after this date |
| Edmstok_LabelBefore | 23 = VT_DATE; search for labels set before this date |
| Edmstok_LabelByUser | 22 = VT_BSTR; search for files where a user with this name created a label |
| Edmstok_LabelComment | 21 = VT_BOOL; search for the label string in the comment |
| Edmstok_Locked | 6 = VT_BOOL; search for checked out files |
| Edmstok_LockedBy | 8 = VT_BSTR; search for files checked out by users with this name |
| Edmstok_LoggedInUser | 47 = VT_BSTR; search for this logged in user |
| Edmstok_LoggedOutUser | 48 = VT_BSTR; search for this logged out user |
| Edmstok_MigratedFiles | 51 = VT_BOOL; search only in imported files |
| Edmstok_Name | 3 = VT_BSTR; search for file or folder by name |
| Edmstok_PrivateStateFiles | 45 = VT_BSTR; search for files in the vault that have not been checked in yet |
| Edmstok_Recursive | 1 = VT_BOOL; search subfolders recursively |
| Edmstok_RevisionNo | 46 = VT_I4; search by revision number |
| Edmstok_SearchID | 49 = VT_I4; search by search ID |
| Edmstok_StateAfter | 19 = VT_DATE; only find files where a state change was made after this date |
| Edmstok_StateBefore | 18 = VT_DATE; only find files where a state change was made before this date |
| Edmstok_StateByUser | 17 = VT_BSTR; find files where a user with this name has changed workflow state |
| Edmstok_StateHistoric | 16 = VT_BOOL; search in historic states, not just the latest state |
| Edmstok_StateID | 15 = VT_I4; only find files in the workflow state with this ID |
| Edmstok_StateName | 14 = VT_BSTR; only find files in workflow states with this name |
| Edmstok_Unlocked | 7 = VT_BOOL; search for checked in files |
| Edmstok_VersionComment | 10 = VT_BSTR; search for files with this version comment |
| Edmstok_VersionsAfter | 13 = VT_DATE; only find files that have been checked in after this date |
| Edmstok_VersionsBefore | 12 = VT_DATE; only find files that have been checked in before this date |
| Edmstok_VersionsByUser | 11 = VT-BSTR; only find files that have been checked in by a user with this name |
| Edmstok_WorkflowName | 35 = VT_BSTR; search for files part of this workflow |

## Remarks

Used by

[IEdmSearch6::GetToken](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch6~GetToken.html)

and

[IEdmSearch6::SetToken](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch6~SetToken.html)

.

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
