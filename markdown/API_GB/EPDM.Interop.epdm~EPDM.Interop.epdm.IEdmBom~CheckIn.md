---
title: "CheckIn Method (IEdmBom)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBom"
member: "CheckIn"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBom~CheckIn.html"
---

# CheckIn Method (IEdmBom)

Checks in this BOM.

## Syntax

### Visual Basic

```vb
Sub CheckIn( _
   ByVal bsComment As System.String _
)
```

### C#

```csharp
void CheckIn(
   System.string bsComment
)
```

### C++/CLI

```cpp
void CheckIn(
   System.String^ bsComment
)
```

### Parameters

- `bsComment`: Comment to add to the history of this BOM

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBom Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBom.html)
[IEdmBom Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBom_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
