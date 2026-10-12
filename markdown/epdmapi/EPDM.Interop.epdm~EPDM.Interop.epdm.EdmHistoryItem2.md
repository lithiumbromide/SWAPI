---
title: "EdmHistoryItem2 Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmHistoryItem2"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem2.html"
---

# EdmHistoryItem2 Structure

Contains a history item.

## Syntax

### Visual Basic

```vb
Public Structure EdmHistoryItem2
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmHistoryItem2 : System.ValueType
```

### C++/CLI

```cpp
public value class EdmHistoryItem2 : public System.ValueType
```

## Examples

struct EdmHistoryItem{
[enum EdmHistoryType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryType.html) [meType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem2~meType.html);
datetime [moDate](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem2~moDate.html);
integer [mlVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem2~mlVersion.html);
integer [mlUserID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem2~mlUserID.html);
integer [mlFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem2~mlFileID.html);
integer [mlFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem2~mlFolderID.html);
string [mbsItemName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem2~mbsItemName.html);
string [mbsUserName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem2~mbsUserName.html);
string [mbsComment](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem2~mbsComment.html);
[struct EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html) [moData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem2~moData.html);
string [mbsDetails](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem2~mbsDetails.html);
};

## See Also

[EdmHistoryItem2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem2_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
