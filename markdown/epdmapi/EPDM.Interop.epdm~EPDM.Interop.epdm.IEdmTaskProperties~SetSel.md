---
title: "SetSel Method (IEdmTaskProperties)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskProperties"
member: "SetSel"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetSel.html"
---

# SetSel Method (IEdmTaskProperties)

Sets the selection of objects on which to execute this task.

## Syntax

### Visual Basic

```vb
Sub SetSel( _
   ByVal poSel() As EdmTaskSel _
)
```

### C#

```csharp
void SetSel(
   EdmTaskSel[] poSel
)
```

### C++/CLI

```cpp
void SetSel(
   array<EdmTaskSel>^ poSel
)
```

### Parameters

- `poSel`: Array of [EdmTaskSel](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskSel.html) structures; one structure for each selected object

## Remarks

The user can select the objects on which the task performs from a dialog box that is displayed when the task add-in calls [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html). The hook, [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_TaskLaunch, must be previously registered by calling [IEdmCmdMgr5::AddHook](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddHook.html) in your implementation of [IEdmAddIn5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.html). The add-in returns the user's selections in the [EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html) structures that are returned by IEdmAddIn5::OnCmd.

You can set a selection of objects that should always be passed to the task instances by calling this method.

Call [IEdmTaskProperties::GetSel](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~GetSel.html) to get the objects set by this method.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTaskProperties Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html)
[IEdmTaskProperties Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties_members.html)
[Task Add-in Sample](TaskSample.htm)

## Availability

SOLIDWORKS PDM Professional 2010
