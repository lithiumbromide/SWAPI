---
title: "OnRenderActionRequested Method (IRenderCallbackHandler)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRenderCallbackHandler"
member: "OnRenderActionRequested"
kind: "method"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderCallbackHandler~OnRenderActionRequested.html"
---

# OnRenderActionRequested Method (IRenderCallbackHandler)

Sends the specified control instruction to the rendering engine during an ongoing asynchronous render.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnRenderActionRequested( _
   ByVal renderAction As RenderAction_e _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderCallbackHandler
Dim renderAction As RenderAction_e

instance.OnRenderActionRequested(renderAction)
```

### C#

```csharp
void OnRenderActionRequested(
   RenderAction_e renderAction
)
```

### C++/CLI

```cpp
void OnRenderActionRequested(
   RenderAction_e renderAction
)
```

### Parameters

- `renderAction`: Action to take as defined by [RenderAction_e](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.RenderAction_e.html)

## VBA Syntax

See [IRenderCallbackHandler::OnRenderActionRequested](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRenderCallbackHandler~OnRenderActionRequested.html).

## Remarks

Call this method to request cancellation of the render or to cancel and save intermediate results.

## See Also

[IRenderCallbackHandler Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderCallbackHandler.html)
[IRenderCallbackHandler Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderCallbackHandler_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2026 FCS
