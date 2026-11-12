---
title: "RendererPropertyChangedNotify Method (IRenderNotificationHandler2)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRenderNotificationHandler2"
member: "RendererPropertyChangedNotify"
kind: "method"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler2~RendererPropertyChangedNotify.html"
---

# RendererPropertyChangedNotify Method (IRenderNotificationHandler2)

Called whenever there is a change in a render property during an ongoing render operation.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RendererPropertyChangedNotify( _
   ByVal renderProperty As RenderProperty_e, _
   ByVal rendererPropertiesStatus As IRendererPropertiesStatus2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderNotificationHandler2
Dim renderProperty As RenderProperty_e
Dim rendererPropertiesStatus As IRendererPropertiesStatus2

instance.RendererPropertyChangedNotify(renderProperty, rendererPropertiesStatus)
```

### C#

```csharp
void RendererPropertyChangedNotify(
   RenderProperty_e renderProperty,
   IRendererPropertiesStatus2 rendererPropertiesStatus
)
```

### C++/CLI

```cpp
void RendererPropertyChangedNotify(
   RenderProperty_e renderProperty,
   IRendererPropertiesStatus2^ rendererPropertiesStatus
)
```

### Parameters

- `renderProperty`: The specific render property that has changed as defined by [RenderProperty_e](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.RenderProperty_e.html)
- `rendererPropertiesStatus`: [IRendererPropertiesStatus2](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2.html)

## VBA Syntax

See [IRenderNotificationHandler2::RendererPropertyChangedNotify](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRenderNotificationHandler2~RendererPropertyChangedNotify.html).

## Remarks

Use this method to receive updates such as progress changes, frame counts, elapsed time, job status updates, or updated preview images (if those have been previously requested).

## See Also

[IRenderNotificationHandler2 Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler2.html)
[IRenderNotificationHandler2 Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler2_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2026 FCS
