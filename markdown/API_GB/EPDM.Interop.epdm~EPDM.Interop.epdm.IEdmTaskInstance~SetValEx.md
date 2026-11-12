---
title: "SetValEx Method (IEdmTaskInstance)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskInstance"
member: "SetValEx"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetValEx.html"
---

# SetValEx Method (IEdmTaskInstance)

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

- `bsValName`: User-defined variable name
- `oValue`: Value of user-defined variable (see **Remarks**)

## Remarks

This method can be called to set the value when the task is launched on the client computer ([EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_TaskLaunch) and [IEdmTaskInstance::GetValEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~GetValEx.html) can be called to get the value when the task is executed on the server (EdmCmdType.EdmCmd_TaskRun).

Custom data types and objects must be serialized to a string, numeric type, or date before calling IEdmTaskInstance::SetValEx. For example:

1. Serialize the object data to XML or JSON using StringBuilder, XmlWriter, XmlSerializer, etc.
2. Call IEdmTaskInstance::SetValEx to store the resulting string.
3. Call IEdmTaskInstance::GetValEx to retrieve the stored string.
4. Initialize the new instance of the object from XML/JSON using StringReader, XmlReader, XmlSerializer, etc.

**NOTE**: The difference between this method and [IEdmTaskInstance::SetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetVar.html) is that the latter requires a pre-defined card variable in the vault, whereas this method does not.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTaskInstance Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html)
[IEdmTaskInstance Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance_members.html)
[Task Add-in Sample](TaskSample.htm)

## Availability

SOLIDWORKS PDM Professional 2010
