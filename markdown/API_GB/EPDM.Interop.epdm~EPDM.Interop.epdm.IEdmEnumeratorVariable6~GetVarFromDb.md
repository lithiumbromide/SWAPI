---
title: "GetVarFromDb Method (IEdmEnumeratorVariable6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVariable6"
member: "GetVarFromDb"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable6~GetVarFromDb.html"
---

# GetVarFromDb Method (IEdmEnumeratorVariable6)

Reads a variable from the SOLIDWORKS PDM Professional database.

## Syntax

### Visual Basic

```vb
Function GetVarFromDb( _
   ByVal bsVarName As System.String, _
   ByVal bsCfgName As System.String, _
   ByRef poRetValue As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool GetVarFromDb(
   System.string bsVarName,
   System.string bsCfgName,
   out System.object poRetValue
)
```

### C++/CLI

```cpp
System.bool GetVarFromDb(
   System.String^ bsVarName,
   System.String^ bsCfgName,
   [Out] System.Object^ poRetValue
)
```

### Parameters

- `bsVarName`: Name of variable to read
- `bsCfgName`: Name of configuration or layout from which to get the variable value; empty string for folders and file types that do not support configurations
- `poRetValue`: Variable value

### Return Value

True if a variable is found, false if not

## Remarks

To read a variable from a checked out file, call [IEdmEnumeratorVariable5::GetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~GetVar.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: The variable is not found.

## See Also

[IEdmEnumeratorVariable6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable6.html)
[IEdmEnumeratorVariable6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0
