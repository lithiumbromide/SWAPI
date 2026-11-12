---
title: "SetRefVars Method (IEdmBatchRefVars)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchRefVars"
member: "SetRefVars"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars~SetRefVars.html"
---

# SetRefVars Method (IEdmBatchRefVars)

Sets the values of the specified reference variables.

## Syntax

### Visual Basic

```vb
Sub SetRefVars( _
   ByRef ppoVars() As EdmRefVar _
)
```

### C#

```csharp
void SetRefVars(
   out EdmRefVar[] ppoVars
)
```

### C++/CLI

```cpp
void SetRefVars(
   [Out] array<EdmRefVar>^ ppoVars
)
```

### Parameters

- `ppoVars`: Array of [EdmRefVar structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefVar.html)s; one structure for each reference variable whose value you want to update

## Examples

See the [IEdmBatchRefVars](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars.html) examples.

## Remarks

Call [IEdmBatchRefVars::GetRefVars](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars~GetRefVars.html) and [IEdmBatchRefVars::GetAllRefVars](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars~GetAllRefVars.html) to get the variable values.

The parent file must be checked out in order to update reference variables.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchRefVars Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars.html)
[IEdmBatchRefVars Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
