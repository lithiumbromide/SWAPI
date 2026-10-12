---
title: "BrowseForFolder2 Method (IEdmVault11)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault11"
member: "BrowseForFolder2"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~BrowseForFolder2.html"
---

# BrowseForFolder2 Method (IEdmVault11)

Displays a Browse for Folder dialog box in which the user can click a file or item folder.

## Syntax

### Visual Basic

```vb
Function BrowseForFolder2( _
   ByVal hParentWnd As System.Integer, _
   ByVal bsMessage As System.String, _
   ByVal poDefaultFolder As IEdmFolder5, _
   ByVal lFlags As System.Integer _
) As IEdmFolder5
```

### C#

```csharp
IEdmFolder5 BrowseForFolder2(
   System.int hParentWnd,
   System.string bsMessage,
   IEdmFolder5 poDefaultFolder,
   System.int lFlags
)
```

### C++/CLI

```cpp
IEdmFolder5^ BrowseForFolder2(
   System.int hParentWnd,
   System.String^ bsMessage,
   IEdmFolder5^ poDefaultFolder,
   System.int lFlags
)
```

### Parameters

- `hParentWnd`: Parent window handle
- `bsMessage`: Message to display in the dialog box
- `poDefaultFolder`: [IEdmFolder5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html); default folder to browse
- `lFlags`: Combination of [EdmBrowseForFolderFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBrowseForFolderFlag.html) bits

### Return Value

[IEdmFolder5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html); Null if the user clicks **Cancel** (see **Remarks**)

## Examples

[Get and Set Item References (VB.NET)](Get_and_Set_Item_References_Example_VBNET.htm)
[Get and Set Item References (C#)](Get_and_Set_Item_References_Example_CSharp.htm)

## Remarks

This method supersedes [IEdmVault5::BrowseForFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~BrowseForFolder.html) by providing the ability to select items.

C++ users must release the returned interface, IEdmFolder5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- S_FALSE: The user pressed **Cancel**.
- E_EDM_NOT_LOGGED_IN: You must call [IEdmVault5::Login](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~Login.html) or [IEdmVault5::LoginAuto](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~LoginAuto.html) before calling this method.

## See Also

[IEdmVault11 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11.html)
[IEdmVault11 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
