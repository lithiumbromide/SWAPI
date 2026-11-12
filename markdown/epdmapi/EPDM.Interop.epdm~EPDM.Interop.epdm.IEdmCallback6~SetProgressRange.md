---
title: "SetProgressRange Method (IEdmCallback6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCallback6"
member: "SetProgressRange"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6~SetProgressRange.html"
---

# SetProgressRange Method (IEdmCallback6)

Sets the maximum value for a progress bar.

## Syntax

### Visual Basic

```vb
Sub SetProgressRange( _
   ByVal lBarIndex As System.Integer, _
   ByVal lMax As System.Integer _
)
```

### C#

```csharp
void SetProgressRange(
   System.int lBarIndex,
   System.int lMax
)
```

### C++/CLI

```cpp
void SetProgressRange(
   System.int lBarIndex,
   System.int lMax
)
```

### Parameters

- `lBarIndex`: 0-based index of the progress bar
- `lMax`: Maximum value for the progress bar; minimum value is always 0

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
