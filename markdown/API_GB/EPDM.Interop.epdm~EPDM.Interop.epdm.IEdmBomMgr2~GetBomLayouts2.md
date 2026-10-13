---
title: "GetBomLayouts2 Method (IEdmBomMgr2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomMgr2"
member: "GetBomLayouts2"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr2~GetBomLayouts2.html"
---

# GetBomLayouts2 Method (IEdmBomMgr2)

Gets all of the BOM layouts installed in a vault.

## Syntax

### Visual Basic

```vb
Sub GetBomLayouts2( _
   ByRef ppoRetLayouts As EdmBomLayout2() _
)
```

### C#

```csharp
void GetBomLayouts2(
   out EdmBomLayout2[] ppoRetLayouts
)
```

### C++/CLI

```cpp
void GetBomLayouts2(
   [Out] array<EdmBomLayout2> ppoRetLayouts
)
```

### Parameters

- `ppoRetLayouts`: Array of [EdmBomLayout2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomLayout2.html) structures; one structure for each BOM layout

## Examples

See the [IEdmBomMgr2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr2.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBomMgr2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr2.html)
[IEdmBomMgr2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr2_members.html)

## Availability

SOLIDWORKS PDM Professional 2020
