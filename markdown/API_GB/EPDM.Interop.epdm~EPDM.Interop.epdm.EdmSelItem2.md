---
title: "EdmSelItem2 Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmSelItem2"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelItem2.html"
---

# EdmSelItem2 Structure

Contains information about a selected item.

## Syntax

### Visual Basic

```vb
Public Structure EdmSelItem2
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmSelItem2 : System.ValueType
```

### C++/CLI

```cpp
public value class EdmSelItem2 : public System.ValueType
```

## Examples

struct EdmSelItem2

{
[EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html) [meType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelItem2~meType.html);

integer [mlID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelItem2~mlID.html);
integer [mlParentID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelItem2~mlParentID.html);
integer [mlVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelItem2~mlVersion.html);
};

## Examples

[Create a Task that Finds Approved Files (VB.NET)](Schedule_Task_Addin_Example_VBNET.htm)
[Create a Task that Finds Approved Files (C#)](Schedule_Task_Addin_Example_CSharp.htm)
[Create a Task that Finds Files in Workflow States (VB.NET)](Schedule_Task_to_Find_Files_in_State_Addin_Example_VBNET.htm)
[Create a Task that Finds Files in Workflow States (C#)](Schedule_Task_to_Find_Files_in_State_Addin_Example_CSharp.htm)

## Remarks

Used by:

- oNotificationAttachments argument of [IEdmTaskInstance::SetStatus](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetStatus.html).
- poSelections argument of [IEdmTaskMgr::RunTask](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskMgr~RunTask.html).

## See Also

[EdmSelItem2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelItem2_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2010
