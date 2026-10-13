---
title: "IEdmTaskProperties Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskProperties"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html"
---

# IEdmTaskProperties Interface

Allows you to access the task definition of an add-in.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmTaskProperties
```

### C#

```csharp
public interface IEdmTaskProperties
```

### C++/CLI

```cpp
public interface class IEdmTaskProperties
```

## Examples

[Create a Task that Finds Approved Files (VB.NET)](Schedule_Task_Addin_Example_VBNET.htm)
[Create a Task that Finds Approved Files (C#)](Schedule_Task_Addin_Example_CSharp.htm)
[Create a Task that Finds Files in Workflow States (VB.NET)](Schedule_Task_to_Find_Files_in_State_Addin_Example_VBNET.htm)
[Create a Task that Finds Files in Workflow States (C#)](Schedule_Task_to_Find_Files_in_State_Addin_Example_CSharp.htm)

## Remarks

This interface inherits from IDispatch. See [IDispatch Interface (Automation)](http://msdn.microsoft.com/en-us/library/windows/desktop/ms221608(v=vs.85).aspx).

This interface provides the definition of a task and can be used to extend the task setup page. This interface is created in [EdmCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd.html)::mpoExtra when an add-in calls [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html) and has previously registered the hook, [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_TaskSetup, using [IEdmCmdMgr5::AddHook](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddHook.html). Use this interface in the processing of the EdmCmdType.EdmCmd_TaskSetup hook to load or store user-defined variables, load or store card variables, or set menu commands for the task setup page.

[Programming tasks](Tasks.htm) are add-ins that allow you to specify when and where to perform specific tasks.

An [instance of the task](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html) is created when the task is launched.

## See Also

[IEdmTaskProperties Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[Task Add-in Sample](TaskSample.htm)
[Standard Task Add-in](StandardTaskAddIn.htm)
[IEdmTaskMgr Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskMgr.html)
