---
title: "GetSel Method (IEdmTaskProperties)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskProperties"
member: "GetSel"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~GetSel.html"
---

# GetSel Method (IEdmTaskProperties)

Gets the selection of objects on which to execute this task.

## Syntax

### Visual Basic

```vb
Sub GetSel( _
   ByRef ppoSel() As EdmTaskSel _
)
```

### C#

```csharp
void GetSel(
   out EdmTaskSel[] ppoSel
)
```

### C++/CLI

```cpp
void GetSel(
   [Out] array<EdmTaskSel>^ ppoSel
)
```

### Parameters

- `ppoSel`: Array of [EdmTaskSel](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskSel.html) structures; one structure for each selected object

## Remarks

The user can select the objects on which the task performs from a dialog box that is displayed when the task add-in calls [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html). The hook, [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_TaskLaunch, must be previously registered by calling [IEdmCmdMgr5::AddHook](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddHook.html) in your implementation of [IEdmAddIn5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.html). The add-in returns the user's selections in the [EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html) structures that are returned by IEdmAddIn5::OnCmd.

You can set a selection of objects directly in this task definition by calling [IEdmTaskProperties::SetSel](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetSel.html).

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTaskProperties Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html)
[IEdmTaskProperties Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties_members.html)
[Task Add-in Sample](TaskSample.htm)

## Availability

SOLIDWORKS PDM Professional 2010
