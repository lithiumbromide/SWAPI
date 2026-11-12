---
title: "SetCtrlData Method (IEdmCardViewCallback6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCardViewCallback6"
member: "SetCtrlData"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6~SetCtrlData.html"
---

# SetCtrlData Method (IEdmCardViewCallback6)

Stores the control's variable data when a card is saved.

## Syntax

### Visual Basic

```vb
Sub SetCtrlData( _
   ByVal lCardWnd As System.Integer, _
   ByVal lCardID As System.Integer, _
   ByVal lControlID As System.Integer, _
   ByVal lVariableID As System.Integer, _
   ByVal bsVariableName As System.String, _
   ByVal poView As IEdmCardView5, _
   ByRef poValue As System.Object _
)
```

### C#

```csharp
void SetCtrlData(
   System.int lCardWnd,
   System.int lCardID,
   System.int lControlID,
   System.int lVariableID,
   System.string bsVariableName,
   IEdmCardView5 poView,
   ref System.object poValue
)
```

### C++/CLI

```cpp
void SetCtrlData(
   System.int lCardWnd,
   System.int lCardID,
   System.int lControlID,
   System.int lVariableID,
   System.String^ bsVariableName,
   IEdmCardView5^ poView,
   System.Object^% poValue
)
```

### Parameters

- `lCardWnd`: Window handle of the card
- `lCardID`: ID of the card (see **Remarks**)
- `lControlID`: ID of the control for which to get the value (see **Remarks**)
- `lVariableID`: ID of the variable used by this control (see **Remarks**)
- `bsVariableName`: Name of the variable used by this control
- `poView`: [IEdmCardView5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardView5.html)
- `poValue`: Control variable data to save

## Examples

See the [IEdmCardViewCallback6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6.html) examples.

## Remarks

The framework calls this method once per control when a card created with [IEdmVault10::CreateCardViewEx2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault10~CreateCardViewEx2.html) is saved.

| Use... | In a call to IEdmVault5::GetObject with eType = ... | To obtain... |
| --- | --- | --- |
| ICardID | EdmObjectType .EdmObject_Card | IEdmCard5 |
| IControlID | EdmObjectType.EdmObject_CardControl | IEdmCardControl5 |
| IVariableID | EdmObjectType.EdmObject_Variable | IEdmVariable5 |

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmCardViewCallback6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6.html)
[IEdmCardViewCallback6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0
