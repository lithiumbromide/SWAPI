---
title: "MsgBox Method (IEdmVault5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5"
member: "MsgBox"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~MsgBox.html"
---

# MsgBox Method (IEdmVault5)

Displays a message box to the user.

## Syntax

### Visual Basic

```vb
Function MsgBox( _
   ByVal lParentWnd As System.Integer, _
   ByVal bsMsg As System.String, _
   Optional ByVal eType As EdmMBoxType, _
   Optional ByVal bsCaption As System.String _
) As EdmMBoxResult
```

### C#

```csharp
EdmMBoxResult MsgBox(
   System.int lParentWnd,
   System.string bsMsg,
   EdmMBoxType eType,
   System.string bsCaption
)
```

### C++/CLI

```cpp
EdmMBoxResult MsgBox(
   System.int lParentWnd,
   System.String^ bsMsg,
   EdmMBoxType eType,
   System.String^ bsCaption
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `bsMsg`: Message to display in the message box
- `eType`: Optional style of the message box as defined in [EdmMBoxType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMBoxType.html)
- `bsCaption`: Optional string to display for the message box caption

### Return Value

Button clicked as defined in [EdmMBoxResult](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMBoxResult.html)

## Examples

[Notify User When File Changes State (VB.NET)](Notify_User_When_File_Changes_State_Example_VBNET.htm)
[Notify User When File Changes State (C#)](Notify_User_When_File_Changes_State_Example_CSharp.htm)

## Remarks

The only advantage of this method over the standard Visual Basic MsgBox function is that, with this method, you can specify a parent window handle to ensure that the message box stays on top of whatever parent window you have. For add-ins the parent window is usually the File Explorer window.

You do not need to call [IEdmVault5::Login](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~Login.html) or [IEdmVault5::LoginAuto](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~LoginAuto.html) before calling this method.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- S_FALSE: The user pressed **Cancel**.

## See Also

[IEdmVault5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html)
[IEdmVault5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
