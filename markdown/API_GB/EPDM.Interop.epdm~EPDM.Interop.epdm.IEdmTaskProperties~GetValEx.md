---
title: "GetValEx Method (IEdmTaskProperties)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskProperties"
member: "GetValEx"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~GetValEx.html"
---

# GetValEx Method (IEdmTaskProperties)

Gets the value of a user-defined variable created with [IEdmTaskProperties::SetValEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetValEx.html).

## Syntax

### Visual Basic

```vb
Function GetValEx( _
   ByVal bsValName As System.String _
) As System.Object
```

### C#

```csharp
System.object GetValEx(
   System.string bsValName
)
```

### C++/CLI

```cpp
System.Object^ GetValEx(
   System.String^ bsValName
)
```

### Parameters

- `bsValName`: Name of variable for which to get a value

### Return Value

Value of variable (see **Remarks**)

## Examples

[Create a Task that Finds Files in Workflow States (VB.NET)](Schedule_Task_to_Find_Files_in_State_Addin_Example_VBNET.htm)
[Create a Task that Finds Files in Workflow States (C#)](Schedule_Task_to_Find_Files_in_State_Addin_Example_CSharp.htm)

## Remarks

Call IEdmTaskProperties::SetValEx to store variable data entered by the user in the task definition setup page on the client machine. The task definition setup page displays during the processing of the [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_TaskSetup hook when the task add-in calls [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html).

Custom data types and objects must have been serialized to a string, numeric type, or date before calling IEdmTaskProperites::SetValEx. For example:

1. Serialize the object data to XML or JSON using StringBuilder, XmlWriter, XmlSerializer, etc.
2. Call IEdmTaskProperites::SetValEx to store the resulting string.
3. Call IEdmTaskProperites::GetValEx to retrieve the stored string.
4. Initialize the new instance of the object from XML/JSON using StringReader, XmlReader, XmlSerializer, etc.

To get the values when the task is executing on the server, call [IEdmTaskInstance::GetValEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~GetValEx.html) during the processing of the EdmCmdType.EdmCmd_TaskRun hook.

**NOTE**: User-defined variables are not related to the card variables created using the administration tool. To access card variables for this task definition, call [IEdmTaskProperties::GetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~GetVar.html) and [IEdmTaskProperties::SetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetVar.html).

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTaskProperties Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html)
[IEdmTaskProperties Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
