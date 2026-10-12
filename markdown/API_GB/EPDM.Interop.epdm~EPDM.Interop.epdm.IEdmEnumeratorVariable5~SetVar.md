---
title: "SetVar Method (IEdmEnumeratorVariable5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVariable5"
member: "SetVar"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~SetVar.html"
---

# SetVar Method (IEdmEnumeratorVariable5)

Sets the value of the specified variable in this file or folder.

## Syntax

### Visual Basic

```vb
Sub SetVar( _
   ByVal bsVarName As System.String, _
   ByVal bsCfgName As System.String, _
   ByRef poValue As System.Object, _
   Optional ByVal bOnlyIfPartOfCard As System.Boolean _
)
```

### C#

```csharp
void SetVar(
   System.string bsVarName,
   System.string bsCfgName,
   ref System.object poValue,
   System.bool bOnlyIfPartOfCard
)
```

### C++/CLI

```cpp
void SetVar(
   System.String^ bsVarName,
   System.String^ bsCfgName,
   System.Object^% poValue,
   System.bool bOnlyIfPartOfCard
)
```

### Parameters

- `bsVarName`: Name of variable to write
- `bsCfgName`: Name of configuration or layout to which to store the variable value; empty string for folders and file types that do not support configurations
- `poValue`: Variable value
- `bOnlyIfPartOfCard`: True to store the variable only if it is part of the file or folder data card, false to store the variable as hidden data if it is not part of the file or folder data card

## Examples

[Change Card Variables Add-in (C#)](Change_Card_Variables_Addin_Example_CSharp.htm)
[Change Card Variables Add-in (VB.NET)](Change_Card_Variables_Addin_Example_VBNET.htm)
[Set Part Number Using Default Serial Numbers (C#)](Set_Part_Number_Using_Default_Serial_Numbers_Example_CSharp.htm)
[Set Part Number Using Default Serial Numbers (VB.NET)](Set_Part_Number_Using_Default_Serial_Numbers_Example_VBNET.htm)

## Remarks

To specify bsCfgName:

- Call [IEdmFile5::GetConfigurations](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetConfigurations.html) to get the available configuration names for this file.
- If this method is used in your add-in's implementation of [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html), then a list of configuration names for the data card is returned in ppoData that can be cast to [EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html). EdmCmdData.mpoExtra contains an [IEdmStrLst5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5.html) of configuration names.

After calling this method to update the variables that can be updated, you must call [IEdmEnumeratorVariable5::Flush](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~Flush.html) or [IEdmEnumeratorVariable8::CloseFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable8~CloseFile.html) with the bFlush argument set to true in order to ensure that the changes are saved properly to the file or folder.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: The variable was not found, and bOnlyIfPartOfCard is true.
- E_EDM_FILE_NOT_LOCKED_BY_YOU: The file is not checked out.

## See Also

[IEdmEnumeratorVariable5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html)
[IEdmEnumeratorVariable5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5_members.html)
[IEdmEnumeratorVariable10::GetVar2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable10~GetVar2.html)
[IEdmEnumeratorVariable10::GetVarAsText Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable10~GetVarAsText.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
