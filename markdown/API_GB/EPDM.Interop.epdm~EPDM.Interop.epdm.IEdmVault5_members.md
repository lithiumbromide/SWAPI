---
title: "IEdmVault5 Interface Members"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5_members"
member: ""
kind: "members"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html"
---

# IEdmVault5 Interface Members

The following tables list the members exposed by [IEdmVault5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CommandID | Gets the command ID count. |
| Property | IsLoggedIn | Gets whether you are logged in to this vault. |
| Property | Language | Gets the language used by the SOLIDWORKS PDM Professional client. |
| Property | Name | Gets the name of this vault. |
| Property | RootFolder | Gets the root folder of this vault. |
| Property | RootFolderID | Gets the database ID of the root folder of this vault. |
| Property | RootFolderPath | Gets the file system path to the root folder of this vault. |
| Property | SilentMode | Gets whether the add-in is running in silent mode. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | BrowseForFile | Displays an Open or Save As dialog box in which the user can click one or more files. |
| Method | BrowseForFolder | Obsolete. Superseded by IEdmVault11::BrowseForFolder2 . |
| Method | CreatePluginMenu | Obsolete. Superseded by IEdmVault12::CreatePluginMenu2 . |
| Method | CreateSearch | Obsolete. Superseded by IEdmVault21::CreateSearch2 . |
| Method | GetDictionary | Gets or creates the specified dictionary. |
| Method | GetErrorString | Gets the name and description for the specified error code returned by one of SOLIDWORKS PDM Professional's API methods. |
| Method | GetFileFromPath | Gets an interface to the file with the specified file system path. |
| Method | GetFolderFromPath | Gets an interface to a folder on the specified file system path. |
| Method | GetObject | Gets an interface to a SOLIDWORKS PDM Professional object of the specified type and having the specified ID. |
| Method | GetVaultNameFromPath | Gets the name of the vault where the specified file or folder resides. |
| Method | GetVersion | Gets the version of SOLIDWORKS PDM Professional that is installed on this machine. |
| Method | Login | Logs in to the specified vault using the specified user name and password. |
| Method | LoginAuto | Logs in to the specified vault. |
| Method | MsgBox | Displays a message box to the user. |
| Method | RefreshFolder | Refreshes the file listing in the specified folder. |
| Method | SetAddInWnd | Obsolete. See Keeping Add-in Windows in the Foreground . |
| Method | VerifyVersion | Verifies that the installed SOLIDWORKS PDM Professional is at the specified version level or higher. |

[Top](#topBookmark)

## See Also

[IEdmVault5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
