---
title: "CreateNewVaultView Method (IEdmVault11)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault11"
member: "CreateNewVaultView"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~CreateNewVaultView.html"
---

# CreateNewVaultView Method (IEdmVault11)

Creates a local view of a file vault in File Explorer.

## Syntax

### Visual Basic

```vb
Sub CreateNewVaultView( _
   ByVal bsArchiveServer As System.String, _
   ByVal bsArchiveServerUserName As System.String, _
   ByVal bsArchiveServerPassword As System.String, _
   ByVal bsVaultName As System.String, _
   ByVal bsParentFolderPath As System.String, _
   ByVal lEdmCreateVaultViewFlag As System.Integer _
)
```

### C#

```csharp
void CreateNewVaultView(
   System.string bsArchiveServer,
   System.string bsArchiveServerUserName,
   System.string bsArchiveServerPassword,
   System.string bsVaultName,
   System.string bsParentFolderPath,
   System.int lEdmCreateVaultViewFlag
)
```

### C++/CLI

```cpp
void CreateNewVaultView(
   System.String^ bsArchiveServer,
   System.String^ bsArchiveServerUserName,
   System.String^ bsArchiveServerPassword,
   System.String^ bsVaultName,
   System.String^ bsParentFolderPath,
   System.int lEdmCreateVaultViewFlag
)
```

### Parameters

- `bsArchiveServer`: Name or IP number of the archive server computer; "" if the local comuter is the archive server
- `bsArchiveServerUserName`: Name of the Windows user who logs in to the archive server
- `bsArchiveServerPassword`: Password for the Windows user who logs in to the archive server
- `bsVaultName`: Name of the vault for which to create a view
- `bsParentFolderPath`: Full system path to the parent folder of the view; a subfolder with the same name as the vault is created in the parent folder
- `lEdmCreateVaultViewFlag`: Combination of [EdmCreateVaultViewFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCreateVaultViewFlag.html) bits

## Examples

[Create New Vault (VB.NET)](Create_New_Vault_Example_VBNET.htm)
[Create New Vault (C#)](Create_New_Vault_Example_CSharp.htm)

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_FOLDER_NOT_FOUND: The parent folder does not exist.
- E_EDM_VERSION_MISMATCH: The client version and the archive server version do not match.
- E_EDM_FVC_CANT_WRITE_TO_REGISTRY: Failed to write to the system registry. Possibly you are trying to create a shared view, and the logged-in Windows user lacks privileges to write to HKEY_LOCAL_MACHINE.

## See Also

[IEdmVault11 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11.html)
[IEdmVault11 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11_members.html)
[IEdmVault11::CreateNewVault Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~CreateNewVault.html)

## Availability

SOLIDWORKS PDM Professional 2010
