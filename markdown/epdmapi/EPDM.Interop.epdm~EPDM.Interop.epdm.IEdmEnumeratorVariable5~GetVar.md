---
title: "GetVar Method (IEdmEnumeratorVariable5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVariable5"
member: "GetVar"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~GetVar.html"
---

# GetVar Method (IEdmEnumeratorVariable5)

Gets the value of the specified variable from this file or folder.

## Syntax

### Visual Basic

```vb
Function GetVar( _
   ByVal bsVarName As System.String, _
   ByVal bsCfgName As System.String, _
   ByRef poRetValue As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool GetVar(
   System.string bsVarName,
   System.string bsCfgName,
   out System.object poRetValue
)
```

### C++/CLI

```cpp
System.bool GetVar(
   System.String^ bsVarName,
   System.String^ bsCfgName,
   [Out] System.Object^ poRetValue
)
```

### Parameters

- `bsVarName`: Name of variable to read
- `bsCfgName`: Name of configuration or layout from which to get the variable value; empty string for folders and file types that do not support configurations (see

Remarks

)
- `poRetValue`: Variable value; data type as specified in

[IEdmVariable5::VariableType](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariable5~VariableType.html)

(see

Remarks

)

### Return Value

True if the variable is found, false if not

## Remarks

To specify bsCfgName:

- Call

  [IEdmFile5::GetConfigurations](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetConfigurations.html)

  to get the available configuration names for this file.
- If this method is used in your add-in's implementation of

  [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html)

  , then a list of configuration names for the data card is returned in ppoData that can be cast to

  [EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html)

  . EdmCmdData.mpoExtra contains an

  [IEdmStrLst5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5.html)

  of configuration names.

C++ users must initialize the VARIANT struct of poRetValue with a call to VariantInit before calling this method. They also must free the contents of the struct with a call to VariantClear.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: The variable was not found.

## See Also

[IEdmEnumeratorVariable5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html)

[IEdmEnumeratorVariable5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5_members.html)

[IEdmEnumeratorVariable5::SetVar Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~SetVar.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
