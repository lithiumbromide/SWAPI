---
title: "EdmGroupSetting Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGroupSetting"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupSetting.html"
---

# EdmGroupSetting Enumeration

User group settings used by [IEdmUserGroup9::SetSettingsVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup9~SetSettingsVar.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmGroupSetting
   Inherits System.Enum
```

### C#

```csharp
public enum EdmGroupSetting : System.Enum
```

### C++/CLI

```cpp
public enum class EdmGroupSetting : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmGSv_AutoDelete | 9 = Whether to automatically delete local read-only files that are not part of the vault; 1 = true, 0 = false; this setting corresonds to the "Automatically delete local read-only files that are not part of the file vault" checkbox on the Explorer tab on the Settings dialog that appears when you click "Settings" on the Properties dialog of a group in the Admin Tool |
| EdmGSv_AutoGetLatest | 11 = Whether to always work with the latest version of files; 1 = true, 0 = false; this setting corresponds to the "Always work with latest version of files" checkbox on the Reference Dialog tab on the Settings dialog that appears when you click "Settings" on the Properties dialog of a group in the Admin Tool |
| EdmGSv_AutoGetLatestRefs | 43 = Whether to auto-select reference files to get latest when checking out; 1 = true, 0 = false; this setting corresponds to the "Auto select reference files to get latest when checking out" checkbox on the Reference Dialog tab on the Settings dialog that appears when you click "Settings" on the Properties dialog of a group in the Admin Tool |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
