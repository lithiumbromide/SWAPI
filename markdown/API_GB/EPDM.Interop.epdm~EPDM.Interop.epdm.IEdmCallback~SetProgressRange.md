---
title: "SetProgressRange Method (IEdmCallback)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCallback"
member: "SetProgressRange"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback~SetProgressRange.html"
---

# SetProgressRange Method (IEdmCallback)

Sets the minimum and maximum values in the progress bar.

## Syntax

### Visual Basic

```vb
Sub SetProgressRange( _
   ByVal lMin As System.Integer, _
   ByVal lMax As System.Integer _
)
```

### C#

```csharp
void SetProgressRange(
   System.int lMin,
   System.int lMax
)
```

### C++/CLI

```cpp
void SetProgressRange(
   System.int lMin,
   System.int lMax
)
```

### Parameters

- `lMin`: Minimum value in the progress bar
- `lMax`: Maximum value in the progress bar

## Examples

See the [IEdmCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_CANCELLED_BY_USER: Cancel the operation.

## See Also

[IEdmCallback Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback.html)
[IEdmCallback Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback_members.html)
[IEdmCallback::SetProgressPos Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback~SetProgressPos.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
