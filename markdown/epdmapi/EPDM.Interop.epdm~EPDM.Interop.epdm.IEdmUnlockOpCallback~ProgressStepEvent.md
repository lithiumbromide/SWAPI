---
title: "ProgressStepEvent Method (IEdmUnlockOpCallback)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUnlockOpCallback"
member: "ProgressStepEvent"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~ProgressStepEvent.html"
---

# ProgressStepEvent Method (IEdmUnlockOpCallback)

Called to advance a progress bar.

## Syntax

### Visual Basic

```vb
Function ProgressStepEvent( _
   ByVal eType As EdmProgressType, _
   ByVal eText As EdmUnlockEventMsg, _
   ByVal lProgressPos As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool ProgressStepEvent(
   EdmProgressType eType,
   EdmUnlockEventMsg eText,
   System.int lProgressPos
)
```

### C++/CLI

```cpp
System.bool ProgressStepEvent(
   EdmProgressType eType,
   EdmUnlockEventMsg eText,
   System.int lProgressPos
)
```

### Parameters

- `eType`: Type of progress bar to advance as defined in [EdmProgressType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmProgressType.html)
- `eText`: Type of current operation as defined in [EdmUnlockEventMsg](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockEventMsg.html)
- `lProgressPos`: New position in the progress bar

### Return Value

True to continue the operation, false to cancel it

## Examples

See the [IEdmUnlockOpCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback.html) examples.

## Remarks

This method or [IEdmUnlockOpCallback::ProgressStep](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~ProgressStep.html) is called for each step in an operation that begins with [IEdmUnlockOpCallback::ProgressBegin](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~ProgressBegin.html).

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUnlockOpCallback Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback.html)
[IEdmUnlockOpCallback Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.3
