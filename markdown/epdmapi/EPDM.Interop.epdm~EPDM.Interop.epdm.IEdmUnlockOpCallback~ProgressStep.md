---
title: "ProgressStep Method (IEdmUnlockOpCallback)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUnlockOpCallback"
member: "ProgressStep"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~ProgressStep.html"
---

# ProgressStep Method (IEdmUnlockOpCallback)

Called to advance a progress bar.

## Syntax

### Visual Basic

```vb
Function ProgressStep( _
   ByVal eType As EdmProgressType, _
   ByVal bsText As System.String, _
   ByVal lProgressPos As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool ProgressStep(
   EdmProgressType eType,
   System.string bsText,
   System.int lProgressPos
)
```

### C++/CLI

```cpp
System.bool ProgressStep(
   EdmProgressType eType,
   System.String^ bsText,
   System.int lProgressPos
)
```

### Parameters

- `eType`: Type of progress bar to advance as defined in [EdmProgressType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmProgressType.html)
- `bsText`: Message that indicates what the operation is doing
- `lProgressPos`: New position in the progress bar

### Return Value

True to continue the operation, false to cancel it

## Examples

See the [IEdmUnlockOpCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback.html) examples.

## Remarks

This method or [IEdmUnlockOpCallback::ProgressStepEvent](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~ProgressStepEvent.html) is called for each step in an operation that begins with [IEdmUnlockOpCallback::ProgressBegin](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~ProgressBegin.html).

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUnlockOpCallback Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback.html)
[IEdmUnlockOpCallback Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.3
