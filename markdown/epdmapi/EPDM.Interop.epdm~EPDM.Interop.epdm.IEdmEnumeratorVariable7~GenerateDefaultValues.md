---
title: "GenerateDefaultValues Method (IEdmEnumeratorVariable7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVariable7"
member: "GenerateDefaultValues"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable7~GenerateDefaultValues.html"
---

# GenerateDefaultValues Method (IEdmEnumeratorVariable7)

Generates all default values that have not been generated before.

## Syntax

### Visual Basic

```vb
Function GenerateDefaultValues( _
   ByVal lFolderID As System.Integer, _
   ByVal bWriteValuesToFile As System.Boolean, _
   ByRef ppoRetVariables() As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool GenerateDefaultValues(
   System.int lFolderID,
   System.bool bWriteValuesToFile,
   out System.object[] ppoRetVariables
)
```

### C++/CLI

```cpp
System.bool GenerateDefaultValues(
   System.int lFolderID,
   System.bool bWriteValuesToFile,
   [Out] System.array<Object^>^ ppoRetVariables
)
```

### Parameters

- `lFolderID`: ID of the file's parent folder
- `bWriteValuesToFile`: True to write values to the file, false to write only to the database
- `ppoRetVariables`: Array of [IEdmVariableValue6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableValue6.html) interfaces; one interface for each variable value generated (see **Remarks**)

### Return Value

True if values were generated, false if not

## Remarks

If bWriteValuesToFile is false, then the caller is responsible for writing the values to the file.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: No values needed to be generated.

## See Also

[IEdmEnumeratorVariable7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable7.html)
[IEdmEnumeratorVariable7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable7_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.4
