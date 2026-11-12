---
title: "MsgBox Method (IEdmCallback6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCallback6"
member: "MsgBox"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6~MsgBox.html"
---

# MsgBox Method (IEdmCallback6)

Displays a message box.

## Syntax

### Visual Basic

```vb
Function MsgBox( _
   ByVal lParentWnd As System.Integer, _
   ByVal lMsgID As System.Integer, _
   ByVal bsMsg As System.String, _
   Optional ByVal eType As EdmMBoxType _
) As EdmMBoxResult
```

### C#

```csharp
EdmMBoxResult MsgBox(
   System.int lParentWnd,
   System.int lMsgID,
   System.string bsMsg,
   EdmMBoxType eType
)
```

### C++/CLI

```cpp
EdmMBoxResult MsgBox(
   System.int lParentWnd,
   System.int lMsgID,
   System.String^ bsMsg,
   EdmMBoxType eType
)
```

### Parameters

- `lParentWnd`: Handle of the parent window
- `lMsgID`: ID of the message to be shown (see **Remarks**)
- `bsMsg`: Message to be displayed
- `eType`: Message box type as defined in [EdmMBoxType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMBoxType.html)

### Return Value

Message box result as defined in [EdmMBoxResult](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMBoxResult.html)

## Examples

See the [IEdmCallback6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6.html) examples.

## Remarks

For callbacks during add operations, IMsgID is one of the values defined in [EdmAddCallbackMsgID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddCallbackMsgID.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- <any error code>: The calling method terminated.

## See Also

[IEdmCallback6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6.html)
[IEdmCallback6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0
