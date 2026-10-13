---
title: "GetCardSize Method (IEdmCardView5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCardView5"
member: "GetCardSize"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView5~GetCardSize.html"
---

# GetCardSize Method (IEdmCardView5)

Gets the size of the file or folder data card.

## Syntax

### Visual Basic

```vb
Sub GetCardSize( _
   ByRef plWidth As System.Integer, _
   ByRef plHeight As System.Integer _
)
```

### C#

```csharp
void GetCardSize(
   out System.int plWidth,
   out System.int plHeight
)
```

### C++/CLI

```cpp
void GetCardSize(
   [Out] System.int plWidth,
   [Out] System.int plHeight
)
```

### Parameters

- `plWidth`: Width of the card in pixels
- `plHeight`: Height of the card in pixels

## Examples

See the [IEdmCardView5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView5.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmCardView5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView5.html)
[IEdmCardView5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
