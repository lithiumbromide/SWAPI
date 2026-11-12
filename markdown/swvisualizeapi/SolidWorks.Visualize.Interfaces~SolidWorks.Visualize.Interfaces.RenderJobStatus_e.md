---
title: "RenderJobStatus_e Enumeration"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "RenderJobStatus_e"
member: ""
kind: "enum"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.RenderJobStatus_e.html"
---

# RenderJobStatus_e Enumeration

Render job status codes (see [Bitmasks](ms-its:sldworksAPIProgGuide.chm:://Overview/Bitmasks.htm))

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum RenderJobStatus_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As RenderJobStatus_e
```

### C#

```csharp
public enum RenderJobStatus_e : System.Enum
```

### C++/CLI

```cpp
public enum class RenderJobStatus_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| CopyingToJobFolder | 1 or 0x01 |
| CopyToJobFolderComplete | 2 or 0x02 |
| JobAborted | 2048 or 0x800 |
| JobCancelled | 4096 or 0x1000 |
| JobComplete | 1024 or 0x400 |
| JobFailed | 256 or 0x100 |
| JobFailedNoLicense | 512 or 0x200 |
| LoadingDocument | 32768 or 0x8000 |
| NotFound | 8192 or 0x2000 |
| Outputting | 64 or 0x40 |
| OutputtingComplete | 128 or 0x80 |
| Paused | 16384 or 0x4000 |
| Queued | 4 or 0x04 |
| RenderComplete | 32 or 0x20 |
| Rendering | 16 or 0x10 |
| RenderInitializing | 8 or 0x08 |
| SaveComplete | 65536 or 0x10000 |
| Undetermined | 0 |

## Examples

See the [IRenderNotificationHandler](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler.html) example.

## See Also

[SolidWorks.Visualize.Interfaces Namespace](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces_namespace.html)
