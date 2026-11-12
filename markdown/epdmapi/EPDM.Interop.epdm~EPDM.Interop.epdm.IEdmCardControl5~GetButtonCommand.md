---
title: "GetButtonCommand Method (IEdmCardControl5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCardControl5"
member: "GetButtonCommand"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5~GetButtonCommand.html"
---

# GetButtonCommand Method (IEdmCardControl5)

Gets the command string that is executed when a button is clicked in the Card Editor.

## Syntax

### Visual Basic

```vb
Function GetButtonCommand( _
   ByVal lParentWnd As System.Integer _
) As System.String
```

### C#

```csharp
System.string GetButtonCommand(
   System.int lParentWnd
)
```

### C++/CLI

```cpp
System.String^ GetButtonCommand(
   System.int lParentWnd
)
```

### Parameters

- `lParentWnd`: Parent window handle

### Return Value

Command string

## Remarks

If the button is linked to a program that is not found, this method launches a dialog box in which the user can browse to the missing EXE file. If the user clicks **Cancel** in the dialog box, HRESULT = E_EDM_CANCELLED_BY_USER is returned by this method.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_INVALID_ID: The supplied control is not a push-button. Call [IEdmCardControl5::ControlType](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5~ControlType.html) first to verify whether the control is a push-button.
- E_EDM_CANCELLED_BY_USER: The user clicked **Cancel** in the dialog box.

## See Also

[IEdmCardControl5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5.html)
[IEdmCardControl5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
