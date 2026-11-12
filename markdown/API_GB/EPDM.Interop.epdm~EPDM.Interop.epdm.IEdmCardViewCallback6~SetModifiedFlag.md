---
title: "SetModifiedFlag Method (IEdmCardViewCallback6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCardViewCallback6"
member: "SetModifiedFlag"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6~SetModifiedFlag.html"
---

# SetModifiedFlag Method (IEdmCardViewCallback6)

Called when a card variable changes.

## Syntax

### Visual Basic

```vb
Sub SetModifiedFlag()
```

### C#

```csharp
void SetModifiedFlag()
```

### C++/CLI

```cpp
void SetModifiedFlag();
```

## Examples

See the [IEdmCardViewCallback6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6.html) examples.

## Remarks

You can implement this method, for instance, to enable **Save** when the card changes.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmCardViewCallback6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6.html)
[IEdmCardViewCallback6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0
