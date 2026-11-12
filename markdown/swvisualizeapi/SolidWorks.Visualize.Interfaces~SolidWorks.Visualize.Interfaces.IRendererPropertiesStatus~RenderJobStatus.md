---
title: "RenderJobStatus Property (IRendererPropertiesStatus)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRendererPropertiesStatus"
member: "RenderJobStatus"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus~RenderJobStatus.html"
---

# RenderJobStatus Property (IRendererPropertiesStatus)

Gets the render job status.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property RenderJobStatus As RenderJobStatus_e
```

### Visual Basic (Usage)

```vb
Dim instance As IRendererPropertiesStatus
Dim value As RenderJobStatus_e

value = instance.RenderJobStatus
```

### C#

```csharp
RenderJobStatus_e RenderJobStatus {get;}
```

### C++/CLI

```cpp
property RenderJobStatus_e RenderJobStatus {
   RenderJobStatus_e get();
}
```

### Property Value

Render job status as defined by [RenderJobStatus_e](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.RenderJobStatus_e.html)

## VBA Syntax

See [IRendererPropertiesStatus::RenderJobStatus](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRendererPropertiesStatus~RenderJobStatus.html).

## Examples

See the [IRenderNotificationHandler](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler.html) example.

## See Also

[IRendererPropertiesStatus Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus.html)
[IRendererPropertiesStatus Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
