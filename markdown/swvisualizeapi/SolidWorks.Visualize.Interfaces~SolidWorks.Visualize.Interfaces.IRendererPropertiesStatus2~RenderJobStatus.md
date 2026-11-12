---
title: "RenderJobStatus Property (IRendererPropertiesStatus2)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRendererPropertiesStatus2"
member: "RenderJobStatus"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2~RenderJobStatus.html"
---

# RenderJobStatus Property (IRendererPropertiesStatus2)

Gets the render job status.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property RenderJobStatus As RenderJobStatus_e
```

### Visual Basic (Usage)

```vb
Dim instance As IRendererPropertiesStatus2
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

[IRendererPropertiesStatus2 Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2.html)
[IRendererPropertiesStatus2 Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
