---
title: "SetAddInWnd Method (IEdmVault5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5"
member: "SetAddInWnd"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~SetAddInWnd.html"
---

# SetAddInWnd Method (IEdmVault5)

Obsolete. See [Keeping Add-in Windows in the Foreground](KeepWindowInfront.htm).

## Syntax

### Visual Basic

```vb
Sub SetAddInWnd( _
   ByVal lAddInWnd As System.Integer, _
   ByVal lParentWnd As System.Integer _
)
```

### C#

```csharp
void SetAddInWnd(
   System.int lAddInWnd,
   System.int lParentWnd
)
```

### C++/CLI

```cpp
void SetAddInWnd(
   System.int lAddInWnd,
   System.int lParentWnd
)
```

### Parameters

- `lAddInWnd`: Add-in window handle
- `lParentWnd`: File Explorer window handle; [EdmCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd.html)::mlParentWnd passed to [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html)

## Remarks

This method ensures that windows created from add-ins written in Visual Basic 6 do not appear behind the application window. Since VBA is no longer supported, this method is obsolete and should not be used.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVault5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html)
[IEdmVault5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
