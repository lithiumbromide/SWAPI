---
title: "SetValEx Method (IEdmTaskProperties)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskProperties"
member: "SetValEx"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetValEx.html"
---

# SetValEx Method (IEdmTaskProperties)

Sets a value for the specified user-defined variable.

## Syntax

### Visual Basic

```vb
Sub SetValEx( _
   ByVal bsValName As System.String, _
   ByVal oValue As System.Object _
)
```

### C#

```csharp
void SetValEx(
   System.string bsValName,
   System.object oValue
)
```

### C++/CLI

```cpp
void SetValEx(
   System.String^ bsValName,
   System.Object^ oValue
)
```

### Parameters

- `bsValName`: Name of the user-defined variable for which to set a value
- `oValue`: Value of user-defined variable (see **Remarks**)

## Examples

[Create a Task that Finds Files in Workflow States (VB.NET)](Schedule_Task_to_Find_Files_in_State_Addin_Example_VBNET.htm)
[Create a Task that Finds Files in Workflow States (C#)](Schedule_Task_to_Find_Files_in_State_Addin_Example_CSharp.htm)

## Remarks

Call this method:

- to store variable data entered by the user in the task definition setup page on the client machine.
- during the processing of the [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_TaskSetup hook.

Custom data types and objects must be serialized to a string, numeric type, or date before calling this method. For example:

1. Serialize the object data to XML or JSON using StringBuilder, XmlWriter, XmlSerializer, etc.
2. Call IEdmTaskProperites::SetValEx to store the resulting string.
3. Call [IEdmTaskProperties::GetValEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~GetValEx.html) to retrieve the stored string.
4. Initialize the new instance of the object from XML/JSON using StringReader, XmlReader, XmlSerializer, etc.

To get the user-defined values when the task is executing on the server, call [IEdmTaskInstance::GetValEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~GetValEx.html) during the processing of the EdmCmdType.EdmCmd_TaskRun hook.

**NOTE:** The difference between this method and [IEdmTaskProperties::SetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetVar.html) is that the latter requires a pre-defined card variable in the vault, whereas this method does not.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTaskProperties Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html)
[IEdmTaskProperties Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
