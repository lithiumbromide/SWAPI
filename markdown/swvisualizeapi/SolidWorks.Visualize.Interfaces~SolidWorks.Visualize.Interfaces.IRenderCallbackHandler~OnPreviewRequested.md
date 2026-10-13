---
title: "OnPreviewRequested Method (IRenderCallbackHandler)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRenderCallbackHandler"
member: "OnPreviewRequested"
kind: "method"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderCallbackHandler~OnPreviewRequested.html"
---

# OnPreviewRequested Method (IRenderCallbackHandler)

Requests a preview image of the specified size from the rendering engine during an ongoing asynchronous render.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnPreviewRequested( _
   ByVal width As System.Integer, _
   ByVal height As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderCallbackHandler
Dim width As System.Integer
Dim height As System.Integer

instance.OnPreviewRequested(width, height)
```

### C#

```csharp
void OnPreviewRequested(
   System.int width,
   System.int height
)
```

### C++/CLI

```cpp
void OnPreviewRequested(
   System.int width,
   System.int height
)
```

### Parameters

- `width`: Width in pixels of the preview image
- `height`: Height in pixels of the preview image

## VBA Syntax

See [IRenderCallbackHandler::OnPreviewRequested](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRenderCallbackHandler~OnPreviewRequested.html).

## Remarks

The rendering engine responds by invoking [IRenderNotificationHandler2::RendererPropertyChangedNotify](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler2~RendererPropertyChangedNotify.html) with the updated preveiw image included in the status.

Both image size and the frequency at which preview images are requested may negatively impact overall rendering performance. Use sparingly to avoid delays or degraded output quality.

## See Also

[IRenderCallbackHandler Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderCallbackHandler.html)
[IRenderCallbackHandler Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderCallbackHandler_members.html)
[IRenderNotificationHandler2::RendererPropertyChangedNotify Method ()](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler2~RendererPropertyChangedNotify.html)

## Availability

SOLIDWORKS Visualize Add-in API 2026 FCS
