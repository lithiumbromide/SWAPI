---
title: "OnAddInInput Method (IEdmCardViewCallback6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCardViewCallback6"
member: "OnAddInInput"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6~OnAddInInput.html"
---

# OnAddInInput Method (IEdmCardViewCallback6)

Handles input from an add-in when an add-in button is clicked in the card view.

## Syntax

### Visual Basic

```vb
Sub OnAddInInput( _
   ByVal lFlags As System.Integer _
)
```

### C#

```csharp
void OnAddInInput(
   System.int lFlags
)
```

### C++/CLI

```cpp
void OnAddInInput(
   System.int lFlags
)
```

### Parameters

- `lFlags`: Combination of [EdmCardFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardFlag.html) bits from a button's add-in (see **Remarks**)

## Examples

See the [IEdmCardViewCallback6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6.html) examples.

## Remarks

When an add-in's button is clicked in a card view, [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html) is called. lFlags contains the same data that is returned in ppoData ([EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html)::mlLongData1) of IEdmAddIn5::OnCmd.

This method allows you to act on the information provided by the button's add-in.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmCardViewCallback6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6.html)
[IEdmCardViewCallback6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0
