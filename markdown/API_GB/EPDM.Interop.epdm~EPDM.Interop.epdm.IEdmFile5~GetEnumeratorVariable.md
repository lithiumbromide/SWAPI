---
title: "GetEnumeratorVariable Method (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "GetEnumeratorVariable"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetEnumeratorVariable.html"
---

# GetEnumeratorVariable Method (IEdmFile5)

Gets an interface to this file's data card variables.

## Syntax

### Visual Basic

```vb
Function GetEnumeratorVariable( _
   Optional ByVal bsOptionalPath As System.String _
) As IEdmEnumeratorVariable5
```

### C#

```csharp
IEdmEnumeratorVariable5 GetEnumeratorVariable(
   System.string bsOptionalPath
)
```

### C++/CLI

```cpp
IEdmEnumeratorVariable5^ GetEnumeratorVariable(
   System.String^ bsOptionalPath
)
```

### Parameters

- `bsOptionalPath`: Optional; full file path to the file to access; if not specified, uses location where this file is checked out (see **Remarks**)

### Return Value

[IEdmEnumeratorVariable5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html)

## Examples

[Set Initial Revision (VB.NET)](Set_Initial_Revision_Example_VBNET.htm)
[Set Initial Revision (C#)](Set_Initial_Revision_Example_CSharp.htm)
[Set Part Number Using Default Serial Numbers (C#)](Set_Part_Number_Using_Default_Serial_Numbers_Example_CSharp.htm)
[Set Part Number Using Default Serial Numbers (VB.NET)](Set_Part_Number_Using_Default_Serial_Numbers_Example_VBNET.htm)

## Remarks

You must check out a file in order to write variables in its data card.

See [Return Codes](ReturnCodes.htm) for the complete list of potential success and error codes. The following are just a few examples:

- S_OK: The method successfully executed.
- E_EDM_FILE_NOT_FOUND: File not found on the specified path.

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
