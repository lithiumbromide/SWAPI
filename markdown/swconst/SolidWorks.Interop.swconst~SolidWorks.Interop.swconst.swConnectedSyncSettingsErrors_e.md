---
title: "swConnectedSyncSettingsErrors_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swConnectedSyncSettingsErrors_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConnectedSyncSettingsErrors_e.html"
---

# swConnectedSyncSettingsErrors_e Enumeration

Return codes for [ISldWorks::UploadToMySolidWorksSettings](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UploadToMySolidWorksSettings.html) and [ISldWorks::DownloadFromMySolidWorksSettings](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DownloadFromMySolidWorksSettings.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swConnectedSyncSettingsErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swConnectedSyncSettingsErrors_e
```

### C#

```csharp
public enum swConnectedSyncSettingsErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class swConnectedSyncSettingsErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swConnectedSyncSettings_ConnectedDisabled | 1 |
| swConnectedSyncSettings_ConnectedNotLoggedIn | 2 |
| swConnectedSyncSettings_Success | 0 |
| swConnectedSyncSettings_UploadDownloadError | 3 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
