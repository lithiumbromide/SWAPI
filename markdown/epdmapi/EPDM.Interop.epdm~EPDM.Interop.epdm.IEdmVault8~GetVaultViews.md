---
title: "GetVaultViews Method (IEdmVault8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault8"
member: "GetVaultViews"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault8~GetVaultViews.html"
---

# GetVaultViews Method (IEdmVault8)

Gets all of the views set up on this vault.

## Syntax

### Visual Basic

```vb
Sub GetVaultViews( _
   ByRef ppoRetViews() As EdmViewInfo, _
   ByVal bOnlyLoggedIn As System.Boolean _
)
```

### C#

```csharp
void GetVaultViews(
   out EdmViewInfo[] ppoRetViews,
   System.bool bOnlyLoggedIn
)
```

### C++/CLI

```cpp
void GetVaultViews(
   [Out] array<EdmViewInfo>^ ppoRetViews,
   System.bool bOnlyLoggedIn
)
```

### Parameters

- `ppoRetViews`: Array of [EdmViewInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmViewInfo.html) structures; one structure for each view
- `bOnlyLoggedIn`: True to get views in which you are currently logged, false to get all views

## Examples

See the [IEdmVault8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault8.html) examples.

## Remarks

You do not have to call [IEdmVault5::Login](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~Login.html) or [IEdmVault5::LoginAuto](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~LoginAuto.html) before calling this method.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVault8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault8.html)
[IEdmVault8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault8_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.4
