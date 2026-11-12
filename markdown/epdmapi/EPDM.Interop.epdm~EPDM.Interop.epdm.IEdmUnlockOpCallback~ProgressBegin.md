---
title: "ProgressBegin Method (IEdmUnlockOpCallback)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUnlockOpCallback"
member: "ProgressBegin"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~ProgressBegin.html"
---

# ProgressBegin Method (IEdmUnlockOpCallback)

Called by the check-in operation when it starts.

## Syntax

### Visual Basic

```vb
Sub ProgressBegin( _
   ByVal eType As EdmProgressType, _
   ByVal eEvent As EdmUnlockEvent, _
   ByVal lSteps As System.Integer _
)
```

### C#

```csharp
void ProgressBegin(
   EdmProgressType eType,
   EdmUnlockEvent eEvent,
   System.int lSteps
)
```

### C++/CLI

```cpp
void ProgressBegin(
   EdmProgressType eType,
   EdmUnlockEvent eEvent,
   System.int lSteps
)
```

### Parameters

- `eType`: Type of progress bar to start as defined in [EdmProgressType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmProgressType.html)
- `eEvent`: Type of operation as defined in [EdmUnlockEvent](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockEvent.html)
- `lSteps`: Number of steps in the operation (see **Remarks**)

## Examples

See the [IEdmUnlockOpCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback.html) examples.

## Remarks

[IEdmUnlockOpCallback::ProgressStep](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~ProgressStep.html) and [IEdmUnlockOpCallback::ProgressStepEvent](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~ProgressStepEvent.html) are each called lStep times. [IEdmUnlockOpCallback::ProgressEnd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback~ProgressEnd.html) is called when the operation completes.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUnlockOpCallback Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback.html)
[IEdmUnlockOpCallback Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUnlockOpCallback_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.3
