---
title: "SetStatusMessage Method (IEdmCallback)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCallback"
member: "SetStatusMessage"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback~SetStatusMessage.html"
---

# SetStatusMessage Method (IEdmCallback)

Displays a message to the user.

## Syntax

### Visual Basic

```vb
Sub SetStatusMessage( _
   ByVal bsMessage As System.String _
)
```

### C#

```csharp
void SetStatusMessage(
   System.string bsMessage
)
```

### C++/CLI

```cpp
void SetStatusMessage(
   System.String^ bsMessage
)
```

### Parameters

- `bsMessage`: Message to display

## Examples

See the [IEdmCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_CANCELLED_BY_USER: Cancel the operation.

## See Also

[IEdmCallback Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback.html)
[IEdmCallback Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
