---
title: "GetVersions Method (IEdmBom)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBom"
member: "GetVersions"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBom~GetVersions.html"
---

# GetVersions Method (IEdmBom)

Gets the versions of this BOM.

## Syntax

### Visual Basic

```vb
Sub GetVersions( _
   ByRef ppoVersions() As EdmBomVersion _
)
```

### C#

```csharp
void GetVersions(
   out EdmBomVersion[] ppoVersions
)
```

### C++/CLI

```cpp
void GetVersions(
   [Out] array<EdmBomVersion>^ ppoVersions
)
```

### Parameters

- `ppoVersions`: Array of [EdmBomVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomVersion.html) structures; one structure for each BOM version; the structure of the oldest version is at the beginning of the array

## Examples

See the [IEdmBom](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBom.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBom Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBom.html)
[IEdmBom Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBom_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
