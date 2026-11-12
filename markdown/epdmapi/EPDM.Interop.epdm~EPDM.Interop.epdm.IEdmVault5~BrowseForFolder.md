---
title: "BrowseForFolder Method (IEdmVault5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5"
member: "BrowseForFolder"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~BrowseForFolder.html"
---

# BrowseForFolder Method (IEdmVault5)

Obsolete. Superseded by [IEdmVault11::BrowseForFolder2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~BrowseForFolder2.html).

## Syntax

### Visual Basic

```vb
Function BrowseForFolder( _
   ByVal hParentWnd As System.Integer, _
   ByVal bsMessage As System.String _
) As IEdmFolder5
```

### C#

```csharp
IEdmFolder5 BrowseForFolder(
   System.int hParentWnd,
   System.string bsMessage
)
```

### C++/CLI

```cpp
IEdmFolder5^ BrowseForFolder(
   System.int hParentWnd,
   System.String^ bsMessage
)
```

### Parameters

- `hParentWnd`: Parent window handle
- `bsMessage`: Message to display in the dialog box

### Return Value

[IEdmFolder5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html); Null if the user clicks **Cancel** (see **Remarks**)

## Remarks

C++ users must release the returned interface, IEdmFolder5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- S_FALSE: The user clicked **Cancel**.
- E_EDM_NOT_LOGGED_IN: You must call [IEdmVault5::Login](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~Login.html) or [IEdmVault5::LoginAuto](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~LoginAuto.html) before calling this method.

## See Also

[IEdmVault5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html)
[IEdmVault5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
