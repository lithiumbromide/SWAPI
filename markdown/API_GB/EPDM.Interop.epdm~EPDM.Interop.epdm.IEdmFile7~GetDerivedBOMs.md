---
title: "GetDerivedBOMs Method (IEdmFile7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile7"
member: "GetDerivedBOMs"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile7~GetDerivedBOMs.html"
---

# GetDerivedBOMs Method (IEdmFile7)

Gets the derived Bills of Materials for this file.

## Syntax

### Visual Basic

```vb
Sub GetDerivedBOMs( _
   ByRef ppoBoms As EdmBomInfo() _
)
```

### C#

```csharp
void GetDerivedBOMs(
   out EdmBomInfo[] ppoBoms
)
```

### C++/CLI

```cpp
void GetDerivedBOMs(
   [Out] array<EdmBomInfo> ppoBoms
)
```

### Parameters

- `ppoBoms`: Array of [EdmBomInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomInfo.html)s

## Examples

See the [IEdmFile7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile7.html) examples.

## Remarks

A derived Bill of Materials is also known as a named or saved Bill of Materials.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: An argument is invalid.

## See Also

[IEdmFile7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile7.html)
[IEdmFile7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile7_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
