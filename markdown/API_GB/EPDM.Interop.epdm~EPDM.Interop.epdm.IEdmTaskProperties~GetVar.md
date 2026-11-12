---
title: "GetVar Method (IEdmTaskProperties)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskProperties"
member: "GetVar"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~GetVar.html"
---

# GetVar Method (IEdmTaskProperties)

Gets the value of a card variable created in the administration tool and set by [IEdmTaskProperties::SetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetVar.html).

## Syntax

### Visual Basic

```vb
Function GetVar( _
   ByVal lVarID As System.Integer _
) As System.Object
```

### C#

```csharp
System.object GetVar(
   System.int lVarID
)
```

### C++/CLI

```cpp
System.Object^ GetVar(
   System.int lVarID
)
```

### Parameters

- `lVarID`: ID of variable for which to get a value

### Return Value

Value of a card variable

## Remarks

The task add-in calls this method to retrieve a data card variable value that is set by the user on the task details page on the client computer. To save and retrieve the variable, the add-in calls [IEdmTaskProperties::SetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetVar.html) and this method, respectively, during the processing of the [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_TaskSetup hook.

These data card variable values can also be retrieved when the task is executed on the server by calling [IEdmTaskInstance::GetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~GetVar.html).

Card variables accessible by this method must be created using the administration tool card editor and are not related to the user-defined variables accessed by [IEdmTaskProperties::GetValEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~GetValEx.html) and [IEdmTaskProperties::SetValEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetValEx.html).

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTaskProperties Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html)
[IEdmTaskProperties Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties_members.html)
[Task Add-in Sample](TaskSample.htm)

## Availability

SOLIDWORKS PDM Professional 2010
