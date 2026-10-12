---
title: "ProgressEnd Method (IEdmUnlockOpCallback)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUnlockOpCallback"
member: "ProgressEnd"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~ProgressEnd.html"
---

# ProgressEnd Method (IEdmUnlockOpCallback)

Called by the check-in operation when it finishes.

## Syntax

### Visual Basic

```vb
Sub ProgressEnd( _
   ByVal eType As EdmProgressType _
)
```

### C#

```csharp
void ProgressEnd(
   EdmProgressType eType
)
```

### C++/CLI

```cpp
void ProgressEnd(
   EdmProgressType eType
)
```

### Parameters

- `eType`: Type of progress bar to end as defined in [EdmProgressType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmProgressType.html)

## Examples

See the [IEdmUnlockOpCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback.html) examples.

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUnlockOpCallback Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback.html)
[IEdmUnlockOpCallback Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback_members.html)
[IEdmUnlockOpCallback::ProgressBegin Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~ProgressBegin.html)

## Availability

SOLIDWORKS PDM Professional Version 6.3
