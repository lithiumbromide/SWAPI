---
title: "Show Method (IEdmGetCSVersionDialog)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmGetCSVersionDialog"
member: "Show"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetCSVersionDialog~Show.html"
---

# Show Method (IEdmGetCSVersionDialog)

Shows the Restore coldstored file version dialog.

## Syntax

### Visual Basic

```vb
Sub Show( _
   ByRef peReply As EdmGetOpReply, _
   ByRef vbApplyForAll As System.Boolean _
)
```

### C#

```csharp
void Show(
   out EdmGetOpReply peReply,
   out System.bool vbApplyForAll
)
```

### C++/CLI

```cpp
void Show(
   [Out] EdmGetOpReply peReply,
   [Out] System.bool vbApplyForAll
)
```

### Parameters

- `peReply`: [EdmGetOpReply](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetOpReply.html); user-defined action
- `vbApplyForAll`: True to apply peReply to all items, false to not

## See Also

[IEdmGetCSVersionDialog Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetCSVersionDialog.html)
[IEdmGetCSVersionDialog Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmGetCSVersionDialog_members.html)
