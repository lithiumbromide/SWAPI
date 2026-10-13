---
title: "EdmTaskInfo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmTaskInfo"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskInfo.html"
---

# EdmTaskInfo Structure

Used by [IEdmTaskMgr::RunTask](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskMgr~RunTask.html).

## Syntax

### Visual Basic

```vb
Public Structure EdmTaskInfo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmTaskInfo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmTaskInfo : public System.ValueType
```

## Examples

struct EdmTaskInfo{
string [mbsTaskName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskInfo~mbsTaskName.html);
long [mllShortTaskInfoFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskInfo~mllShortTaskInfoFlags.html);
integer [mlTaskID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskInfo~mlTaskID.html);
};

## See Also

[EdmTaskInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskInfo_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[Programming Tasks](Tasks.htm)
