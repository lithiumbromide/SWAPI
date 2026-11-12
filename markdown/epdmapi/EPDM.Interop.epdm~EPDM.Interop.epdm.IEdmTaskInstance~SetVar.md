---
title: "SetVar Method (IEdmTaskInstance)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskInstance"
member: "SetVar"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetVar.html"
---

# SetVar Method (IEdmTaskInstance)

Sets the value of a card variable created in the administration tool.

## Syntax

### Visual Basic

```vb
Sub SetVar( _
   ByVal oVarIDorName As System.Object, _
   ByVal oValue As System.Object _
)
```

### C#

```csharp
void SetVar(
   System.object oVarIDorName,
   System.object oValue
)
```

### C++/CLI

```cpp
void SetVar(
   System.Object^ oVarIDorName,
   System.Object^ oValue
)
```

### Parameters

- `oVarIDorName`: Database ID or name of the variable for which to set a value (see **Remarks**)
- `oValue`: Value to set

## Remarks

The task add-in can display a data card with variable values that the user can modify when the task is launched on the client computer ([EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_TaskLaunch). The add-in can call this method to store the variable values entered by the user.

The task add-in can call [IEdmTaskInstance::GetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~GetVar.html) during the processing of the EdmCmdType.EdmCmd_TaskRun hook to retrieve a card variable value from the server where the task is running.

Card variables are created using the administration tool card editor and are not related to the user-defined variables accessed by [IEdmTaskInstance::GetValEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~GetValEx.html) and [IEdmTaskInstance::SetValEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetValEx.html).

The difference between this method and IEdmTaskInstance::SetValEx is that the latter does not require a pre-defined card variable in the vault, whereas this method does.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTaskInstance Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html)
[IEdmTaskInstance Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance_members.html)
[Task Add-in Sample](TaskSample.htm)

## Availability

SOLIDWORKS PDM Professional 2010
