---
title: "EdmTaskSetupPage Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmTaskSetupPage"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskSetupPage.html"
---

# EdmTaskSetupPage Structure

Used by the method [IEdmTaskProperties::SetSetupPages](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetSetupPages.html).

## Syntax

### Visual Basic

```vb
Public Structure EdmTaskSetupPage
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmTaskSetupPage : System.ValueType
```

### C++/CLI

```cpp
public value class EdmTaskSetupPage : public System.ValueType
```

## Examples

struct EdmTaskSetupPage{
string [mbsPageName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskSetupPage~mbsPageName.html);
integer [mlPageHwnd](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskSetupPage~mlPageHwnd.html);
object [mpoPageImpl](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskSetupPage~mpoPageImpl.html);
};

## Examples

[Create a Task that Finds Files in Workflow States (VB.NET)](Schedule_Task_to_Find_Files_in_State_Addin_Example_VBNET.htm)
[Create a Task that Finds Files in Workflow States (C#)](Schedule_Task_to_Find_Files_in_State_Addin_Example_CSharp.htm)

## Remarks

This structure defines a task add-in's setup page in the task properties dialog box.

## See Also

[EdmTaskSetupPage Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskSetupPage_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[Programming Tasks](Tasks.htm)

## Availability

SOLIDWORKS PDM Professional 2010
