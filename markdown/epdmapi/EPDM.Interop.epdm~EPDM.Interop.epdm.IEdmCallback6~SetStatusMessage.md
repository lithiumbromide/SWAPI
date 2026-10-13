---
title: "SetStatusMessage Method (IEdmCallback6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCallback6"
member: "SetStatusMessage"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6~SetStatusMessage.html"
---

# SetStatusMessage Method (IEdmCallback6)

Displays a message to the user.

## Syntax

### Visual Basic

```vb
Sub SetStatusMessage( _
   ByVal lBarIndex As System.Integer, _
   ByVal bsMessage As System.String _
)
```

### C#

```csharp
void SetStatusMessage(
   System.int lBarIndex,
   System.string bsMessage
)
```

### C++/CLI

```cpp
void SetStatusMessage(
   System.int lBarIndex,
   System.String^ bsMessage
)
```

### Parameters

- `lBarIndex`: 0-based index of the progress bar
- `bsMessage`: Message to display

## Examples

See the [IEdmCallback6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- <any error code>: The calling method terminated.

## See Also

[IEdmCallback6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6.html)
[IEdmCallback6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0
