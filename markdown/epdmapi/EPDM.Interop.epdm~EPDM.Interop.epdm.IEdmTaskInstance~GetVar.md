---
title: "GetVar Method (IEdmTaskInstance)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskInstance"
member: "GetVar"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~GetVar.html"
---

# GetVar Method (IEdmTaskInstance)

Gets the value of a card variable created in the administration tool.

## Syntax

### Visual Basic

```vb
Function GetVar( _
   ByVal oVarIDorName As System.Object _
) As System.Object
```

### C#

```csharp
System.object GetVar(
   System.object oVarIDorName
)
```

### C++/CLI

```cpp
System.Object^ GetVar(
   System.Object^ oVarIDorName
)
```

### Parameters

- `oVarIDorName`: ID or name of the card variable for which to get a value

### Return Value

Value of a card variable

## Remarks

The task add-in calls this method while the task is running on the server (EdmCmdType.EdmCmd_TaskRun) to retrieve a variable value set by the add-in when it calls:

- [IEdmTaskInstance::SetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetVar.html) during the processing of the [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_TaskLaunch hook when the user enters values on the data card displayed when the task is launched on the client computer.
- [IEdmTaskProperties.SetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetVar.html) during the processing of the EdmCmdType.EdmCmd_TaskSetup hook when the user enters data card variable values on the task setup page.

Card variables accessible by this method must be created using the administration tool card editor and are not related to the user-defined variables accessed by [IEdmTaskInstance::GetValEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~GetValEx.html) and [IEdmTaskInstance::SetValEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetValEx.html).

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTaskInstance Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html)
[IEdmTaskInstance Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance_members.html)
[IEdmTaskInstance::SetVar Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetVar.html)
[Task Add-in Sample](TaskSample.htm)

## Availability

SOLIDWORKS PDM Professional 2010
