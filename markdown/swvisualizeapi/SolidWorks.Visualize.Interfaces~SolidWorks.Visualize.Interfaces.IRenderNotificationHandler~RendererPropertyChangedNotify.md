---
title: "RendererPropertyChangedNotify Method (IRenderNotificationHandler)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRenderNotificationHandler"
member: "RendererPropertyChangedNotify"
kind: "method"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler~RendererPropertyChangedNotify.html"
---

# RendererPropertyChangedNotify Method (IRenderNotificationHandler)

Obsolete. Superseded by [IRenderNotificationHandler2::RendererPropertyChangedNotify](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler2~RendererPropertyChangedNotify.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub RendererPropertyChangedNotify( _
   ByVal renderProperty As RenderProperty_e, _
   ByVal rendererPropertiesStatus As IRendererPropertiesStatus _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderNotificationHandler
Dim renderProperty As RenderProperty_e
Dim rendererPropertiesStatus As IRendererPropertiesStatus

instance.RendererPropertyChangedNotify(renderProperty, rendererPropertiesStatus)
```

### C#

```csharp
void RendererPropertyChangedNotify(
   RenderProperty_e renderProperty,
   IRendererPropertiesStatus rendererPropertiesStatus
)
```

### C++/CLI

```cpp
void RendererPropertyChangedNotify(
   RenderProperty_e renderProperty,
   IRendererPropertiesStatus^ rendererPropertiesStatus
)
```

### Parameters

- `renderProperty`: Render property as defined by [RenderProperty_e](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.RenderProperty_e.html)
- `rendererPropertiesStatus`: [IRendererPropertiesStatus](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus.html)

## VBA Syntax

See [IRenderNotificationHandler::RendererPropertyChangedNotify](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRenderNotificationHandler~RendererPropertyChangedNotify.html).

## Remarks

Implement this method to handle updates on render progress, render status, as well as previously requested preview images.

## See Also

[IRenderNotificationHandler Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler.html)
[IRenderNotificationHandler Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
