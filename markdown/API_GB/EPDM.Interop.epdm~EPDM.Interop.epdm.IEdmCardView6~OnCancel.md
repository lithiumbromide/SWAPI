---
title: "OnCancel Method (IEdmCardView6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCardView6"
member: "OnCancel"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView6~OnCancel.html"
---

# OnCancel Method (IEdmCardView6)

Rolls back all changes made in the card view after it is cancelled.

## Syntax

### Visual Basic

```vb
Sub OnCancel()
```

### C#

```csharp
void OnCancel()
```

### C++/CLI

```cpp
void OnCancel();
```

## Examples

See the [IEdmCardView6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView6.html) examples.

## Remarks

Call this method when the card view is cancelled. This method ensures that all serial numbers generated in the card (by right-clicking in edit boxes linked to serial numbers) are pushed back to the database so they can be reused. If you do not call this method, serial numbers are not restored to the database, and gaps in the serial number series occur.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmCardView6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView6.html)
[IEdmCardView6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0
