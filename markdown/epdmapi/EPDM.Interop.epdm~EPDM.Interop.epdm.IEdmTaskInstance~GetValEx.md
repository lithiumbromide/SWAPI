---
title: "GetValEx Method (IEdmTaskInstance)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskInstance"
member: "GetValEx"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~GetValEx.html"
---

# GetValEx Method (IEdmTaskInstance)

Gets the value of the specified user-defined variable.

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

- `bsValName`: Name of a user-defined variable

### Return Value

Value of user-defined variable (see **Remarks**)

## Examples

[Create a Task that Finds Files in Workflow States (VB.NET)](Schedule_Task_to_Find_Files_in_State_Addin_Example_VBNET.htm)
[Create a Task that Finds Files in Workflow States (C#)](Schedule_Task_to_Find_Files_in_State_Addin_Example_CSharp.htm)

## Remarks

This method gets the value of a user-defined variable that is created by [IEdmTaskInstance::SetValEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetValEx.html) or [IEdmTaskProperties::SetValEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetValEx.html). User-defined variables are usually created during the processing of the [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_TaskLaunch or the EdmCmdType.EdmCmd_TaskSetup hook and are usually read during the processing of the EdmCmdType.EdmCmd_TaskRun hook.

Custom data types and objects must have been serialized to a string, numeric type, or date before calling IEdmTaskInstance::SetValEx or IEdmTaskProperites::SetValEx. For example:

1. Serialize the object data to XML or JSON using StringBuilder, XmlWriter, XmlSerializer, etc.
2. Call IEdmTaskInstance::SetValEx or IEdmTaskProperties::SetValEx to store the resulting string.
3. Call IEdmTaskInstance::GetValEx to retrieve the stored string.
4. Initialize the new instance of the object from XML/JSON using StringReader, XmlReader, XmlSerializer, etc.

**NOTE**: User-defined variables are not related to the card variables created using the administration tool. To access card variables, call [IEdmTaskInstance::GetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~GetVar.html) and [IEdmTaskInstance::SetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetVar.html).

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTaskInstance Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html)
[IEdmTaskInstance Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
