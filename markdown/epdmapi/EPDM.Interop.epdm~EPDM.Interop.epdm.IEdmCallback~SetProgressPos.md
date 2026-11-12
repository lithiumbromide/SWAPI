---
title: "SetProgressPos Method (IEdmCallback)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCallback"
member: "SetProgressPos"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback~SetProgressPos.html"
---

# SetProgressPos Method (IEdmCallback)

Sets the current position in the progress bar.

## Syntax

### Visual Basic

```vb
Sub SetProgressPos( _
   ByVal lPos As System.Integer _
)
```

### C#

```csharp
void SetProgressPos(
   System.int lPos
)
```

### C++/CLI

```cpp
void SetProgressPos(
   System.int lPos
)
```

### Parameters

- `lPos`: Current position in the progress bar

## Examples

See the [IEdmCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_CANCELLED_BY_USER: Cancel the operation.

## See Also

[IEdmCallback Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback.html)
[IEdmCallback Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback_members.html)
[IEdmCallback::SetProgressRange Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback~SetProgressRange.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
