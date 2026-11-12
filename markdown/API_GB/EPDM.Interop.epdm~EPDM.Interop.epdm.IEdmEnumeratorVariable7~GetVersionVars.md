---
title: "GetVersionVars Method (IEdmEnumeratorVariable7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVariable7"
member: "GetVersionVars"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable7~GetVersionVars.html"
---

# GetVersionVars Method (IEdmEnumeratorVariable7)

Gets the values of variables of the specified version directly from the database.

## Syntax

### Visual Basic

```vb
Sub GetVersionVars( _
   ByVal oVersion As System.Object, _
   ByVal lFolderID As System.Integer, _
   ByRef ppoRetVariables As System.Object(), _
   ByRef ppoRetConfigs As System.String(), _
   ByRef poRetData As EdmGetVarData _
)
```

### C#

```csharp
void GetVersionVars(
   System.object oVersion,
   System.int lFolderID,
   out System.object[] ppoRetVariables,
   out System.string[] ppoRetConfigs,
   out EdmGetVarData poRetData
)
```

### C++/CLI

```cpp
void GetVersionVars(
   System.Object^ oVersion,
   System.int lFolderID,
   [Out] System.array<Object^> ppoRetVariables,
   [Out] System.array<String^> ppoRetConfigs,
   [Out] EdmGetVarData poRetData
)
```

### Parameters

- `oVersion`: Version number of variables to get; 0 to get the latest version
- `lFolderID`: ID of the file's parent folder; 0 if the file is not shared
- `ppoRetVariables`: Array of [IEdmVariableValue6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableValue6.html) interfaces; one interface for each variable value
- `ppoRetConfigs`: Array of configuration or layout names
- `poRetData`: [EdmGetVarData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetVarData.html); extra information about the file

## Examples

[Get File Variable Data (VB.NET)](Get_File_Variable_Data_Example_VBNET.htm)
[Get File Variable Data (C#)](Get_File_Variable_Data_Example_CSharp.htm)

## Remarks

In previous versions of the API, you had to call [IEdmFile5::GetFileCopy](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetFileCopy.html) get a local copy of a file and then call [IEdmFile5::GetEnumeratorVariable](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetEnumeratorVariable.html) to read variables. This method is more efficient, because it retrieves the variable values directly from the database, removing the need to retrieve the file first.

When retrieving several variables, it is more efficient to use this method instead of multiple calls to [IEdmEnumeratorVariable5::GetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~GetVar.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: An argument is invalid.

## See Also

[IEdmEnumeratorVariable7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable7.html)
[IEdmEnumeratorVariable7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable7_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.4
