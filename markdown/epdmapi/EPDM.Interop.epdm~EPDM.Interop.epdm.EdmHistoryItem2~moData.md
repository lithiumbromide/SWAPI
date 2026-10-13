---
title: "moData Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmHistoryItem2"
member: "moData"
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem2~moData.html"
---

# moData Field

Extra data.

## Syntax

### Visual Basic

```vb
Public moData As EdmCmdData
```

### C#

```csharp
public EdmCmdData moData
```

### C++/CLI

```cpp
public:
EdmCmdData moData
```

## Remarks

The members of the structure stored in this member have different values, depending on the value of EdmHistoryItem::meType. The tables below contain the moData structure member values for each EdmHistoryItem::meType. Any members not listed in the tables are undefined for that data type.

##### EdmHistoryItem::meType = EdmHistoryType .Edmhist_FileShare

| EdmCmdData Members | Description |
| --- | --- |
| mbsStrData1 | Destination folder path |
| mlObjectID1 | Destination folder ID |

##### EdmHistoryItem::meType = EdmHistoryType .Edmhist_FileRename

| EdmCmdData Members | Description |
| --- | --- |
| mbsStrData1 | Old file name |

##### EdmHistoryItem::meType = EdmHistoryType .Edmhist_FileMove

| EdmCmdData Members | Description |
| --- | --- |
| mbsStrData1 | Source folder path |
| mbsStrData2 | Destination folder path |
| mlObjectID1 | Source folder ID |
| mlObjectID2 | Destination folder ID |

##### EdmHistoryItem::meType = EdmHistoryType .Edmhist_FileRollback

| EdmCmdData Members | Description |
| --- | --- |
| mlLongData1 | From version |
| mlLongData2 | To version |

##### EdmHistoryItem::meType = EdmHistoryType .Edmhist_FileDelete

| EdmCmdData Members | Description |
| --- | --- |
| mlObjectID1 | Parent folder ID |
| mbsStrData1 | Parent folder path |

##### EdmHistoryItem::meType = EdmHistoryType .Edmhist_FileUndelete

| EdmCmdData Members | Description |
| --- | --- |
| mlObjectID1 | Parent folder ID |
| mbsStrData1 | Parent folder path |

##### EdmHistoryItem::meType = EdmHistoryType .Edmhist_FileLabel

| EdmCmdData Members | Description |
| --- | --- |
| mbsStrData1 | Label name |
| mlObjectID1 | Label ID |

##### EdmHistoryItem::meType = EdmHistoryType .Edmhist_FileState

| EdmCmdData Members | Description |
| --- | --- |
| mbsStrData1 | Source workflow name + <newline> + source state name |
| mbsStrData2 | Destination workflow name + <newline> + destination state name |
| mlLongData1 | Transition number |

##### EdmHistoryItem::meType = EdmHistoryType .Edmhist_FileRevision

| EdmCmdData Members | Description |
| --- | --- |
| mbsStrData1 | Revision name |

##### EdmHistoryItem::meType = EdmHistoryType .Edmhist_FileColdStore

| EdmCmdData Members | Description |
| --- | --- |
| mbsStrData1 | Media name |
| mlLongData1 | Storage type |

##### EdmHistoryItem::meType = EdmHistoryType .Edmhist_FolderDelete

| EdmCmdData Members | Description |
| --- | --- |
| mbsStrData1 | Folder path |

##### EdmHistoryItem::meType = EdmHistoryType .Edmhist_FolderUndelete

| EdmCmdData Members | Description |
| --- | --- |
| mbsStrData1 | Folder path |

##### EdmHistoryItem::meType = EdmHistoryType .Edmhist_FolderCreate

| EdmCmdData Members | Description |
| --- | --- |
| mbsStrData1 | Folder path |

##### EdmHistoryItem::meType = EdmHistoryType .Edmhist_FolderCardData

| EdmCmdData Members | Description |
| --- | --- |
| mbsStrData1 | Folder path |

##### EdmHistoryItem::meType = EdmHistoryType .Edmhist_FolderRename

| EdmCmdData Members | Description |
| --- | --- |
| mbsStrData1 | Old folder name |

##### EdmHistoryItem::meType = EdmHistoryType .Edmhist_FolderMove

| EdmCmdData Members | Description |
| --- | --- |
| mbsStrData1 | From folder path |
| mbsStrData2 | To folder path |
| mlObjectID1 | From folder ID |
| mlObjectID2 | To folder ID |

##### EdmHistoryItem::meType = EdmHistoryType .Edmhist_FolderLabel

| EdmCmdData Members | Description |
| --- | --- |
| mbsStrData1 | Label name |
| mlObjectID1 | Label ID |

## See Also

[EdmHistoryItem2 Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem2.html)
[EdmHistoryItem2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem2_members.html)
