---
title: "IsLoggedIn Property (IEdmVault5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5"
member: "IsLoggedIn"
kind: "property"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~IsLoggedIn.html"
---

# IsLoggedIn Property (IEdmVault5)

Gets whether you are logged in to this vault.

## Syntax

### Visual Basic

```vb
ReadOnly Property IsLoggedIn As System.Boolean
```

### C#

```csharp
System.bool IsLoggedIn {get;}
```

### C++/CLI

```cpp
property System.bool IsLoggedIn {
   System.bool get();
}
```

### Property Value

True if logged in, false if not

## Examples

[Add Users (C#)](Add_Users_Example_CSharp.htm)
[Add Users (VB.NET)](Add_Users_Example_VBNET.htm)

## Remarks

Log in to the vault by calling [IEdmVault5::Login](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~Login.html) or [IEdmVault5::LoginAuto](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~LoginAuto.html).

## See Also

[IEdmVault5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html)
[IEdmVault5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
