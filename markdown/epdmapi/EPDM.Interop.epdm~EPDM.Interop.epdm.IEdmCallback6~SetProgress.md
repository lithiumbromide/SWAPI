---
title: "SetProgress Method (IEdmCallback6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCallback6"
member: "SetProgress"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6~SetProgress.html"
---

# SetProgress Method (IEdmCallback6)

Sets the current progress bar position.

## Syntax

### Visual Basic

```vb
Function SetProgress( _
   ByVal lBarIndex As System.Integer, _
   ByVal lPos As System.Integer, _
   ByVal bsMsg As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool SetProgress(
   System.int lBarIndex,
   System.int lPos,
   System.string bsMsg
)
```

### C++/CLI

```cpp
System.bool SetProgress(
   System.int lBarIndex,
   System.int lPos,
   System.String^ bsMsg
)
```

### Parameters

- `lBarIndex`: 0-based index of the progress bar
- `lPos`: Current position
- `bsMsg`: Message to be displayed

### Return Value

True to continue, false to cancel

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
