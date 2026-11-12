---
title: "GetAllRefVars Method (IEdmBatchRefVars)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchRefVars"
member: "GetAllRefVars"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars~GetAllRefVars.html"
---

# GetAllRefVars Method (IEdmBatchRefVars)

Gets all of the values for the specified reference variables.

## Syntax

### Visual Basic

```vb
Sub GetAllRefVars( _
   ByRef ppoVars As EdmRefVar(), _
   ByVal lParentFileID As System.Integer, _
   Optional ByVal lParentFileVersion As System.Integer, _
   Optional ByVal lChildFileID As System.Integer, _
   Optional ByVal bsParentConfig As System.String, _
   Optional ByVal bsChildConfig As System.String _
)
```

### C#

```csharp
void GetAllRefVars(
   out EdmRefVar[] ppoVars,
   System.int lParentFileID,
   System.int lParentFileVersion,
   System.int lChildFileID,
   System.string bsParentConfig,
   System.string bsChildConfig
)
```

### C++/CLI

```cpp
void GetAllRefVars(
   [Out] array<EdmRefVar> ppoVars,
   System.int lParentFileID,
   System.int lParentFileVersion,
   System.int lChildFileID,
   System.String^ bsParentConfig,
   System.String^ bsChildConfig
)
```

### Parameters

- `ppoVars`: Array of [EdmRefVar structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefVar.html)s; one structure for each reference variable
- `lParentFileID`: ID of parent file for which to get reference variables
- `lParentFileVersion`: Version number of parent file for which to get reference variables; 0 gets the latest version if the parent file is checked in and the checked-out version if it is checked out
- `lChildFileID`: ID of the referenced child file; 0 gets variables for all child references
- `bsParentConfig`: Configuration of parent file for which to get reference variables; "" gets all configurations
- `bsChildConfig`: Configuration of parent file for which to get reference variables; "" is ignored

## Examples

See the [IEdmBatchRefVars](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchRefVars Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars.html)
[IEdmBatchRefVars Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchRefVars_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
