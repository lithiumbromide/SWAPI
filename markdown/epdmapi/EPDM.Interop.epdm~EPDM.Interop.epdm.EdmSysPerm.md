---
title: "EdmSysPerm Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmSysPerm"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSysPerm.html"
---

# EdmSysPerm Enumeration

Types of system permissions for a user or group.

## Syntax

### Visual Basic

```vb
Public Enum EdmSysPerm
   Inherits System.Enum
```

### C#

```csharp
public enum EdmSysPerm : System.Enum
```

### C++/CLI

```cpp
public enum class EdmSysPerm : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmSysPerm_AcceptTasks | 1026 = May accept tasks to execute on a host |
| EdmSysPerm_CanAddCustomColsInFileDetails | 1032 = May add custom columns in File details |
| EdmSysPerm_CanAddCustomColsInFileOperations | 1033 = May add custom columns in File operations |
| EdmSysPerm_CanAddDelLabels | 2048 = May add and delete labels |
| EdmSysPerm_CanDeleteLabels | 1029 = May delete labels |
| EdmSysPerm_CanPurgeHistory | 1024 = May purge history listings |
| EdmSysPerm_CanSetLabels | 1030 = May set labels |
| EdmSysPerm_CantIgnoreWarnings | 4096 = Cannot click OK in the Check-in, Check-out, Get, etc., dialog boxes if there are any warnings in them |
| EdmSysPerm_CanUndoCheckOutAndCheckInForOthers | 1028 = May check in a file checked out to a different user in the same vault view May undo checkouts of files that are checked out to a different user in the same or different vault view Default permission for the Admin user in a new or upgraded 2018 vault Applicable to all users/groups |
| EdmSysPerm_CanUpdateHistoryComments | 1031 = May delete history comments |
| EdmSysPerm_CanViewTask | 1034 = may view task list |
| EdmSysPerm_EditAddins | 4 = May install or uninstall add-ins |
| EdmSysPerm_EditReportQuery | 512 = May modify report queries |
| EdmSysPerm_EditSharedSearchQuery | 64 = May update shared search favorites |
| EdmSysPerm_EditTemplates | 256 = May update templates |
| EdmSysPerm_EditUserMgr | 1 = May update user and group properties |
| EdmSysPerm_EditWorkflow | 2 = May edit workflows |
| EdmSysPerm_ExportWebFolder | 128 = May export file vault folders to the internet |
| EdmSysPerm_MandatoryMailLogin | 32 = Must enter password before sending email |
| EdmSysPerm_MandatoryStateComments | 16 = Must enter change state comments |
| EdmSysPerm_MandatoryVersionComments | 8 = Must enter version comments |
| EdmSysPerm_MaySeeAdminTool | 67108864 = May see the Administration tool menu command item in File Explorer |
| EdmSysPerm_ModifyCardLists | 131072 = May update definitions of lists used in cards |
| EdmSysPerm_ModifyCategories | 8192 = May update category definitions |
| EdmSysPerm_ModifyColdStore | 268435456 = May update the cold storage settings |
| EdmSysPerm_ModifyColumns | 65536 = May update column definitions, including BOM definitions |
| EdmSysPerm_ModifyERPCfg | 1073741824 = May update XML Import and Export settings |
| EdmSysPerm_ModifyIndexing | 536870912 = May update the indexing settings |
| EdmSysPerm_ModifyItemNoGen | 2097152 = May administrate items |
| EdmSysPerm_ModifyLicenseKey | 524288 = May enter a new license key |
| EdmSysPerm_ModifyMailCfg | 1048576 = May update the notification settings |
| EdmSysPerm_ModifyReplication | 4194304 = May update vault replication settings |
| EdmSysPerm_ModifyRevisionNumbers | 32768 = May update the definition of revision numbers |
| EdmSysPerm_ModifySearchForms | 16777216 = May save search cards with the card editor |
| EdmSysPerm_ModifySerialNumbers | 262144 = May update serial number generators |
| EdmSysPerm_ModifyTasks | 1025 = May manage task definitions in the Administration tool |
| EdmSysPerm_ModifyTemplateForms | 33554432 = May save template cards with the card editor |
| EdmSysPerm_ModifyToolbox | 1027 = May update Toolbox Library settings in the Administration tool |
| EdmSysPerm_ModifyVariables | 16384 = May update variable definitions |
| EdmSysPerm_None | 0 = No rights at all |
| EdmSysPerm_RefuseLogin | 134217728 = Block the user from logging in |

## Remarks

This enumeration was added in SOLIDWORKS PDM Professional 2010 and supersedes the [EdmSysRightFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSysRightFlags.html) enumeration.

Always use the [IEdmUser7::HasSysRightEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser7~HasSysRightEx.html) and [IEdmUserGroup6::HasSysRightEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup6~HasSysRightEx.html) methods instead of the obsoleted [IEdmUser5::HasSysRight](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser5~HasSysRight.html) and [IEdmUserGroup5::HasSysRight](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5~HasSysRight.html) methods when writing code for SOLIDWORKS PDM Professional 2010 and later.

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
