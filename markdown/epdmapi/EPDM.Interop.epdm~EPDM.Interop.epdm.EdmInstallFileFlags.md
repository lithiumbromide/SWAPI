---
title: "EdmInstallFileFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmInstallFileFlags"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmInstallFileFlags.html"
---

# EdmInstallFileFlags Enumeration

Operations used in calls to [IEdmVault12::InstallFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault12~InstallFile.html) to control the installation of data.

## Syntax

### Visual Basic

```vb
Public Enum EdmInstallFileFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmInstallFileFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmInstallFileFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmIff_Nothing | 0 = Default operation |
| EdmIff_ReplaceDuplicates | 1 = This flag is used for CEX-files when you want to replace duplicate objects in the vault; i.e., if you are importing a group named "ABC" and if there is already a different group named "ABC" in the vault, it will be silently replaced; the default behavior is not to replace duplicates |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
