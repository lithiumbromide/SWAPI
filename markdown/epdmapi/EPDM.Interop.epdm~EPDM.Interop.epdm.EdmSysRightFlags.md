---
title: "EdmSysRightFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmSysRightFlags"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSysRightFlags.html"
---

# EdmSysRightFlags Enumeration

Obsolete. Superseded by [EdmSysPerm](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSysPerm.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmSysRightFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmSysRightFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmSysRightFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmSysRight_CanAddDelLabels | 2048 = May add and delete labels |
| EdmSysRight_CanPurgeHistory | 1024 = May delete the contents of history listings |
| EdmSysRight_CantIgnoreWarnings | 4096 = May not click OK in the check in, check out, Get, etc. dialog boxes if there are warnings in them |
| EdmSysRight_EditAddins | 4 = May install or uninstall add-ins |
| EdmSysRight_EditReportQuery | 512 = May use the Report Generator |
| EdmSysRight_EditSharedSearchQuery | 64 = May update shared search favorites |
| EdmSysRight_EditTemplates | 256 = May run the Template Manager |
| EdmSysRight_EditUserMgr | 1 = May run the User Manager |
| EdmSysRight_EditWorkflow | 2 = May run the Workflow Editor |
| EdmSysRight_ExportWebFolder | 128 = May export file vault folders to the internet |
| EdmSysRight_MandatoryMailLogin | 32 = Must enter password before sending email |
| EdmSysRight_MandatoryStateComments | 16 = Must enter change state comments |
| EdmSysRight_MandatoryVersionComments | 8 = Must enter version comments |
| EdmSysRight_MaySeeAdminTool | 67108864 = May see the Administration tool in the Tools menu in the File Explorer |
| EdmSysRight_ModifyCardLists | 131072 = May update lists used in cards |
| EdmSysRight_ModifyCategories | 8192 = May update category definitions in the SOLIDWORKS PDM Professional Administration tool |
| EdmSysRight_ModifyColdStore | 268435456 = May update the cold storage settings |
| EdmSysRight_ModifyColumns | 65536 = May update column definitions |
| EdmSysRight_ModifyERPCfg | 1073741824 = May update ERP import/export settings |
| EdmSysRight_ModifyIndexing | 536870912 = May update indexing settings |
| EdmSysRight_ModifyItemNoGen | 2097152 = May update item settings |
| EdmSysRight_ModifyLicenseKey | 524288 = May enter a new license key |
| EdmSysRight_ModifyMailCfg | 1048576 = May update the notification settings |
| EdmSysRight_ModifyReplication | 4194304 = May update replication settings |
| EdmSysRight_ModifyRevisionNumbers | 32768 = May update the definition of revision numbers |
| EdmSysRight_ModifySearchForms | 16777216 = May update search forms |
| EdmSysRight_ModifySerialNumbers | 262144 = May update serial number generators |
| EdmSysRight_ModifyTemplateForms | 33554432 = May update template input forms |
| EdmSysRight_ModifyVariables | 16384 = May update variable definitions |
| EdmSysRight_None | 0 = No permissions |
| EdmSysRight_RefuseLogin | 134217728 = Block the user from logging in |

## Remarks

Flags that indicate which SOLIDWORKS PDM Professional permissions a user has, etc. [Bitmask](Bitmasks.htm).

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
