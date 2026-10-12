---
title: "IEdmTaskInstance Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskInstance"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html"
---

# IEdmTaskInstance Interface

Allows you to access the task instance of an add-in.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmTaskInstance
```

### C#

```csharp
public interface IEdmTaskInstance
```

### C++/CLI

```cpp
public interface class IEdmTaskInstance
```

## Examples

[Create a Task that Finds Approved Files (VB.NET)](Schedule_Task_Addin_Example_VBNET.htm)
[Create a Task that Finds Approved Files (C#)](Schedule_Task_Addin_Example_CSharp.htm)
[Create a Task that Finds Files in Workflow States (VB.NET)](Schedule_Task_to_Find_Files_in_State_Addin_Example_VBNET.htm)
[Create a Task that Finds Files in Workflow States (C#)](Schedule_Task_to_Find_Files_in_State_Addin_Example_CSharp.htm)

## Remarks

This interface inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).

An instance of the task is created when the task is launched. This interface is created in [EdmCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd.html)::mpoExtra when an add-in calls [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html) and has previously registered the hooks, [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_TaskRun, EdmCmdType.EdmCmd_TaskLaunch, EdmCmdType.EdmCmd_TaskDetails, using [IEdmCmdMgr5::AddHook](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddHook.html). After the task launches, IEdmTaskInstance can be used to prompt the user for user-defined variable values, display a data card for editing data card variables, or update the task list messages and progress bar as the task runs.

[Programming tasks](Tasks.htm) are add-ins that allow you to specify when and where to perform specific tasks.

The [definition of the task](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html) can be used to modify the task setup page.

## See Also

[IEdmTaskInstance Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[Task Add-in Sample](TaskSample.htm)
[Standard Task Add-in](StandardTaskAddIn.htm)
[IEdmTaskMgr Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskMgr.html)
