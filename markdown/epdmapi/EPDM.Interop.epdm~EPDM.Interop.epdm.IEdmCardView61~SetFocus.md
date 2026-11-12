---
title: "SetFocus Method (IEdmCardView61)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCardView61"
member: "SetFocus"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView61~SetFocus.html"
---

# SetFocus Method (IEdmCardView61)

Sets input focus to a certain control in this card view.

## Syntax

### Visual Basic

```vb
Sub SetFocus( _
   Optional ByRef poVariableNameOrID As System.Object _
)
```

### C#

```csharp
void SetFocus(
   ref System.object poVariableNameOrID
)
```

### C++/CLI

```cpp
void SetFocus(
   System.Object^% poVariableNameOrID
)
```

### Parameters

- `poVariableNameOrID`: Name or ID of the variable to which to set focus; 0 to set focus to the first control in the card

## Examples

See the [IEdmCardView61](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView61.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmCardView61 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView61.html)
[IEdmCardView61 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView61_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0
