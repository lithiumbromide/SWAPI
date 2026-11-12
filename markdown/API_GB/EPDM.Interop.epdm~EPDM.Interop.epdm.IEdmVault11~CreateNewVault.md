---
title: "CreateNewVault Method (IEdmVault11)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault11"
member: "CreateNewVault"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~CreateNewVault.html"
---

# CreateNewVault Method (IEdmVault11)

Creates a new vault.

## Syntax

### Visual Basic

```vb
Sub CreateNewVault( _
   ByVal bsArchiveServer As System.String, _
   ByVal bsArchiveServerUserName As System.String, _
   ByVal bsArchiveServerPassword As System.String, _
   ByVal bsVaultName As System.String, _
   ByVal bsDescription As System.String, _
   ByVal bsArchiveRootFolder As System.String, _
   ByVal bsSQLServer As System.String, _
   ByVal bsSQLUserName As System.String, _
   ByVal bsSQLPassword As System.String, _
   ByVal bsSQLDatabaseName As System.String, _
   ByVal lDateFmt As System.Integer, _
   ByVal bsAdminUserPassword As System.String, _
   ByVal lEdmCreateVaultFlag As System.Integer, _
   ByVal poCallback As EdmCallback, _
   Optional ByVal oExtra As System.Object _
)
```

### C#

```csharp
void CreateNewVault(
   System.string bsArchiveServer,
   System.string bsArchiveServerUserName,
   System.string bsArchiveServerPassword,
   System.string bsVaultName,
   System.string bsDescription,
   System.string bsArchiveRootFolder,
   System.string bsSQLServer,
   System.string bsSQLUserName,
   System.string bsSQLPassword,
   System.string bsSQLDatabaseName,
   System.int lDateFmt,
   System.string bsAdminUserPassword,
   System.int lEdmCreateVaultFlag,
   EdmCallback poCallback,
   System.object oExtra
)
```

### C++/CLI

```cpp
void CreateNewVault(
   System.String^ bsArchiveServer,
   System.String^ bsArchiveServerUserName,
   System.String^ bsArchiveServerPassword,
   System.String^ bsVaultName,
   System.String^ bsDescription,
   System.String^ bsArchiveRootFolder,
   System.String^ bsSQLServer,
   System.String^ bsSQLUserName,
   System.String^ bsSQLPassword,
   System.String^ bsSQLDatabaseName,
   System.int lDateFmt,
   System.String^ bsAdminUserPassword,
   System.int lEdmCreateVaultFlag,
   EdmCallback^ poCallback,
   System.Object^ oExtra
)
```

### Parameters

- `bsArchiveServer`: Name or IP number of the archive server computer; "" if the local comuter is the archive server
- `bsArchiveServerUserName`: Name of the Windows user who logs in to the archive server
- `bsArchiveServerPassword`: Password for the Windows user who logs in to the archive server
- `bsVaultName`: Name of the vault to create
- `bsDescription`: Description of the vault; appears in the vault properties window in the administration tool
- `bsArchiveRootFolder`: Archive server vault folder; "" to use the default folder
- `bsSQLServer`: Name or IP number of the SQL Server computer
- `bsSQLUserName`: Name of the user who logs in to the SQL Server computer
- `bsSQLPassword`: Password for the user who logs in to the SQL Server computer
- `bsSQLDatabaseName`: Name of the SQL database for the new vault
- `lDateFmt`: SQL Server date format code for the new vault (see **Remarks**)
- `bsAdminUserPassword`: Password for the Admin user
- `lEdmCreateVaultFlag`: Combination of [EdmCreateVaultFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCreateVaultFlag.html) bits
- `poCallback`: Optional pointer to a class that implements [IEdmCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback.html) to obtain progress information
- `oExtra`: (see **Remarks**)

## Examples

[Create New Vault (VB.NET)](Create_New_Vault_Example_VBNET.htm)
[Create New Vault (C#)](Create_New_Vault_Example_CSharp.htm)

## Remarks

See the CAST/CONVERT documentation in the SQL Server online help to learn more about the date format codes for lDateFmt. The following table lists the valid values for lDateFmt:

| Date Codes | Date Format |
| --- | --- |
| 1 | 12/31/99 |
| 2 | 99.12.31 |
| 3 | 31/12/99 |
| 4 | 31.12.99 |
| 5 | 31-12-99 |
| 6 | 31 Dec 99 |
| 7 | Dec 31, 99 |
| 10 | 12-31-99 |
| 11 | 99/12/31 |
| 12 | 991231 |
| 102 | 1999.12.31 |
| 103 | 31/12/1999 |
| 104 | 31.12.1999 |
| 105 | 31-12-1999 |
| 106 | 31 Dec 1999 |
| 107 | Dec 31, 1999 |
| 110 | 12-31-1999 |
| 111 | 1999/12/31 |
| 112 | 19991231 |
| 120 | 1999-12-31 |

Specify oExtra with one of the following:

- VT_BSTR containing either a CEX-file path to set up the vault with data from the export file or a valid vault configuration name like "Default", "Empty" or "SOLIDWORKS Quick Start"; for valid configuration names, see the **Configure Vault** step in the vault creation wizard of the administration tool
- VT_EMPTY to use default configuration

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_VAULT_ALREADY_EXISTS: There is already a file vault with the specified name on the archive server.
- E_EDM_INVALID_VAULT_NAME: The vault name contains invalid characters or is longer than 31 characters. See the SOLIDWORKS PDM Professional administrative help for restrictions on valid characters in vault names.
- E_EDM_ARCHIVE_ROOT_FOLDER_DOES_NOT_EXIST: The root folder specified in bsArchiveRootFolder does not exist.
- E_EDM_INVALID_DATABASE_NAME: The specified SQL database name is invalid. See the SOLIDWORKS PDM Professional administrative help or the Microsoft SQL Server help for restrictions regarding database names.
- E_EDM_INSUFFICIENT_SQL_PERMISSION: The specified SQL user lacks permission to create a new database. (He or she must typically be a member of the sysadmin group.)
- E_EDM_SQLSERVER_UNSUPPORTED_VERSION: The SQL server version is not supported. (SQL Server 2000 is not supported by SOLIDWORKS PDM Professional 2010.)
- E_EDM_DATABASE_ALREADY_EXISTS: There is already an SQL database with the suggested name.
- E_EDM_SQLSERVER_LOGIN_FAILED: The provided SQL credentials are not valid.
- E_EDM_SQLSERVER_CANNOT_CONNECT: General failure connecting to the SQL-server machine. Maybe the name/IP contains a typo?
- E_EDM_INVALID_DATE_FORMAT_CODE: The lDateFmt argument is invalid.

## See Also

[IEdmVault11 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11.html)
[IEdmVault11 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11_members.html)
[IEdmVault11::CreateNewVaultView Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~CreateNewVaultView.html)

## Availability

SOLIDWORKS PDM Professional 2010
