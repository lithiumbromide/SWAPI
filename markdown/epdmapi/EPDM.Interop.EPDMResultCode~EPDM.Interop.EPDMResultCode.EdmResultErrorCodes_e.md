---
title: "EdmResultErrorCodes_e Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmResultErrorCodes_e"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.EPDMResultCode~EPDM.Interop.EPDMResultCode.EdmResultErrorCodes_e.html"
---

# EdmResultErrorCodes_e Enumeration

Error codes. See

[EdmResultSuccessCodes_e](EPDM.Interop.EPDMResultCode~EPDM.Interop.EPDMResultCode.EdmResultSuccessCodes_e.html)

for the success codes.

## Syntax

### Visual Basic

```vb
Public Enum EdmResultErrorCodes_e
   Inherits System.Enum
```

### C#

```csharp
public enum EdmResultErrorCodes_e : System.Enum
```

### C++/CLI

```cpp
public enum class EdmResultErrorCodes_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| E_EDM_ADDIN_CANT_ACCESS_REGISTRY | 0x800402D8 = Cannot redirect registry to retrieve add-in class ID |
| E_EDM_ADDIN_CLSID_ALREADY_USED | 0x800402CE = There is already an add-in using the CLSID that you are trying to add; class IDs must be unique |
| E_EDM_ADDIN_CLSID_NOT_FOUND | 0x800402DA = The add-in registration succeeded, but the add-in's class ID could not be found in the registry |
| E_EDM_ADDIN_FILE_NOT_FOUND | 0x800402D6 = The add-in file was not found |
| E_EDM_ADDIN_LOAD_CONFLICT | 0x800402DB = The add-in could not be loaded; this can happen if an attempt is made to register a new version of a .NET add-in that is already loaded; the situation can usually be resolved by closing the application and reattempting the operation |
| E_EDM_ADDIN_LOADCONFLICT | 0x80040284 = An older version of the add-in is already loaded in memory; restart the program to load the new version of the add-in |
| E_EDM_ADDIN_NAME_ALREADY_USED | 0x800402D1 = There is already an add-in with the same name as the one you are trying to add; the name must be unique |
| E_EDM_ADDIN_NOT_COM_DLL | 0x800402D7 = The specified add-in file is not a COM DLL |
| E_EDM_ADDIN_NOT_FOUND | 0x800402CF = T he add-in cannot be found in the vault |
| E_EDM_ADDIN_NOT_MULTITHREADED | 0x800402AF = An attempt was made to add an add-in that is not a multithreaded COM-server |
| E_EDM_ADDIN_UNSUPPORTED_OS | 0x800402DC = The add-in does not support the operating system; you cannot load an 64-bit add-in in 32-bit Windows |
| E_EDM_ALIAS_USED_IN_EXPORT_SCRIPT | 0x800402AC = The alias set cannot be deleted because it is used in a data export rule |
| E_EDM_ALIAS_USED_IN_IMPORT_SCRIPT | 0x800402AD = The alias set cannot be deleted because it is used in a data import rule |
| E_EDM_ALL_GROUPS_NOT_VALIDATED | 0x80040298 = All groups were not validated |
| E_EDM_ALL_USERS_NOT_VALIDATED | 0x80040289 = All users were not validated |
| E_EDM_ALREADY_INITIALIZED | 0x8004021B = An attempt was made to initialize an object twice; you can only initialize an object one time |
| E_EDM_ALREADY_LOGGED_IN | 0x80040205 = You tried to log in twice |
| E_EDM_ARCHIVE_LOGIN_FAILED | 0x80040243 = Login failed because of an invalid user name or password |
| E_EDM_ARCHIVE_ROOT_FOLDER_DOES_NOT_EXIST | 0x800402C7 = Specified archive server root folder does not exist |
| E_EDM_ARCHIVE_SERVER_NOT_FOUND | 0x8004023F = The archive server is not found; try starting the archive server |
| E_EDM_ASSEMBLY_IN_LDR_MODE | 0x8004030B = The assembly is in Large Design Review mode |
| E_EDM_AUTO_LOGGED_OUT | 0x80040280 = You have been inactive for too long and have been logged out |
| E_EDM_BAD_LENGTH | 0x80040242 = The statement is out of bounds |
| E_EDM_BOM_NOT_FOUND | 0x800402A9 = The specified bill of materials could not be found |
| E_EDM_BOM_USED_IN_EXPORT_SCRIPT | 0x800402AB = The bill of materials cannot be deleted because it is used in a data export rule |
| E_EDM_CANCELLED_BY_USER | 0x80040226 = The operation was canceled by the user |
| E_EDM_CANT_MOVE_FOLDER_TO_SUBFOLDER | 0x8004029C = An attempt was made to move a folder to one of its subfolders |
| E_EDM_CANT_OPEN_DATABASE | 0x80040206 = Could not open database; this could happen if the network connection is broken or if the database has been removed |
| E_EDM_CANT_START_EDMSERVER | 0x8004025B = Could not start EdmServer.exe; please reinstall the program |
| E_EDM_CARD_NOT_FOUND | 0x8004027E = The specified card could not be found |
| E_EDM_CARDLIST_HAS_NO_NAME | 0x800402E1 = Not the latest version, when latest version is required |
| E_EDM_CIRCULAR_XREF | 0x8004022F = Detected cyclic file reference |
| E_EDM_COLD_STORAGE_SCHEMA_NOT_FOUND | 0x80040275 = The cold storage schema with the specified name was not found |
| E_EDM_COLD_STORE_SCHEMA_EXISTS | 0x80040277 = Saving the cold storage schema failed because the name is already used by another schema |
| E_EDM_COLUMN_VIEW_NOT_FOUND | 0x80040290 = The column view cannot be found |
| E_EDM_COMMENT_NOT_ENTERED | 0x800402F4 = Comment not entered |
| E_EDM_CONDITIONS_NOT_MET | 0x80040233 = Conditions for transition were not met |
| E_EDM_COPYTREE_ZIP_FAILED | 0x800402FB = Failed to create ZIP file during the file copy operation |
| E_EDM_COULD_NOT_CREATE_LOCAL_FOLDER | 0x8004021E = Could not create the folder in the local cache; the folder name might contain invalid characters |
| E_EDM_COULD_NOT_LAUNCH_TASKS | 0x800402CB = Cannot launch tasks with user interface in silent mode |
| E_EDM_COULD_NOT_OPEN_CLIPBOARD | 0x8004027A = Could not open the clipboard |
| E_EDM_DATABASE_ACCESS | 0x80040207 = Could not access the item in the database |
| E_EDM_DATABASE_ALREADY_EXISTS | 0x800402D0 = A database with the same name already exists on the server |
| E_EDM_DATABASE_LINK_FAILURE | 0x80040267 = A communication link failure occurred when accessing the database server; the database service might have been restarted, or the network might be down; please try the operation again and contact your system administrator if the problem persists |
| E_EDM_DATASOURCE_NOT_FOUND | 0x80040222 = The ODBC data source was not found |
| E_EDM_DISABLED | 0x8004023D = The command is disabled |
| E_EDM_DISK_FULL | 0x80040239 = The disk is full |
| E_EDM_DOCTYPE_EXISTS | 0x80040259 = A category with the specified name already exists |
| E_EDM_DOCTYPE_IN_USE | 0x80040258 = The category is currently associated with one or more documents and cannot be deleted |
| E_EDM_DONTSETMODIFIED_FLAG | 0x800402E5 = Do not set the modified flag |
| E_EDM_DOTNET_REGISTRATION_MODULE_MISSING | 0x800402D9 = The .NET registration module is missing |
| E_EDM_DRAWING_IN_DETAILING_MODE | 0x80040306 = The drawing is in detailing mode |
| E_EDM_DUPLICATE_GROUP_NAME | 0x80040268 = Saving the user group failed because the group name is already used by another group |
| E_EDM_DUPLICATE_SEARCH_FAVORITE_NAME | 0x8004024B = Could not save the search favorite with the specified name because the name is already used by another favorite and the names must be unique; if the other favorite is not visible in the program, it is probably because you do not have permission to see it |
| E_EDM_EMPTY_VALUE_FIELD | 0x80040301 = The value of one or more transiiton conditions cannot be empty |
| E_EDM_END_OF_LIST | 0x80040208 = You tried to get an element from a list where the cursor is off right |
| E_EDM_END_OF_REV_GEN_LIST_CONTINUE | 0x80040232 = You have reached the end of the revision generator list; please contact your system administrator to add more revision-generator entries in the workflow editor |
| E_EDM_END_OF_REV_GEN_LIST_STOP | 0x80040231 = You have reached the end of the revision generator list; please contact your system administrator to add more revision-generator entries in the workflow editor |
| E_EDM_END_OF_SN_FILE | 0x8004023A = You have reached the end of the serial number file |
| E_EDM_ERPMGR_ALIAS_DOES_NOT_EXIST | 0x8004029D = The alias does not exist |
| E_EDM_ERPMGR_EXPORT_SCRIPT_NOT_FOUND | 0x800402A8 = The specified export rule could not be found |
| E_EDM_ERPMGR_IMPORTBATCH_DOES_NOT_EXIST | 0x8004029E = The data import batch does not exist |
| E_EDM_ERPMGR_IMPORTSCRIPT_NAME_ALREADY_EXISTS | 0x8004029F = The name of the data import rule is already used |
| E_EDM_ERPMGR_INVALID_DATE_FORMAT | 0x800402A0 = The date format is invalid |
| E_EDM_ERPMGR_INVALID_FILENAME | 0x800402A1 = The file name is invalid |
| E_EDM_ERPMGR_ITEM_NOT_FOUND | 0x800402A2 = The data import/export item was not found in the database |
| E_EDM_ERPMGR_VALUE_TOO_LONG | 0x800402A3 = The value is too long |
| E_EDM_ERPMGR_VARALIASSET_ALREADY_EXISTS | 0x800402A4 = The specified alias set already exists |
| E_EDM_ERPMGR_VARALIASSET_DOES_NOT_EXIST | 0x800402A5 = The specified variable alias set does not exist |
| E_EDM_ERPMGR_VARIABLE_DOES_NOT_EXIST | 0x800402A6 = The specified variable does not exist |
| E_EDM_ERPMGR_VARIABLENAME_NOT_UNIQUE | 0x800402A7 = The variable name is not unique |
| E_EDM_EXCLUDED_FROM_PREVIEW | 0x8004023C = The file type is excluded from preview |
| E_EDM_FILE_ALREADY_OPEN | 0x80040281 = The file is already open |
| E_EDM_FILE_DELETED | 0x8004026D = The file has been deleted |
| E_EDM_FILE_FORMAT_UNSUPPORTED_BY_CONISIO_VERSION | 0x8004026A = The file format is not supported by your SOLIDWORKS PDM Professional license |
| E_EDM_FILE_IN_COLDSTORAGE | 0x80040278 = The file that you are trying to access is currently placed in cold storage and cannot be retrieved |
| E_EDM_FILE_IS_LOCKED | 0x80040211 = The operation is not permitted because the file is checked out |
| E_EDM_FILE_IS_REFERENCED | 0x8004022D = The file is referenced by another file |
| E_EDM_FILE_MIGRATED_TO_PLATFORM | 0x8004030C = The file cannot be moved as it is migrated to the 3DEXPERIENCE platform |
| E_EDM_FILE_NAME_NOT_GLOBALLY_UNIQUE | 0x80040286 = The file name, which needs to be unique in the file vault, has been used before |
| E_EDM_FILE_NOT_FOUND | 0x80040213 = T he file could not be found |
| E_EDM_FILE_NOT_LOCKED_BY_YOU | 0x80040210 = The file is not checked out by you, which is required by the operation |
| E_EDM_FILE_NOT_OPEN | 0x80040282 = The file is not open |
| E_EDM_FILE_NOT_REGENERATED | 0x800402B3 = The file is not rebuilt |
| E_EDM_FILE_SHARE_ERROR | 0x8004020B = An attempt was made to access a file that is exclusively opened by another application |
| E_EDM_FILES_WERE_LOCKED | 0x80040257 = One or more documents have been checked out; these files have been deselected; click OK again if you still want to perform the operation on the remaining files |
| E_EDM_FOLDER_DESTROY_CONSTRAINT_FAILED | 0x8004030A = Failed to destroy one or more folders due to a constraint violation |
| E_EDM_FOLDER_NOT_EMPTY | 0x8004021F = The specified folder is not empty |
| E_EDM_FOLDER_NOT_FOUND | 0x80040214 = The folder could not be found |
| E_EDM_GET_EDMFORMATROUTER | 0x8004027D = The file format plug-in routes the call onto another plug-in; the file format manager will query the interface for the IEdmFormatRouter code to figure out which plug-in to use |
| E_EDM_GROUP_NAME_ALREADY_EXISTS | 0x80040297 = The group name already exists |
| E_EDM_GROUP_NAME_NOT_UNIQUE | 0x80040295 = The group name is not unique in the specified array of groups |
| E_EDM_GROUP_NOT_FOUND | 0x800402D4 = The group could not be found |
| E_EDM_HAS_NO_CARD | 0x80040227 = The file does not have a file data card |
| E_EDM_HAS_NO_PARENT | 0x80040202 = The folder does not have a parent |
| E_EDM_HAS_NO_PREVIEW | 0x80040223 = The file does not have a preview bitmap |
| E_EDM_INDEXER_NOT_STARTED | 0x8004027F = Indexing has not been set up for this file vault |
| E_EDM_INSUFFICIENT_SQL_PERMISSION | 0x80040283 = The SQL server user account associated with the vault has insufficient privileges; the administrator can solve this by running the following command in the SQL Server Query Analyzer: GRANT VIEW SERVER STATE TO user name |
| E_EDM_INVALID_BOM | 0x800402EA = Invalid BOM |
| E_EDM_INVALID_CATEGORY_ID | 0x80040263 = The specified category database ID is invalid |
| E_EDM_INVALID_COLUMN_VIEW | 0x80040291 = The column view is invalid |
| E_EDM_INVALID_COMPLETE_NAME | 0x8004028B = The complete name is invalid |
| E_EDM_INVALID_DATABASE_NAME | 0x800402C3 = The SQL database name is invalid |
| E_EDM_INVALID_DATE_FORMAT_CODE | 0x800402C5 = The SQL date format code is invalid |
| E_EDM_INVALID_EMAIL | 0x8004028C = The email is invalid |
| E_EDM_INVALID_FILE | 0x80040229 = The file format is not recognized |
| E_EDM_INVALID_FILE_ID | 0x80040264 = The specified file ID is invalid |
| E_EDM_INVALID_GROUP_DESCRIPTION | 0x80040296 = The group description is invalid |
| E_EDM_INVALID_GROUP_MEMBER_ID | 0x80040299 = A group member ID is invalid |
| E_EDM_INVALID_GROUP_NAME | 0x80040294 = The group name is invalid |
| E_EDM_INVALID_ID | 0x80040241 = The supplied object ID is not valid |
| E_EDM_INVALID_INITIALS | 0x8004028D = The initials are invalid |
| E_EDM_INVALID_NAME | 0x8004021D = The file/key name was invalid |
| E_EDM_INVALID_OUTLOOK_VERSION | 0x800402E2 = The specified version of Microsoft Outlook is invalid |
| E_EDM_INVALID_PASSWORD | 0x8004028F = The password is invalid |
| E_EDM_INVALID_QUERY | 0x80040230 = The search query is invalid |
| E_EDM_INVALID_REVISION_NUMBER | 0x80040224 = Specified revision number is invalid |
| E_EDM_INVALID_REVISION_NUMBER_COMPONENT_NAME | 0x8004029B = The revision number component name is invalid |
| E_EDM_INVALID_REVISION_NUMBER_GENERATOR_NAME | 0x8004029A = The revision number generator name is invalid |
| E_EDM_INVALID_SERIAL_NUMBER_NAME | 0x80040256 = Invalid serial number name |
| E_EDM_INVALID_TRANSITION_WEB | 0x80040274 = Could not change state because the transition would create a new document version, which is not supported by the web client |
| E_EDM_INVALID_TYPE | 0x80040225 = T he object has an invalid type for the specified operation |
| E_EDM_INVALID_USER_DATA | 0x8004028E = The user data string is invalid |
| E_EDM_INVALID_USER_NAME | 0x80040287 = The user name is invalid |
| E_EDM_INVALID_VAULT_NAME | 0x800402C2 = The vault name is invalid |
| E_EDM_INVALID_WORKFLOW_ID | 0x80040260 = The specified workflow database ID is invalid |
| E_EDM_INVALID_WORKFLOW_STATE_ID | 0x80040262 = The specified workflow state database ID is invalid |
| E_EDM_INVALID_WORKFLOW_TRANSITION_ID | 0x80040261 = The specified workflow transition database ID is invalid |
| E_EDM_IO_ERROR | 0x80040228 = Error accessing the file |
| E_EDM_KEY_NOT_FOUND | 0x8004022B = The key you specified was not found in the collection |
| E_EDM_LABEL_ALREADY_EXIST | 0x80040302 = The label already exists |
| E_EDM_LOCAL_FILE_NOT_FOUND | 0x80040285 = The file is not present in the file vault cache folder on the client computer |
| E_EDM_LOCK_ERRORS | 0x80040266 = One or more documents could not be checked out |
| E_EDM_LOCKED | 0x800402B0 = The file is checked out |
| E_EDM_LOCKED_BY_ANOTHER_USER | 0x80040212 = The file is checked out by another user |
| E_EDM_LOCKED_IN_OTHER_FOLDER | 0x800402B0 = The file is checked out in another folder |
| E_EDM_LOCKED_ON_OTHER_COMPUTER | 0x80040215 = The file is checked out on another computer |
| E_EDM_LOGIN_FAILED | 0x80040200 = Login failed because of an invalid user name or password |
| E_EDM_LOGIN_LOCK | 0x8004024E = The system is locked due to maintenance |
| E_EDM_MAILSERVER_NOT_INSTALLED | 0x80040235 = SOLIDWORKS PDM Professional Database Server is not installed on the database server; please contact your system administrator for assistance |
| E_EDM_MAPPING_FOUND | 0x8004020E = Could not remove the attribute class because it is used by a control in a file data card |
| E_EDM_MISSING_ATTRIBUTE | 0x8004020C = An attempt was made to access an attribute that is not present in the file |
| E_EDM_MISSING_CONISIO_MODULE | 0x80040272 = A required SOLIDWORKS PDM Professional module is not installed |
| E_EDM_MISSING_LOCAL_VIEW | 0x800402D5 = The vault must have a local view |
| E_EDM_MISSING_MANDATORY_VALUE | 0x80040236 = An attempt was made to save an empty value for a mandatory variable |
| E_EDM_MISSING_PLUGIN_COMPONENT | 0x80040245 = The file format plug-in cannot handle this file because a component is missing |
| E_EDM_MISSING_PTID | 0x8004025A = The registry variable PTID is missing; please reinstall the program |
| E_EDM_MISSING_SEARCH_PROC | 0x8004024F = The search card's stored procedure is missing in the database |
| E_EDM_MISSING_URL_PARAM | 0x8004026E = A required URL parameter is missing |
| E_EDM_MISSING_VIEW_INFO | 0x8004024C = Could not find registry information for this view; you might have to attach to this vault again to repair the registry |
| E_EDM_MOVE_FILE_PERMISSION_DENIED | 0x800402E4 = The user does not have permission to move the file. |
| E_EDM_NAME_ALREADY_EXISTS | 0x8004020F = An attempt was made to create a new file or folder with the same name as an existing one |
| E_EDM_NEED_MIGRATING | 0x80040249 = The file needs to be migrated for the operation to succeed |
| E_EDM_NO_ACTIVE_COLDSTORAGE_OPERATION | 0x80040276 = There are currently no active cold storage operations belonging to the calling archive server |
| E_EDM_NO_DOCTYPE | 0x8004025C = The document does not meet the conditions of any category |
| E_EDM_NO_MATCHING_PLUGIN | 0x8004022A = There is no matching plug-in |
| E_EDM_NO_REVISION_GENERATOR | 0x80040247 = The file is not connected to a revision generator |
| E_EDM_NO_REVISION_ON_REFERENCE | 0x80040237 = Cannot set revision because not all referenced files have revisions on the attached versions |
| E_EDM_NO_SECPKG_FOUND | 0x80040254 = Could not negotiate a security package to use between the server and the client |
| E_EDM_NO_WORKFLOW | 0x8004025D = The document does not meet the conditions of any workflow |
| E_EDM_NOT_A_COM_DLL | 0x800402CC = The DLL is not a COM module |
| E_EDM_NOT_AN_ADDIN_DLL | 0x800402CD = T he DLL is not an SOLIDWORKS PDM Professional add-in; i.e., the IEdmAddIn5 interface is not implemented |
| E_EDM_NOT_INITIALIZED | 0x80040201 = The program used an object without properly initializing it |
| E_EDM_NOT_LATEST_VERSION | 0x800402E0 = Item must be checked out to perform this operation |
| E_EDM_NOT_LOGGED_IN | 0x80040204 = You have not logged into the file vault |
| E_EDM_NOT_POWER_USER | 0x80040246 = You are not logged in on Windows as a Power User or Administrator, which is required to run SOLIDWORKS PDM Professional |
| E_EDM_NULL_VALUE | 0x80040240 = A null value was returned where it was not expected |
| E_EDM_OPERATION_REFUSED_BY_PLUGIN | 0x8004021A = The operation was not permitted by one of the installed add-ins |
| E_EDM_OPERATION_UNSUPPORTED_BY_CONISIO_VERSION | 0x8004026B = The operation is not supported by your SOLIDWORKS PDM Professional license |
| E_EDM_PARENT_LOCKED_ELSEWHERE | 0x800402B1 = The file is referenced by a file that is checked out on another computer |
| E_EDM_PARENT_LOCKED_ELSEWHERE_WITHFILE | 0x80040300 = The file is referenced by a file, file_name , that is checked out on another computer |
| E_EDM_PASSWORD_NOT_EMPTY | 0x80040293 = The current login type does not allow passwords to be set |
| E_EDM_PATH_TOO_LONG | 0x80040271 = The path is too long |
| E_EDM_PERMISSION_DENIED | 0x80040203 = You do not have permission to perform this action |
| E_EDM_PICTURE_TOO_BIG | 0x800402E3 = The specified image is too big |
| E_EDM_PREVIEW_NOT_AVAILABLE | 0x800402BF = Preview is not available |
| E_EDM_PRODUCT_TIMEOUT | 0x800402D2 = Your version of SOLIDWORKS PDM Professional has expired; contact your SOLIDWORKS representative for a newer version |
| E_EDM_PROGRAM_VERSION_MISMATCH | 0x80040270 = The server and client are not of the same version |
| E_EDM_RCE_ERROR | 0x80040209 = Error accessing the revision management system; check your network connection |
| E_EDM_REFERENCE_EXISTS | 0x8004027B = The reference already exists |
| E_EDM_REVGEN_EXISTS | 0x8004025E = A revision number component with the specified name already exists |
| E_EDM_REVGENERATOR_IN_USE | 0x80040250 = The revision number component is currently being used by one or more revision numbers and cannot be deleted |
| E_EDM_REVISION_CHANGED | 0x80040253 = The revision number has been changed by another user |
| E_EDM_REVISION_NO_VERSION | 0x80040251 = An attempt was made to set a revision on a version newer than the documents latest version |
| E_EDM_REVISION_ON_OLD_VERSION | 0x80040238 = Cannot set revision on old version |
| E_EDM_REVNUM_EXISTS | 0x8004025F = A revision number with the specified name already exists |
| E_EDM_REVNUMBER_IN_USE | 0x80040255 = The revision number is currently associated with one or more states and cannot be deleted |
| E_EDM_ROLLBACK_ERRORS | 0x800402F7 = Rollback errors |
| E_EDM_ROLLBACK_FOLDER | 0x800402F8 |
| E_EDM_ROLLBACK_PAST_COLDSTORED | 0x80040279 = The rollback operation cannot be performed because one of the versions that you are trying to remove is placed in cold storage |
| E_EDM_SERIAL_NUMBER_NAME_ALREADY_EXISTS | 0x800402AE = The serial number name is already in use |
| E_EDM_SERNO_USED_AS_ITEM_GEN | 0x800402C0 = The serial number cannot be deleted because it is used as an item number generator |
| E_EDM_SERVER_NOT_FOUND | 0x80040220 = The server was not found |
| E_EDM_SKIP_FILE | 0x80040273 = The user selected to skip processing of the current file and go on to the next one |
| E_EDM_SN_FILE_NOT_FOUND | 0x8004023B = Serial number file or add-in could not be found |
| E_EDM_SN_TYPE_OBSOLETE | 0x800402B2 = Serial numbers read from files are no longer supported; please open the serial number in the Administration tool and resave it as a list serial number |
| E_EDM_SQLSERVER_CANNOT_CONNECT | 0x800402C6 = Cannot connect to specified SQL server |
| E_EDM_SQLSERVER_LOGIN_FAILED | 0x800402C4 = Login failed because of an invalid SQL user name or password |
| E_EDM_SQLSERVER_UNSUPPORTED_VERSION | 0x8004027C = The SQL Server version is not supported by SOLIDWORKS PDM Professional; supported versions are SQL Server 2005 SP1 or later |
| E_EDM_STANDARD_APINOTSUPPORTED | 0x800402F2 = The API is not supported in SOLIDWORKS PDM standard version |
| E_EDM_STANDARD_FEATURENOTSUPPORTED | 0x800402ED = This feature is not supported in SOLIDWORKS PDM standard version |
| E_EDM_STANDARD_FEATURENOTSUPPORTED_REFERLOG | 0x800402F9 = This feature is not supported in SOLIDWORKS PDM standard version; refer to the log file for more information |
| E_EDM_STANDARD_PROFLOGINNOTSUPPORTED | 0x800402F3 = Login not supported |
| E_EDM_STANDARD_SQLEDITIONMISMATCH | 0x800402EC = Mismatch between SOLIDWORKS PDM standard version and Microsoft SQL |
| E_EDM_STATE_MULTIPLE_BLOCKING_WARNINGS_FOUND | 0x80040305 = Multiple blocking warnings found |
| E_EDM_STATE_MULTIPLE_WARNINGS_FOUND | 0x80040304 = Multiple warnings found |
| E_EDM_STATE_NOT_FOUND | 0x80040216 = The specified state does not exist |
| E_EDM_STATE_REFERRING_CRS_CONDITION | 0x80040303 = The workflow cannot be deleted since it is used in transition conditions |
| E_EDM_SWDRW_SETTO_USE_INDEPENDENT_REV_TABLE | 0x800402FF = Independent type revision setting is used in the drawing |
| E_EDM_SWFILE_MISSING_XMLSTREAM | 0x800402F5 = SOLIDWORKS file missing XML stream |
| E_EDM_SWSEC_LICENSE_CHECKIN_FAILED | 0x800402E7 = The check-in failed |
| E_EDM_SWSEC_LICENSE_CHECKIN_FAILED_PRO | 0x800402EF = Check-in failed in SOLIDWORKS PDM Professional |
| E_EDM_SWSEC_LICENSE_CHECKIN_FAILED_STD | 0x800402F1 = Check-in failed in SOLIDWORKS PDM standard version |
| E_EDM_SWSEC_LICENSE_CHECKOUT_FAILED | 0x800402E6 = Check-out failed |
| E_EDM_SWSEC_LICENSE_CHECKOUT_FAILED_PRO | 0x800402EE = Check-out failed in SOLIDWORKS PDM Professional |
| E_EDM_SWSEC_LICENSE_CHECKOUT_FAILED_STD | 0x800402F0 = Check-out failed in SOLIDWORKS PDM standard version |
| E_EDM_SWSEC_LICENSE_CONNECTION_LOST | 0x800402E9 = The connection was lost |
| E_EDM_SWSEC_LICENSE_SERVERQUERY_FAILED | 0x800402E8 = The server query failed |
| E_EDM_TEMPLATE_IMPORT_WITHOUT_LOCAL_VIEW | 0x800402F6 = Template imported iwthout local view |
| E_EDM_TOO_MANY_USERS | 0x80040248 = The licensed maximum number of simultaneously logged-in users would be exceeded by this log-in; this log-in was refused |
| E_EDM_TOOLBOX_FILE_LOCATED_IN_NONTOOLBOX_FOLDER | 0x800402FA = Toolbox file must be located in a Toolbox folder |
| E_EDM_TRANSITION_ACTION_FAILED | 0x80040234 = An error occurred when trying to execute a transition action |
| E_EDM_UNC_PATH_ADDIN_NOT_SUPPORTED | 0x800402DD = Information cannot be retrieved from add-ins on a network drive; copy the file to the local hard disk and retry the operation |
| E_EDM_UNSUPPORTED_OS | 0x800402D3 = The version of the operating system is not supported |
| E_EDM_UNSUPPORTED_PROGRAM_VERSION | 0x8004023E = The program requires a higher version of SOLIDWORKS PDM Professional than the installed version |
| E_EDM_UNSUPPORTED_SN_TYPE | 0x8004026F = The serial number type is not supported |
| E_EDM_UPDATE_ATT_FAILED | 0x8004020D = Could not update attributes during check in |
| E_EDM_USER_BLOCKED | 0x80040265 = The administrator has blocked your login name in this file vault |
| E_EDM_USER_NAME_ALREADY_EXISTS | 0x8004028A = The user name already exists |
| E_EDM_USER_NAME_NOT_UNIQUE | 0x80040288 = The user name is not unique in the specified array of users |
| E_EDM_USER_NOT_FOUND_IN_ARCHIVE_SERVER | 0x80040292 = The user name does not exist in the archive server |
| E_EDM_VALUE_NOT_UNIQUE | 0x8004022C = An attempt was made to save a duplicate value when a unique value is required |
| E_EDM_VARIABLE_NOT_FOUND | 0x80040252 = The specified card variable is missing |
| E_EDM_VARIABLE_USED_IN_COLUMN | 0x80040244 = The variable cannot be deleted because it is used in a user-defined column |
| E_EDM_VARIABLE_USED_IN_EXPORT_SCRIPT | 0x800402AA = The variable cannot be deleted because it is used in a data export rule |
| E_EDM_VARIABLE_USED_IN_WORKFLOW_STATE | 0x800402EB = The variable cannot be deleted because it is used in a workflow state |
| E_EDM_VAULT_ALREADY_EXISTS | 0x8004024D = A vault with the same name already exists on the archive server |
| E_EDM_VERSION_MISMATCH | 0x8004022E = The versions of the program and the file vault are incompatible |
| E_EDM_WF_HAS_FILES | 0x8004024A = The workflow contains files and cannot be deleted |
| E_EDM_XREF_OUTSIDE_VAULT | 0x8004026C = One or more of the file's referenced files are outside the file vault |
| E_ITEM_CANNOT_COPY_ITEM | 0x800402BA = You have selected items to copy; the items cannot be copied because they must be unique within the system |
| E_ITEM_CYCLIC_REFERENCE | 0x800402CA = Operation aborted because it would create a cyclic reference between items |
| E_ITEM_ILLEGAL_MOVE_REFERENCED_BY_EXTERNAL | 0x800402C8 = The object cannot be moved because the object or a sub-object is referenced by a locked item |
| E_ITEM_ILLEGAL_RENAME_REFERENCED_BY_EXTERNAL | 0x800402C9 = The object cannot be renamed because the object or a sub-object is referenced by a locked item |
| E_ITEM_INVALID_ITEM_TYPE | 0x800402BB = Invalid object type; only Item, ItemFolder, and files are supported by Item Explorer |
| E_ITEM_INVALID_LINK_OPERATION | 0x800402B8 = This operation cannot be performed on the selected items |
| E_ITEM_INVALID_LINK_TYPE | 0x800402B7 = Invalid link type; only two link types are supported by Item Explorer, static and auto-update |
| E_ITEM_INVALID_OBJECT | 0x800402BD = Item object contains corrupted data |
| E_ITEM_INVALID_SOURCE | 0x800402B5 = The selection contains items that are not valid for this operation |
| E_ITEM_INVALID_TARGET | 0x800402B4 = The destination object is invalid for this operation |
| E_ITEM_LINK_DUPLICATED | 0x800402B9 = The file is already added to this item |
| E_ITEM_LOCKED_ELSEWHERE | 0x800402DF = Item is locked on another computer |
| E_ITEM_MANY_DYN_LINKS | 0x800402B6 = This item already has an auto-update link attached to it; items can have only one auto-update link at a time |
| E_ITEM_NO_ITEM_GEN_DEFINED | 0x800402BC = No serial number generator has been set up to generate item numbers. Please do the following: Launch SOLIDWORKS PDM Professional Administration Tool. Create a serial number. Open the Items administration node and select the serial number. |
| E_ITEM_NOT_CONNECTED | 0x800402C1 = This item has no file linked or connected to it |
| E_ITEM_NOT_LOCKED | 0x800402DE = Item has to be checked out to perform this operation |
| E_ITEM_UP_TO_DATE | 0x800402BE = The item is up to date |

## Examples

Client code can only access these return codes by handling the exception. For example, in C#:

try
{
// Some SOLIDWORKS PDM Professional call that results in an exception
}
catch (System.Runtime.InteropServices.ComException comEx)
{
switch (comEx.ErrorCode)
{
case E_EDM_`xxx`:
// respond to`xxx`
break;
case E_EDM_`yyy`:
// respond to`yyy`
break;
default:
// Unexpected or cannot be handled silently
// Use IEdmVault5::GetErrorString or IEdmVault11::GetErrorMessage to prepare a message for the user or log
break;
}
}

## Remarks

HRESULT return codes are supported by the SOLIDWORKS PDM Professional API. You can pass the HRESULT code to the method IEdmVault11::GetErrorMessage to get information about the code.

NOTES:

- Methods called from Visual Basic do not return the HRESULT code directly. Instead, the return codes are returned as an argument declared with the [retval] directive, if one exists. Visual Basic users can view the error codes returned by methods by implementing an error handler and checking the Number property of the Err object. The property is the HRESULT return code from the failing method.
- The values shown in this topic are written in C++ style hexadecimal notation. In VB.NET, the value 0x80040200 is written as &H80040200.

## See Also

[EPDM.Interop.EPDMResultCode Namespace](EPDM.Interop.EPDMResultCode~EPDM.Interop.EPDMResultCode_namespace.html)

[IEdmVault5::GetErrorString Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetErrorString.html)

[IEdmVault11::GetErrorName Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~GetErrorName.html)

[Return Codes](ReturnCodes.htm)
