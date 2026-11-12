---
title: "GetBomLayouts Method (IEdmBomMgr)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomMgr"
member: "GetBomLayouts"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr~GetBomLayouts.html"
---

# GetBomLayouts Method (IEdmBomMgr)

Obsolete. Superseded by [IEdmBomMgr2::GetBomLayouts2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr2~GetBomLayouts2.html).

## Syntax

### Visual Basic

```vb
Sub GetBomLayouts( _
   ByRef ppoRetLayouts As EdmBomLayout() _
)
```

### C#

```csharp
void GetBomLayouts(
   out EdmBomLayout[] ppoRetLayouts
)
```

### C++/CLI

```cpp
void GetBomLayouts(
   [Out] array<EdmBomLayout> ppoRetLayouts
)
```

### Parameters

- `ppoRetLayouts`: Array of [EdmBomLayout](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomLayout.html) structures; one structure for each BOM layout

## Examples

See the [IEdmBomMgr](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBomMgr Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr.html)
[IEdmBomMgr Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
