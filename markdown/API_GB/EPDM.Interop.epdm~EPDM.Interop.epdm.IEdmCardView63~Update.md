---
title: "Update Method (IEdmCardView63)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCardView63"
member: "Update"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView63~Update.html"
---

# Update Method (IEdmCardView63)

Updates controls in this card view.

## Syntax

### Visual Basic

```vb
Sub Update( _
   ByVal eType As EdmCardViewUpdateType, _
   Optional ByRef poArg As System.Object _
)
```

### C#

```csharp
void Update(
   EdmCardViewUpdateType eType,
   ref System.object poArg
)
```

### C++/CLI

```cpp
void Update(
   EdmCardViewUpdateType eType,
   System.Object^% poArg
)
```

### Parameters

- `eType`: Type of update to perform as defined in [EdmCardViewUpdateType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardViewUpdateType.html)
- `poArg`: Reserved for future use

## Examples

See the [IEdmCardView63](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView63.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmCardView63 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView63.html)
[IEdmCardView63 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView63_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.4
