---
title: "EdmHistoryItem Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmHistoryItem"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem.html"
---

# EdmHistoryItem Structure

Contains a history item.

## Syntax

### Visual Basic

```vb
Public Structure EdmHistoryItem
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmHistoryItem : System.ValueType
```

### C++/CLI

```cpp
public value class EdmHistoryItem : public System.ValueType
```

## Examples

struct EdmHistoryItem{
[enum EdmHistoryType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryType.html) [meType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem~meType.html);
datetime [moDate](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem~moDate.html);
integer [mlVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem~mlVersion.html);
integer [mlUserID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem~mlUserID.html);
integer [mlFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem~mlFileID.html);
integer [mlFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem~mlFolderID.html);
string [mbsItemName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem~mbsItemName.html);
string [mbsUserName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem~mbsUserName.html);
string [mbsComment](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem~mbsComment.html);
[struct EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html) [moData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem~moData.html);
};

## Examples

[Get Histories of Files (VB.NET)](Get_Histories_of_Files_Example_VBNET.htm)
[Get Histories of Files (C#)](Get_Histories_of_Files_Example_CSharp.htm)

## Remarks

Returned by [IEdmHistory](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory.html).

## See Also

[EdmHistoryItem Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
