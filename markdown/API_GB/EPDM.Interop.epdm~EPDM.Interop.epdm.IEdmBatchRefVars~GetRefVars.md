---
title: "GetRefVars Method (IEdmBatchRefVars)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchRefVars"
member: "GetRefVars"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars~GetRefVars.html"
---

# GetRefVars Method (IEdmBatchRefVars)

Gets the values of the specified reference variables.

## Syntax

### Visual Basic

```vb
Sub GetRefVars( _
   ByRef ppoVars As EdmRefVar() _
)
```

### C#

```csharp
void GetRefVars(
   out EdmRefVar[] ppoVars
)
```

### C++/CLI

```cpp
void GetRefVars(
   [Out] array<EdmRefVar> ppoVars
)
```

### Parameters

- `ppoVars`: Array of [EdmRefVar structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefVar.html)s; one structure for each reference variable whose value you want to retrieve

## Examples

See the [IEdmBatchRefVars](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars.html) examples.

## Remarks

This method updates the moValue and mhResult members of the EdmRefVar structures. mlParentVersion = 0 gets the values from the latest version you have permission to read.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchRefVars Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars.html)
[IEdmBatchRefVars Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars_members.html)
[IEdmBatchRefVars::SetRefVars Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars~SetRefVars.html)

## Availability

SOLIDWORKS PDM Professional 2010
