---
title: "GetUpdateVars Method (IEdmEnumeratorVariable5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVariable5"
member: "GetUpdateVars"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~GetUpdateVars.html"
---

# GetUpdateVars Method (IEdmEnumeratorVariable5)

Gets values for the variables that can be updated in this file.

## Syntax

### Visual Basic

```vb
Sub GetUpdateVars( _
   ByVal lFolderID As System.Integer, _
   ByRef ppoRetVariables() As System.Object _
)
```

### C#

```csharp
void GetUpdateVars(
   System.int lFolderID,
   out System.object[] ppoRetVariables
)
```

### C++/CLI

```cpp
void GetUpdateVars(
   System.int lFolderID,
   [Out] System.array<Object^>^ ppoRetVariables
)
```

### Parameters

- `lFolderID`: ID of the file's parent folder
- `ppoRetVariables`: Array of [IEdmVariableValue5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableValue5.html); one interface for each variable value

## Examples

[Access File Card Variables (VB.NET)](Access_File_Card_Variables_Example_VBNET.htm)
[Access File Card Variables (C#)](Access_File_Card_Variables_Example_CSharp.htm)

## Remarks

C++ users must call SafeArrayDestroy to free the returned array elements.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_FILE_NOT_LOCKED_BY_YOU: The file is not checked out.

## See Also

[IEdmEnumeratorVariable5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html)
[IEdmEnumeratorVariable5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5_members.html)
[IEdmEnumeratorVariable5::StoreValuesFromDatabase Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~StoreValuesFromDatabase.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
