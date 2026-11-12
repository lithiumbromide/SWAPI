---
title: "SetMinorProgress Method (IEdmCallback8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCallback8"
member: "SetMinorProgress"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback8~SetMinorProgress.html"
---

# SetMinorProgress Method (IEdmCallback8)

Sets the current minor progress bar position.

## Syntax

### Visual Basic

```vb
Sub SetMinorProgress( _
   ByVal oMsg As System.String, _
   ByVal dwProgress As System.UInteger _
)
```

### C#

```csharp
void SetMinorProgress(
   System.string oMsg,
   System.uint dwProgress
)
```

### C++/CLI

```cpp
void SetMinorProgress(
   System.String^ oMsg,
   System.uint dwProgress
)
```

### Parameters

- `oMsg`: Message to be displayed
- `dwProgress`: Progress

## See Also

[IEdmCallback8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback8.html)
[IEdmCallback8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback8_members.html)

## Availability

SOLIDWORKS PDM Professional 2021
